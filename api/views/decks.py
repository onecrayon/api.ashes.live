from typing import Union

from fastapi import APIRouter, Depends, Request, Query

from api import db
from api.depends import (
    paging_options,
    get_session,
    login_required,
    AUTH_RESPONSES,
    get_current_user,
)
from api.exceptions import NoUserAccessException, APIException, NotFoundException
from api.models import User, Deck, Card, AnonymousUser, Release
from api.schemas import DetailResponse
from api.schemas.decks import DeckFilters, DeckListingOut, DeckOut, DeckIn, DeckDetails
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.services.deck import (
    create_or_update_deck,
    NoSuchDeck,
    PhoenixbornInDeck,
    get_decks_query,
    paginate_deck_listing,
    deck_to_dict,
)

router = APIRouter()


@router.get(
    "/decks",
    response_model=DeckListingOut,
    response_model_exclude_unset=True,
)
def list_published_decks(
    request: Request,
    filters: DeckFilters = Depends(),
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    # Standard dependencies
    paging: PaginationOptions = Depends(paging_options),
    session: db.Session = Depends(get_session),
):
    """Get a paginated listing of published snapshots with optional filters.

    ## Available filters

    * `q`: deck title search
    * `phoenixborn`: list of Phoenixborn slugs
    * `player`: list of player badges
    * `show_legacy` (default: false): if true, legacy 1.0 decks will be returned
    """
    query = get_decks_query(
        session,
        show_legacy=filters.show_legacy,
        is_public=True,
        order=order,
        q=filters.q,
        phoenixborn=filters.phoenixborn,
        cards=filters.card,
        players=filters.player,
    )
    return paginate_deck_listing(query, session, request, paging)


@router.get(
    "/decks/{deck_id}",
    response_model=DeckDetails,
    responses={
        404: {
            "model": DetailResponse,
            "description": "No public snapshot available for this source deck ID.",
        },
        **AUTH_RESPONSES,
    },
)
def get_deck(
    deck_id: int,
    show_saved: bool = Query(
        False,
        description="When viewing a source deck ID, whether the actual latest save should be returned.",
    ),
    session: db.Session = Depends(get_session),
    current_user: Union["User", "AnonymousUser"] = Depends(get_current_user),
):
    """Read a single deck's details.

    This endpoint will return different information depending on the requesting user. For decks the
    user did not create (and for anonymous users):

    * passing a source deck's ID will always return the most recent published snapshot
    * passing a published snapshot's ID will return that snapshot
    * passing a private snapshot's ID (or a deck ID without any public snapshots) will throw an
      authentication error

    For authenticated users who own the deck:

    * passing a source deck's ID will return the most recent published snapshot
    * passing a source deck's ID with the query parameter `show_saved=true` will return the most
      recent saved copy of that deck (allows previewing how a deck will display prior to creating
      a public snapshot)
    * passing any snapshot's ID will return that snapshot
    """
    source_deck = session.query(Deck).get(deck_id)
    own_deck = (
        not current_user.is_anonymous() and source_deck.user_id == current_user.id
    )
    if (
        source_deck.is_snapshot
        and not source_deck.is_public
        and not own_deck
        or (not own_deck and show_saved)
    ):
        raise NoUserAccessException(detail="You do not have access to this deck.")
    deck_dict = None
    # Check for the instances where we just return the source deck (separated into discrete
    #  conditionals to make things more readable)
    # Public snapshots simply get returned
    if source_deck.is_snapshot and source_deck.is_public:
        deck_dict = deck_to_dict(session, deck=source_deck)
    # Private snapshots get returned if the user owns the deck
    elif source_deck.is_snapshot and own_deck:
        deck_dict = deck_to_dict(session, deck=source_deck)
    # The actual deck gets returned if we are showing the latest saved copy
    elif not source_deck.is_snapshot and own_deck and show_saved:
        deck_dict = deck_to_dict(session, deck=source_deck)
    # By default, re-route to the latest public snapshot
    else:
        deck = (
            session.query(Deck)
            .filter(
                Deck.source_id == source_deck.id,
                Deck.is_snapshot.is_(True),
                Deck.is_public.is_(True),
            )
            .order_by(Deck.created.desc())
            .first()
        )
        if not deck:
            raise NotFoundException(detail="Deck not found.")
        deck_dict = deck_to_dict(session, deck=deck)

    # And finally look up the releases that are required by this deck
    card_stubs = set(x["stub"] for x in deck_dict["cards"])
    card_stubs.add(deck_dict["phoenixborn"]["stub"])
    release_stubs = set()
    # Even if cards don't require a particular set, check for dice
    dice_to_release = {
        "ceremonial": "master-set",
        "charm": "master-set",
        "illusion": "master-set",
        "natural": "master-set",
        "divine": "the-law-of-lions",
        "sympathy": "the-song-of-soaksend",
        "time": "the-breaker-of-fate",
    }
    for die in deck_dict["dice"]:
        release_stubs.add(dice_to_release[die["name"]])
    release_results = (
        session.query(Release, Deck)
        .outerjoin(Card, Card.release_id == Release.id)
        .outerjoin(Deck, Deck.preconstructed_release == Release.id)
        .filter(
            db.or_(
                Release.stub.in_(release_stubs),
                Card.stub.in_(card_stubs),
            ),
            Release.is_legacy.is_(bool(deck_dict.get("is_legacy"))),
        )
        .order_by(Release.id.asc())
        .distinct(Release.id)
        .all()
    )
    release_data = []
    for result in release_results:
        release_data.append(
            {
                "name": result.Release.name,
                "stub": result.Release.stub,
                "is_legacy": result.Release.is_legacy,
                "preconstructed_deck_id": (
                    result.Deck.source_id if result.Deck else None
                ),
            }
        )

    return {
        "releases": release_data,
        "deck": deck_dict,
    }


@router.put(
    "/decks",
    response_model=DeckOut,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Deck creation failed.",
        },
        **AUTH_RESPONSES,
    },
)
def save_deck(
    data: DeckIn,
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Create or update a deck in place.

    **This is not a patch!** You must pass the entire deck object in the body every time, and it
    will only be treated as an update if there is an ID included.
    """
    # Verify that the user has access to this deck, if we're saving over an existing deck
    if data.id:
        deck_check: Deck = session.query(Deck.user_id).get(data.id)
        if not deck_check or deck_check.user_id != current_user.id:
            raise NoUserAccessException(detail="You cannot save a deck you do not own.")
        if deck_check.is_legacy:
            raise APIException(detail="Legacy decks cannot be saved.")
        if deck_check.is_snapshot:
            raise APIException(detail="You cannot save over a snapshot.")
    # Ensure we have a Phoenixborn stub
    phoenixborn_stub = (
        data.phoenixborn
        if isinstance(data.phoenixborn, str)
        else data.phoenixborn.get("stub")
    )
    phoenixborn = (
        session.query(Card.id)
        .filter(Card.stub == phoenixborn_stub, Card.is_legacy.is_(False))
        .first()
    )
    if not phoenixborn:
        raise APIException(detail="Valid Phoenixborn is required.")
    try:
        deck = create_or_update_deck(
            session,
            phoenixborn_id=phoenixborn.id,
            deck_id=data.id,
            title=data.title,
            description=data.description,
            dice=[x.dict() for x in data.dice] if data.dice else None,
            cards=[x.dict() for x in data.cards] if data.cards else None,
            first_five=data.first_five,
            effect_costs=data.effect_costs,
            tutor_map=data.tutor_map,
        )
    except NoSuchDeck:
        raise NotFoundException()
    except PhoenixbornInDeck:
        raise APIException(
            detail="Your deck listing includes a Phoenixborn. Please pass the Phoenixborn at the root level of the deck object."
        )
    return deck_to_dict(session, deck=deck)

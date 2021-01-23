from typing import Union

from fastapi import APIRouter, Depends, Request, Query, status

from api import db
from api.depends import (
    paging_options,
    get_session,
    login_required,
    AUTH_RESPONSES,
    get_current_user,
)
from api.exceptions import NoUserAccessException, APIException, NotFoundException
from api.models import (
    User,
    Deck,
    Card,
    AnonymousUser,
    Release,
    DeckCard,
    DeckDie,
    DeckSelectedCard,
)
from api.schemas import DetailResponse
from api.schemas.decks import (
    DeckFilters,
    DeckListingOut,
    DeckOut,
    DeckIn,
    DeckDetails,
    SnapshotIn,
    DeckFiltersMine,
)
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.services.deck import (
    create_or_update_deck,
    NoSuchDeck,
    PhoenixbornInDeck,
    get_decks_query,
    paginate_deck_listing,
    deck_to_dict,
)
from api.services.stream import (
    create_entity,
    refresh_stream_for_entity,
    update_subscription_for_user,
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
    * `card`: list of card slugs
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
    "/decks/mine",
    response_model=DeckListingOut,
    response_model_exclude_unset=True,
    responses=AUTH_RESPONSES,
)
def list_my_decks(
    request: Request,
    filters: DeckFiltersMine = Depends(),
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    paging: PaginationOptions = Depends(paging_options),
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Get a paginated listing of private decks for the current logged-in user.

    Please note that unlike the public-facing GET `/v2/decks` (which solely returns snapshots) this
    endpoint solely returns the base deck listings (no snapshots are included in the list at all).

    ## Available query parameter filters

    * `q`: deck title search
    * `phoenixborn`: list of Phoenixborn slugs
    * `card`: list of card slugs
    * `show_legacy` (default: false): if true, legacy 1.0 decks will be returned
    """
    query = get_decks_query(
        session,
        show_legacy=filters.show_legacy,
        is_public=False,
        order=order,
        q=filters.q,
        phoenixborn=filters.phoenixborn,
        cards=filters.card,
        players=[current_user.badge],
    )
    return paginate_deck_listing(query, session, request, paging)


@router.get(
    "/decks/{deck_id}",
    response_model=DeckDetails,
    response_model_exclude_unset=True,
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
        deck_dict = deck_to_dict(session, deck=source_deck, include_full_deck=True)
    # Private snapshots get returned if the user owns the deck
    elif source_deck.is_snapshot and own_deck:
        deck_dict = deck_to_dict(session, deck=source_deck, include_full_deck=True)
    # The actual deck gets returned if we are showing the latest saved copy
    elif not source_deck.is_snapshot and own_deck and show_saved:
        deck_dict = deck_to_dict(session, deck=source_deck, include_full_deck=True)
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
        deck_dict = deck_to_dict(session, deck=deck, include_full_deck=True)

    # Add our `is_saved` flag, if we're viewing a saved deck
    if not source_deck.is_snapshot and show_saved:
        deck_dict["is_saved"] = True

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
        deck_check: Deck = (
            session.query(Deck.user_id, Deck.is_legacy, Deck.is_snapshot)
            .filter(Deck.id == data.id)
            .first()
        )
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
            current_user,
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


@router.post(
    "/decks/{deck_id}/snapshot",
    response_model=DetailResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Snapshot creation failed.",
        },
        **AUTH_RESPONSES,
    },
)
def create_snapshot(
    deck_id: int,
    data: SnapshotIn = None,
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Create a snapshot of the currently-saved version of the deck.

    **Please note:** you must save the deck prior to calling this endpoint! This endpoint will create a snapshot from
    the most recent saved copy of the deck (although it does allow you to set a custom title and description).
    """
    deck: Deck = (
        session.query(Deck)
        .options(
            db.joinedload("cards"),
            db.joinedload("dice"),
            db.joinedload("selected_cards"),
        )
        .get(deck_id)
    )
    if not deck or deck.user_id != current_user.id:
        raise NoUserAccessException(
            detail="You cannot save a snapshot of a deck you do not own."
        )
    if deck.is_legacy:
        raise APIException(detail="You cannot save snapshots for legacy decks.")
    if deck.is_snapshot:
        raise APIException(detail="You cannot a snapshot of another snapshot.")
    if not data:
        data = SnapshotIn()
    preconstructed_release_id = None
    if data.preconstructed_release:
        if not current_user.is_admin:
            raise NoUserAccessException(
                detail="Only site admins may publish preconstructed decks."
            )
        preconstructed_release_id = (
            session.query(Release.id)
            .outerjoin(Deck, deck.preconstructed_release == Release.id)
            .filter(
                Release.stub == data.preconstructed_release,
                Release.is_legacy.is_(True),
                Release.is_public.is_(True),
                Deck.id.is_(None),
            )
            .scalar()
        )
        if not preconstructed_release_id:
            raise APIException(
                detail="No such release, or release already has a preconstructed deck."
            )
    title = data.title if data.title else deck.title
    description = deck.description
    if data.description:
        description = data.description
    elif data.description is not None:
        # Falsey descriptions that aren't None mean they intentionally want a blank description
        description = None
    entity_id = create_entity(session)
    snapshot = Deck(
        entity_id=entity_id,
        title=title,
        description=description,
        # In the interim while we are saving the cards and dice and so forth, we mark this as private so that it doesn't
        #  show up in any listings and break stuff in weird ways
        is_public=False,
        is_snapshot=True,
        is_preconstructed=bool(preconstructed_release_id),
        preconstructed_release=preconstructed_release_id,
        source_id=deck.id,
        user_id=current_user.id,
        phoenixborn_id=deck.phoenixborn_id,
    )
    # Save our snapshot so that we have an ID
    session.add(snapshot)
    session.commit()
    # Now duplicate the cards, dice, and selected cards for the given deck
    if deck.cards:
        for deck_card in deck.cards:
            session.add(
                DeckCard(
                    deck_id=snapshot.id,
                    card_id=deck_card.card_id,
                    count=deck_card.count,
                )
            )
    if deck.dice:
        for deck_die in deck.dice:
            session.add(
                DeckDie(
                    deck_id=snapshot.id,
                    die_flag=deck_die.die_flag,
                    count=deck_die.count,
                )
            )
    if deck.selected_cards:
        for deck_selected_card in deck.selected_cards:
            session.add(
                DeckSelectedCard(
                    deck_id=snapshot.id,
                    card_id=deck_selected_card.card_id,
                    tutor_card_id=deck_selected_card.tutor_card_id,
                    is_first_five=deck_selected_card.is_first_five,
                    is_paid_effect=deck_selected_card.is_paid_effect,
                )
            )
    # Flip our public flag now that we've populated the deck details, if necessary
    if data.is_public:
        snapshot.is_public = True
        # We also need to publish to the Stream for public snapshots
        refresh_stream_for_entity(
            session,
            entity_id=snapshot.entity_id,
            entity_type="deck",
            source_entity_id=deck.entity_id,
        )
        # And finally we need to update the user's subscription to mark the last_seen_entity_id
        update_subscription_for_user(
            session,
            user=current_user,
            source_entity_id=deck.entity_id,
            last_seen_entity_id=snapshot.entity_id,
        )
    session.commit()
    return {"detail": "Snapshot successfully created!"}

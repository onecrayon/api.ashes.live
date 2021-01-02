from fastapi import APIRouter, Depends, Request

from api import db
from api.depends import (
    paging_options,
    get_session,
    login_required,
    AUTH_RESPONSES,
)
from api.exceptions import NoUserAccessException, APIException, NotFoundException
from api.models import User, Deck, Card
from api.schemas import DetailResponse
from api.schemas.decks import DeckFilters, DeckListingOut, DeckOut, DeckIn
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.services.deck import create_or_update_deck, NoSuchDeck, PhoenixbornInDeck
from api.services.decks import get_decks_query, paginate_deck_listing, deck_to_dict

router = APIRouter()


@router.get(
    "/decks",
    response_model=DeckListingOut,
    response_model_exclude_unset=True,
)
def list_decks(
    request: Request,
    filters: DeckFilters = Depends(),
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    # Standard dependencies
    paging: PaginationOptions = Depends(paging_options),
    session: db.Session = Depends(get_session),
):
    """Get a paginated listing of decks with optional filters.

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
    return deck_to_dict(deck)

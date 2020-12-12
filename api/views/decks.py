from typing import Optional, List

from fastapi import APIRouter, Depends, Request

from api import db
from api.depends import paging_options, get_current_user, get_session
from api.models import User, Deck, Card, DeckCard, DeckDie
from api.schemas.decks import DeckFilters, DeckListingOut
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.utils.helpers import to_prefixed_tsquery
from api.utils.pagination import paginated_results_for_query

router = APIRouter()


def get_decks_query(
    session: db.Session,
    show_legacy=False,
    is_public=False,
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    # Filtering options
    q: Optional[str] = None,
    phoenixborn: Optional[List[str]] = None,
    cards: Optional[List[str]] = None,
    players: Optional[List[str]] = None,
) -> db.Query:
    query = session.query(Deck).filter(Deck.is_legacy.is_(show_legacy))
    if is_public:
        deck_comp = db.aliased(Deck)
        query = query.outerjoin(
            deck_comp,
            db.and_(
                Deck.source_id == deck_comp.source_id,
                deck_comp.is_snapshot.is_(True),
                deck_comp.is_public.is_(True),
                db.or_(
                    Deck.created < deck_comp.created,
                    db.and_(Deck.created == deck_comp.created, Deck.id < deck_comp.id),
                ),
            ),
        ).filter(
            deck_comp.id.is_(None), Deck.is_snapshot.is_(True), Deck.is_public.is_(True)
        )
    if q and q.strip():
        query = query.filter(
            db.func.to_tsvector("english", db.cast(Deck.title, db.Text)).match(
                to_prefixed_tsquery(q)
            )
        )
    # Filter by Phoenixborn stubs (this is always an OR comparison between Phoenixborn)
    if phoenixborn:
        query = query.join(Card, Card.id == Deck.phoenixborn_id).filter(
            Card.stub.in_(phoenixborn)
        )
    # Filter by cards (this is always an OR comparison between cards)
    if cards:
        card_table = db.aliased(Card)
        query = (
            query.join(DeckCard, DeckCard.deck_id == Deck.id)
            .join(card_table, card_table.id == DeckCard.card_id)
            .filter(card_table.stub.in_(cards))
        )
    # Filter by player badge, and always ensure that we eagerly load the user object
    if players:
        query = (
            query.join(User, User.id == Deck.user_id)
            .filter(User.badge.in_(players))
            .options(db.contains_eager(Deck.user))
        )
    else:
        query = query.options(db.joinedload(Deck.user))
    return query.order_by(getattr(Deck.created, order)())


@router.get(
    "/decks",
    response_model=DeckListingOut,
)
def list_decks(
    request: Request,
    filters: DeckFilters = Depends(),
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    # Standard dependencies
    paging: PaginationOptions = Depends(paging_options),
    current_user: "User" = Depends(get_current_user),
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
    # TODO: figure out how to gather up cards, conjurations, etc. and compile them in our output
    # .options(
    #     db.joinedload("phoenixborn").joinedload("conjurations"),
    #     db.joinedload("cards").joinedload("card").joinedload("conjurations"),
    #     db.joinedload("dice"),
    #     db.joinedload("user"),
    # )
    return paginated_results_for_query(query=query, paging=paging, url=str(request.url))

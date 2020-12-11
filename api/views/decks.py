from fastapi import APIRouter, Depends, Request

from api import db
from api.depends import paging_options, get_current_user, get_session
from api.models import User, Deck
from api.schemas.decks import DeckFilters, DeckListingOut
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.utils.pagination import paginated_results_for_query

router = APIRouter()


def get_decks_query(
    session: db.Session,
    show_legacy=False,
    is_public=False,
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
) -> db.Query:
    query = (
        session.query(Deck)
        .filter(Deck.is_legacy.is_(show_legacy))
        .options(
            db.joinedload("phoenixborn").joinedload("conjurations"),
            db.joinedload("cards").joinedload("card").joinedload("conjurations"),
            db.joinedload("dice"),
            db.joinedload("user"),
        )
    )
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
    return query.order_by(getattr(Deck.created, order)())


@router.get(
    "/decks",
    response_model=DeckListingOut,
)
def list_decks(
    request: Request,
    filters: DeckFilters = Depends(DeckFilters),
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    # Standard dependencies
    paging: PaginationOptions = Depends(paging_options),
    current_user: "User" = Depends(get_current_user),
    session: db.Session = Depends(get_session),
):
    """Get a paginated listing of decks with optional filters.

    ## Available filters

    * `q`: deck title search
    * `phoenixborn`: list of Phoenixborn slugs for possible deck Phoenixborn
    * `player`: list of player badges for possible deck authors
    * `show_legacy` (default: false): if true, legacy 1.0 decks will be returned
    """
    # TODO: implement support for all filters and pass them through
    query = get_decks_query(
        session, show_legacy=filters.show_legacy, is_public=True, order=order
    )
    return paginated_results_for_query(query=query, paging=paging, url=str(request.url))

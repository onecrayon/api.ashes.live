from fastapi import APIRouter, Depends, Request

from api import db
from api.depends import get_session, paging_options
from api.models import Comment
from api.schemas.comments import CommentsListingOut
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.utils.pagination import paginated_results_for_query

router = APIRouter()


@router.get(
    "/comments/{entity_id}",
    response_model=CommentsListingOut,
)
def get_comments(
    entity_id: int,
    request: Request,
    # Filtration query string options
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    # Standard dependencies
    paging: PaginationOptions = Depends(paging_options),
    session: db.Session = Depends(get_session),
):
    """Get a listing of comments for a given entity ID.

    By default, comments are ordered from oldest to newest by created date. You can pass the `order` query parameter
    to use a different sorting order.
    """
    query = (
        session.query(Comment)
        .options(db.joinedload("user"))
        .filter(Comment.source_entity_id == entity_id)
        .order_by(getattr(Comment.created, order)())
    )
    return paginated_results_for_query(
        query=query,
        paging=paging,
        url=str(request.url),
    )

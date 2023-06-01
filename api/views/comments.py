from fastapi import APIRouter, Depends, Request, status

from api import db
from api.depends import (
    AUTH_RESPONSES,
    get_session,
    login_required,
    paging_options,
)
from api.exceptions import APIException, NotFoundException
from api.models import Card, Comment, Deck, UserType
from api.schemas import DetailResponse
from api.schemas.comments import CommentIn, CommentOut, CommentsListingOut
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.services.stream import create_entity
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


@router.post(
    "/comments/{entity_id}",
    response_model=DetailResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Comment creation failed.",
        },
        404: {
            "model": DetailResponse,
            "description": "Entity ID is not associated with an entity that can be commented on.",
        },
        **AUTH_RESPONSES,
    },
)
def create_comment(
    entity_id: int,
    data: CommentIn,
    # Standard dependencies
    current_user: "UserType" = Depends(login_required),
    session: db.Session = Depends(get_session),
):
    """Post a comment to a resource on the site."""
    # First, figure out what our entity ID is pointing to
    source = session.query(Card).filter(Card.entity_id == entity_id).first()
    source_type = "card"
    if not source:
        source = session.query(Deck).filter(Deck.entity_id == entity_id).first()
        source_type = "deck"
    if source is None:
        raise NotFoundException(detail="No valid resource found to comment on.")
    if source.is_legacy:
        raise APIException(
            detail="Commenting on legacy decks and cards is not allowed."
        )
    try:
        if source.is_snapshot:
            raise APIException(detail="You cannot comment on snapshots.")
    except AttributeError:
        # Cards don't have this attribute, so we can safely ignore it
        pass
    # Now gather a few parameters, and create our comment
    try:
        source_version = source.version
    except AttributeError:
        # Decks don't have this attribute, so we can ignore it
        source_version = None
    previous_ordering_increment = (
        session.query(Comment.ordering_increment)
        .filter(Comment.source_entity_id == entity_id)
        .order_by(Comment.created.desc())
        .limit(1)
        .scalar()
    )
    if not previous_ordering_increment:
        previous_ordering_increment = 0
    comment = Comment(
        entity_id=create_entity(),
        user_id=current_user.id,
        source_entity_id=source.entity_id,
        source_type=source_type,
        source_version=source_version,
        text=data.text,
        ordering_increment=previous_ordering_increment + 1,
    )
    session.add(comment)
    session.commit()
    return {"detail": "Comment successfully posted!"}

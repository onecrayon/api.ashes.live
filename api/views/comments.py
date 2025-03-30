from fastapi import APIRouter, Depends, Request, Response, status

from api import db
from api.depends import (
    AUTH_RESPONSES,
    get_current_user,
    get_session,
    login_required,
    paging_options,
)
from api.exceptions import APIException, NotFoundException, NoUserAccessException
from api.models import Card, Comment, Deck, User, UserType
from api.schemas import DetailResponse
from api.schemas.comments import (
    CommentDeleteIn,
    CommentEditIn,
    CommentIn,
    CommentOut,
    CommentsListingOut,
)
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.services.stream import (
    create_entity,
    refresh_stream_for_entity,
    update_subscription_for_user,
)
from api.utils.pagination import paginated_results_for_query

router = APIRouter()


def comment_out(comment: "Comment", current_user: "UserType") -> "CommentOut":
    """Utility method for ensuring that we don't pass text for deleted comments unless an admin queries them."""
    output = CommentOut.model_validate(comment)
    if not comment.is_deleted or (
        not current_user.is_anonymous() and current_user.is_admin
    ):
        return output
    output.text = None
    return output


@router.get(
    "/comments/{entity_id}",
    response_model=CommentsListingOut,
)
def get_comments(
    entity_id: int,
    request: Request,
    # Filtration query string options
    order: PaginationOrderOptions = PaginationOrderOptions.asc,
    # Standard dependencies
    paging: PaginationOptions = Depends(paging_options),
    current_user: "UserType" = Depends(get_current_user),
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
    page_results = paginated_results_for_query(
        query=query,
        paging=paging,
        url=str(request.url),
    )
    # We need to do a little post-processing to ensure we don't leak the text of deleted comments
    page_results["results"] = [
        comment_out(x, current_user) for x in page_results["results"]
    ]
    return page_results


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
    current_user: "User" = Depends(login_required),
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
    if not data.text.strip():
        raise APIException(detail="You cannot post blank comments.")
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
    # Create our comment and update the stream and the existing user subscription
    comment = Comment(
        entity_id=create_entity(session),
        user_id=current_user.id,
        source_entity_id=source.entity_id,
        source_type=source_type,
        source_version=source_version,
        text=data.text,
        ordering_increment=previous_ordering_increment + 1,
    )
    session.add(comment)
    refresh_stream_for_entity(
        session,
        entity_id=comment.entity_id,
        entity_type="comment",
        source_entity_id=source.entity_id,
    )
    update_subscription_for_user(
        session,
        user=current_user,
        source_entity_id=source.entity_id,
        last_seen_entity_id=comment.entity_id,
    )
    session.commit()
    return {"detail": "Comment successfully posted!"}


@router.patch(
    "/comment/{comment_entity_id}",
    response_model=CommentOut,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Comment creation failed.",
        },
        404: {
            "model": DetailResponse,
            "description": "No such comment.",
        },
        **AUTH_RESPONSES,
    },
)
def edit_comment(
    comment_entity_id: int,
    data: CommentEditIn,
    # Standard dependencies
    current_user: "User" = Depends(login_required),
    session: db.Session = Depends(get_session),
):
    """Edit an existing comment.

    **Admin-only:** the `moderation_notes` field is required when modifying another user's comment; should contain a
    short description of the reason the comment is being moderated.
    """
    comment = (
        session.query(Comment).filter(Comment.entity_id == comment_entity_id).first()
    )
    if not comment:
        raise NotFoundException(detail="No such comment found.")
    if comment.is_deleted:
        raise APIException(detail="You cannot edit deleted comments.")
    if not data.text.strip():
        raise APIException(detail="You cannot post blank comments.")
    if current_user.id != comment.user_id:
        if not current_user.is_admin:
            raise NoUserAccessException(detail="You may only edit your own comments.")
        elif not data.moderation_notes:
            raise APIException(
                detail="You must include moderation notes when editing other users' comments."
            )
        comment.original_text = comment.text
        comment.moderation_notes = data.moderation_notes
        comment.is_moderated = True
    elif comment.is_moderated and not current_user.is_admin:
        raise APIException(
            detail="This comment has been moderated and cannot be modified."
        )
    comment.text = data.text
    # There's no reason to update the stream when editing comments, so skip that call
    session.commit()
    return comment


@router.delete(
    "/comment/{comment_entity_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Comment creation failed.",
        },
        404: {
            "model": DetailResponse,
            "description": "No such comment.",
        },
        **AUTH_RESPONSES,
    },
)
def delete_comment(
    comment_entity_id: int,
    moderation_notes: str = None,
    # Standard dependencies
    current_user: "User" = Depends(login_required),
    session: db.Session = Depends(get_session),
):
    """Delete a comment.

    **Admin-only:** the `moderation_notes` field is required when modifying another user's comment; should contain a
    short description of the reason the comment is being moderated.
    """
    comment = (
        session.query(Comment).filter(Comment.entity_id == comment_entity_id).first()
    )
    if not comment:
        raise NotFoundException(detail="No such comment found.")
    success_response = Response(status_code=status.HTTP_204_NO_CONTENT)
    if comment.is_deleted:
        return success_response
    if current_user.id != comment.user_id:
        if not current_user.is_admin:
            raise NoUserAccessException(detail="You may only delete your own comments.")
        elif not moderation_notes:
            raise APIException(
                detail="You must include moderation notes when deleting other users' comments."
            )
        comment.moderation_notes = moderation_notes
        comment.is_moderated = True
    comment.is_deleted = True
    session.commit()
    return success_response

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .pagination import PaginatedResultsBase
from .user import UserBasicOut


class CommentOut(BaseModel):
    """A comment on a card or deck."""

    entity_id: int = Field(
        ...,
        description=(
            "The entity ID for this particular comment. Entity IDs are used by subscriptions to track what a user has "
            "previously viewed (assuming that they only view comments in ascending order)."
        ),
    )
    source_entity_id: int = Field(
        ..., description="The entity ID for the resource this comment is commenting on."
    )
    source_version: int | None = Field(
        None,
        description=(
            "Only shown for cards; can be used to highlight comments that apply to previous versions of the card."
        ),
    )
    text: str | None = None
    ordering_increment: int = Field(
        ...,
        description=(
            "This is an auto-incrementing value that counts the number of comments attached to the source_entity_id in "
            "order of ascending created date. This is useful if a front-end wishes to jump from a stream listing or "
            "similar to the specific page that holds a given comment (because if you know the total number of comments "
            "per page and the comment ordering_increment, you can calculate what page it lies on)."
        ),
    )
    created: datetime
    modified: datetime
    is_moderated: bool

    user: UserBasicOut
    model_config = ConfigDict(from_attributes=True)


class CommentsListingOut(PaginatedResultsBase):
    """Ordered listing of comments for a resource on the site."""

    results: list[CommentOut] = []


class CommentIn(BaseModel):
    """Necessary fields for creating or updating a comment."""

    text: str


class CommentEditIn(CommentIn):
    """Fields for editing a comment."""

    moderation_notes: str = Field(
        None,
        description=(
            "The reason this comment is being edited. Can only be set by site admins, and required when editing "
            "another user's comment."
        ),
    )


class CommentDeleteIn(BaseModel):
    """Fields for deleting a comment."""

    moderation_notes: str = Field(
        None,
        description=(
            "The reason this comment is being deleted. Can only be set by site admins, and required when deleting "
            "another user's comment."
        ),
    )

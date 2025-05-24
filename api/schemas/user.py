from typing import Self

from pydantic import UUID4, BaseModel, ConfigDict, EmailStr, Field, model_validator


class UserEmailIn(BaseModel):
    """Email to which an invite should be sent"""

    email: EmailStr


class UserSetPasswordIn(BaseModel):
    """Set the password for a given user"""

    password: str = Field(..., min_length=8, max_length=50)
    password_confirm: str = Field(..., min_length=8, max_length=50)

    @model_validator(mode="after")
    def passwords_match(self) -> Self:
        if self.password != self.password_confirm:
            raise ValueError("Passwords do not match.")
        return self


class UserSelfPasswordIn(UserSetPasswordIn):
    """Update password while logged in"""

    current_password: str = Field(..., min_length=8, max_length=50)


class UserRegistrationIn(UserSetPasswordIn):
    """Registration details for a given user"""

    username: str | None = Field(
        ...,
        description="How you wish to be known around the site.",
        min_length=2,
        max_length=42,
    )
    description: str | None = Field(
        None, description="Supports card codes and star formatting."
    )
    newsletter_opt_in: bool = False


class UserBasicOut(BaseModel):
    """Basic public user information"""

    username: str
    badge: str
    model_config = ConfigDict(from_attributes=True)


class UserPublicOut(UserBasicOut):
    """Public user information"""

    description: str | None = None


class UserSelfOut(UserPublicOut):
    """Private user information"""

    email: str
    reset_uuid: UUID4 | None = None
    newsletter_opt_in: bool
    email_subscriptions: bool
    exclude_subscriptions: bool
    colorize_icons: bool
    is_admin: bool


class UserSelfIn(BaseModel):
    """Patch private user information"""

    username: str = Field(
        None,
        description="How you wish to be known around the site.",
        min_length=2,
        max_length=42,
    )
    description: str = Field(
        None, description="Supports card codes and star formatting."
    )
    newsletter_opt_in: bool = False
    email_subscriptions: bool = False
    exclude_subscriptions: bool = False
    colorize_icons: bool = False


class UserModerationIn(BaseModel):
    """Moderate a user"""

    username: str | None = None
    description: str | None = None
    is_banned: bool | None = False
    moderation_notes: str = Field(
        ...,
        description="Required notes about what and why moderation actions were taken. May be exposed to the moderated user.",
    )


class UserModerationOut(BaseModel):
    """Response after moderating a user"""

    username: str
    description: str | None = None
    is_banned: bool
    moderation_notes: str
    model_config = ConfigDict(from_attributes=True)


class UserExportToken(BaseModel):
    """Export token used for moving decks from one instance to another."""

    export_token: UUID4

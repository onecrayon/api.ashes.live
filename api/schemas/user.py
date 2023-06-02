from pydantic import UUID4, BaseModel, EmailStr, Field, validator


class UserEmailIn(BaseModel):
    """Email to which an invite should be sent"""

    email: EmailStr


class UserSetPasswordIn(BaseModel):
    """Set the password for a given user"""

    password: str = Field(..., min_length=8, max_length=50)
    password_confirm: str = Field(..., min_length=8, max_length=50)

    @validator("password_confirm")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("Passwords do not match.")
        return v


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

    class Config:
        orm_mode = True


class UserPublicOut(UserBasicOut):
    """Public user information"""

    description: str | None


class UserSelfOut(UserPublicOut):
    """Private user information"""

    email: str
    reset_uuid: UUID4 | None
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

    username: str = None
    description: str = None
    is_banned: bool = False
    moderation_notes: str = Field(
        ...,
        description="Required notes about what and why moderation actions were taken. May be exposed to the moderated user.",
    )


class UserModerationOut(BaseModel):
    """Response after moderating a user"""

    username: str
    description: str | None
    is_banned: bool
    moderation_notes: str

    class Config:
        orm_mode = True

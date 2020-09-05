from typing import Optional

from pydantic import BaseModel, Field


class UserPublicOut(BaseModel):
    """Public user information"""

    username: str
    badge: str
    description: Optional[str]

    class Config:
        orm_mode = True


class UserSelfOut(UserPublicOut):
    """Private user information"""

    email: str
    reset_uuid: Optional[str]
    newsletter_opt_in: bool
    email_subscriptions: bool
    exclude_subscriptions: bool
    colorize_icons: bool


class UserSelfIn(BaseModel):
    """Patch private user information"""

    username: str = Field(
        None, description="How you wish to be known around the site.", max_length=42
    )
    description: Optional[str] = Field(
        None, description="Supports card codes and star formatting."
    )
    newsletter_opt_in: bool = False
    email_subscriptions: bool = False
    exclude_subscriptions: bool = False
    colorize_icons: bool = False

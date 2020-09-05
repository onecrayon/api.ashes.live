from typing import Optional

from pydantic import BaseModel


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

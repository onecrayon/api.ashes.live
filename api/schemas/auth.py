from pydantic import BaseModel

from .user import UserSelfOut


class AuthTokenOut(BaseModel):
    """Output response to return JWT authentication tokens"""

    access_token: str
    token_type: str
    user: UserSelfOut

from pydantic import BaseModel


class AuthTokenOut(BaseModel):
    """Output response to return JWT authentication tokens"""

    access_token: str
    token_type: str

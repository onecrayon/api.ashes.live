import uuid
from typing import Optional, Union

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from jose import jwt, JWTError

from .db import Session, SessionLocal
from .environment import settings
from .exceptions import CredentialsException, BannedUserException
from .models import AnonymousUser, User, UserRevokedToken
from .schemas import DetailResponse
from .schemas.pagination import PaginationOptions

# Setup common global dependencies
def get_session():  # pragma: no cover
    """Primary database dependency"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v2/token", auto_error=False)


AUTH_RESPONSES = {
    401: {"model": DetailResponse, "description": "Invalid credentials."},
    403: {
        "model": DetailResponse,
        "description": "User has been banned or otherwise lacks permission to access this resource.",
    },
}


def get_auth_token(token: Optional[str] = Depends(oauth2_scheme)) -> Optional[dict]:
    """Returns the parsed JWT payload data, or raises a CredentialsException"""
    if token is None:
        return None
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        return payload
    except JWTError:
        raise CredentialsException()


def get_current_user(
    payload: Optional[dict] = Depends(get_auth_token),
    session: Session = Depends(get_session),
) -> Union["AnonymousUser", "User"]:
    """Returns authenticated user or AnonymousUser instance"""
    if payload is None:
        return AnonymousUser()
    user_badge: str = payload.get("sub")
    # JWT ID is a UUID encoded as a hex string
    jwt_hex: str = payload.get("jti")
    if user_badge is None or jwt_hex is None:
        raise CredentialsException()
    jwt_id = uuid.UUID(hex=jwt_hex)
    current_user = session.query(User).filter(User.badge == user_badge).first()
    revoked_session = (
        session.query(UserRevokedToken)
        .filter(UserRevokedToken.revoked_uuid == jwt_id)
        .first()
    )
    if revoked_session or current_user is None:
        raise CredentialsException()
    if current_user.is_banned:
        raise BannedUserException()
    return current_user


def anonymous_required(
    current_user: "AnonymousUser" = Depends(get_current_user),
) -> "AnonymousUser":
    """Throws an error if endpoint is accessed by logged-in user"""
    if not current_user.is_anonymous():
        raise CredentialsException(
            detail="You are already logged in as a registered user."
        )
    return current_user


def login_required(current_user: "AnonymousUser" = Depends(get_current_user)) -> "User":
    """Returns authenticated user"""
    if current_user.is_anonymous():
        raise CredentialsException()
    return current_user


def admin_required(current_user: "User" = Depends(login_required)) -> "User":
    """Returns authenticated admin user"""
    if not current_user.is_admin:
        raise CredentialsException()
    return current_user


def paging_options(
    limit: int = settings.pagination_default_limit, offset: int = 0
) -> PaginationOptions:
    """Standard pagination options"""
    return PaginationOptions(limit=limit, offset=offset)

from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, FastAPI, HTTPException, status
from jose import jwt, JWTError

from .db import Session, SessionLocal
from .environment import settings
from .exceptions import CredentialsException, BannedUserException
from .models import AnonymousUser, User
from .schemas import DetailResponse

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
    403: {"model": DetailResponse, "description": "User has been banned."},
}


def get_current_user(
    token: Optional[str] = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
) -> "AnonymousUser":
    """Returns authenticated user or AnonymousUser instance"""
    if token is None:
        return AnonymousUser()
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        user_badge: str = payload.get("sub")
        if user_badge is None:
            raise CredentialsException()
    except JWTError:
        raise CredentialsException()
    current_user = session.query(User).filter(User.badge == user_badge).first()
    if current_user is None:
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

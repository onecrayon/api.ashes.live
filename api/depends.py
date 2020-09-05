from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, FastAPI, HTTPException, status
from jose import JWTError

from .db import Session, SessionLocal
from .environment import settings
from .models import AnonymousUser, User

# Setup common global dependencies
def get_session():  # pragma: no cover
    """Primary database dependency"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid credentials. Please log in again.",
    headers={"WWW-Authenticate": "Bearer"},
)


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
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    current_user = session.query(User).filter(User.badge == user_badge).first()
    if current_user is None:
        raise credentials_exception
    return current_user


def login_required(current_user: "AnonymousUser" = Depends(get_current_user)) -> "User":
    """Returns authenticated user"""
    if current_user.is_anonymous():
        raise credentials_exception
    return user


def admin_required(current_user: "User" = Depends(login_required)) -> "User":
    """Returns authenticated admin user"""
    if not current_user.is_admin:
        raise credentials_exception
    return current_user

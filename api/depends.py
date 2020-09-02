from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, FastAPI, HTTPException, status
from jose import JWTError

from .db import Session, SessionLocal
from .environment import settings

# Setup common global dependencies
def get_session():  # pragma: no cover
    """Primary database dependency"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(
    token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)
):
    """Primary authenticated user dependency"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials. Please log in again.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        user_badge: str = payload.get("sub")
        if user_badge is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = session.query(User).filter(User.badge == user_badge).first()
    if user is None:
        raise credentials_exception
    return user

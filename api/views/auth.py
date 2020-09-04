from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from api import db
from api.depends import get_session
from api.environment import settings
from api.models import User
from api.schemas import auth as schema
from api.utils.auth import verify_password, create_access_token


router = APIRouter()


@router.post("/token", tags=["auth"], response_model=schema.AuthTokenOut)
def log_in(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: db.Session = Depends(get_session),
):
    """Log a user in and return a JWT authentication token to authenticate future requests.

    **Please note:** Only username and password are currently in use, and `username` must be the
    user's registered email. You can ignore the other form fields.
    """
    user = session.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expiry)
    access_token = create_access_token(
        data={"sub": user.badge},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}

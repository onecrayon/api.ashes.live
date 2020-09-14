from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from api import db
from api.depends import AUTH_RESPONSES, get_session
from api.environment import settings
from api.exceptions import CredentialsException, BannedUserException
from api.models import User
from api.services.user import access_token_for_user
from api.schemas import auth as schema
from api.utils.auth import verify_password


router = APIRouter()


@router.post(
    "/token",
    response_model=schema.AuthTokenOut,
    responses=AUTH_RESPONSES,
)
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
        raise CredentialsException(
            detail="Incorrect username or password",
        )
    if user.is_banned:
        raise BannedUserException()
    access_token = access_token_for_user(user)
    return {"access_token": access_token, "token_type": "bearer"}

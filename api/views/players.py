from fastapi import APIRouter, Depends, HTTPException, status

from api import db
from api.depends import get_session, login_required, AUTH_RESPONSES
from api.exceptions import NotFoundException
from api.models import User
from api.schemas import GenericError, user as schema


router = APIRouter()


@router.get(
    "/players/me",
    response_model=schema.UserSelfOut,
    responses=AUTH_RESPONSES,
)
def get_my_data(current_user: "User" = Depends(login_required)):
    """Return user information for logged-in user."""
    return current_user


@router.get(
    "/players/{badge}",
    response_model=schema.UserPublicOut,
    responses={404: {"model": GenericError}},
)
def get_user_data(badge: str, session: db.Session = Depends(get_session)):
    """Return public user information for any user."""
    user = (
        session.query(User)
        .filter(User.badge == badge, User.is_banned.is_(False))
        .first()
    )
    if not user:
        raise NotFoundException(detail="User not found.")
    return user

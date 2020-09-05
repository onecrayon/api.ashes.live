from fastapi import APIRouter, Depends, HTTPException, status

from api import db
from api.depends import get_session, login_required
from api.models import User
from api.schemas import GenericError, user as schema


router = APIRouter()


@router.get(
    "/players/me",
    response_model=schema.UserSelfOut,
    responses={401: {"model": GenericError}},
)
def get_me(current_user: "User" = Depends(login_required)):
    """Return user information for self"""
    return current_user

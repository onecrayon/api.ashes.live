from fastapi import APIRouter, Depends, HTTPException, status

from api import db
from api.depends import get_session, login_required, AUTH_RESPONSES
from api.models import User
from api.schemas import user as schema


router = APIRouter()


@router.get(
    "/players/me",
    response_model=schema.UserSelfOut,
    responses=AUTH_RESPONSES,
)
def get_me(current_user: "User" = Depends(login_required)):
    """Return user information for self"""
    return current_user

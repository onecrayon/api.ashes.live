import logging

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import UUID4

from api import db
from api.depends import (
    get_session,
    admin_required,
    anonymous_required,
    login_required,
    AUTH_RESPONSES,
)
from api.environment import settings
from api.exceptions import APIException, NotFoundException
from api.models import Invite, User
from api.schemas import DetailResponse, user as schema
from api.schemas.auth import AuthTokenOut
from api.services.user import access_token_for_user, get_invite_for_email, create_user
from api.utils.email import send_message


router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/players/new",
    status_code=status.HTTP_201_CREATED,
    response_model=DetailResponse,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Unable to send email. See detail for reason.",
        }
    },
)
def request_invite(
    data: schema.UserEmailIn,
    session: db.Session = Depends(get_session),
    _=Depends(anonymous_required),
):
    """Request an invite be sent to the given email.

    Will fail if requested by an authenticated user.
    """
    email = data.email.lower()
    user = session.query(User).filter(User.email == email).first()
    if user:
        raise APIException(
            detail="This email is already in use.",
        )
    invitation = get_invite_for_email(session, email)
    # Email the user
    if not send_message(
        recipient=invitation.email,
        template_id=settings.sendgrid_invite_template,
        data={
            "invite_token": str(invitation.uuid),
            "email": invitation.email,
        },
    ):
        if settings.debug:
            logger.debug(f"INVITE TOKEN FOR {email}: {invitation.uuid}")
        raise APIException(
            detail="Unable to send invitation email; please contact the site owner."
        )
    return {
        "detail": "Your invitation has been sent! Please follow the link in your email to set your password."
    }


@router.post(
    "/players/new/{token}",
    status_code=status.HTTP_201_CREATED,
    response_model=AuthTokenOut,
    responses={404: {"model": DetailResponse, "description": "Bad invitation token"}},
)
def create_player(
    token: UUID4,
    data: schema.UserRegistrationIn,
    session: db.Session = Depends(get_session),
    _=Depends(anonymous_required),
):
    """Create a new player using the token obtained by requesting an invite.

    Will fail if requested by an authenticated user.
    """
    invite = session.query(Invite).filter(Invite.uuid == token).first()
    if invite is None:
        raise NotFoundException(detail="Token not found. Please request a new invite.")
    user = create_user(
        session,
        invite.email,
        data.password,
        username=data.username,
        description=data.description,
        newsletter_opt_in=data.newsletter_opt_in,
    )
    session.delete(invite)
    session.commit()
    access_token = access_token_for_user(user)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get(
    "/players/me",
    response_model=schema.UserSelfOut,
    responses=AUTH_RESPONSES,
)
def get_my_data(current_user: "User" = Depends(login_required)):
    """Return user information for logged-in user."""
    return current_user


@router.patch(
    "/players/me", response_model=schema.UserSelfOut, responses=AUTH_RESPONSES
)
def update_my_data(
    updates: schema.UserSelfIn,
    current_user: "User" = Depends(login_required),
    session: db.Session = Depends(get_session),
):
    """Update user information for the logged-in user."""
    update_dict = updates.dict(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(current_user, key, value)
    session.commit()
    return current_user


@router.get(
    "/players/{badge}",
    response_model=schema.UserPublicOut,
    responses={404: {"model": DetailResponse}},
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


@router.patch(
    "/players/{badge}",
    response_model=schema.UserModerationOut,
    responses={
        400: {"model": DetailResponse},
        404: {"model": DetailResponse},
        **AUTH_RESPONSES,
    },
)
def moderate_user(
    badge: str,
    updates: schema.UserModerationIn,
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(admin_required),
):
    """**Admin only.** Ban a user; or moderate their username or description."""
    user: User = session.query(User).filter(User.badge == badge).first()
    if not user:
        raise NotFoundException(detail="User not found.")
    if user.id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You cannot moderate yourself.",
        )
    update_dict = updates.dict(exclude_unset=True)
    if "is_banned" in update_dict:
        user.is_banned = update_dict["is_banned"]
        user.moderation_notes = update_dict["moderation_notes"]
    else:
        for key, value in update_dict.items():
            setattr(user, key, value)
    session.commit()
    return user

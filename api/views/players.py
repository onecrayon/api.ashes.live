import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.exceptions import RequestValidationError
from pydantic import UUID4

from api import db
from api.depends import (
    AUTH_RESPONSES,
    admin_required,
    anonymous_required,
    get_session,
    login_required,
)
from api.environment import settings
from api.exceptions import APIException, NotFoundException
from api.models import Invite, User
from api.schemas import DetailResponse
from api.schemas import user as schema
from api.schemas.auth import AuthTokenOut
from api.schemas.user import UserExportToken
from api.services.user import access_token_for_user, create_user, get_invite_for_email
from api.utils.auth import generate_password_hash, verify_password
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
        template_name="invite",
        subject=f"Create your {settings.site_name} account!",
        data={
            "invite_token": str(invitation.uuid),
            "email": invitation.email,
        },
    ):
        if settings.debug:
            logger.debug(f"INVITE TOKEN FOR {email}: {invitation.uuid}")
        raise APIException(
            detail="Unable to send invitation email; please report this to Skaak#0007 on Discord!"
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
    return {"access_token": access_token, "token_type": "bearer", "user": user}


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
    update_dict = updates.model_dump(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(current_user, key, value)
    session.commit()
    return current_user


@router.post(
    "/players/me/password", response_model=DetailResponse, responses=AUTH_RESPONSES
)
def update_my_password(
    updates: schema.UserSelfPasswordIn,
    current_user: "User" = Depends(login_required),
    session: db.Session = Depends(get_session),
):
    """Update logged-in user's password"""
    if not verify_password(updates.current_password, current_user.password):
        # We need to fake a normal validation error, because we can't really do this in the schema
        #  (need access to the database session for the password verification)
        raise RequestValidationError(
            errors=(ValueError("Current password is invalid."),)
        )
    current_user.password = generate_password_hash(updates.password)
    session.commit()
    return {"detail": "Your password has been updated!"}


@router.get(
    "/players/me/export",
    response_model=UserExportToken,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Deck exports are disallowed for this site.",
        },
        **AUTH_RESPONSES,
    },
)
def get_deck_export_token(
    current_user: "User" = Depends(login_required),
    session: db.Session = Depends(get_session),
):
    """Generates (if necessary) and returns the UUID that allows the current user to export their decks to other
    instances. Mainly intended for migrating decks into the official Plaid Hat AshesDB.
    """
    if not settings.allow_exports:
        raise APIException(detail="Deck exports are disallowed for this site.")
    if current_user.deck_export_uuid is None:
        current_user.deck_export_uuid = uuid.uuid4()
        session.commit()
    return {"export_token": current_user.deck_export_uuid}


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
    update_dict = updates.model_dump(exclude_unset=True)
    if "is_banned" in update_dict:
        user.is_banned = update_dict["is_banned"]
        user.moderation_notes = update_dict["moderation_notes"]
    else:
        for key, value in update_dict.items():
            setattr(user, key, value)
    session.commit()
    return user

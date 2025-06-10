import datetime as dt
import logging
import uuid

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import UUID4

from api import db
from api.depends import (
    AUTH_RESPONSES,
    anonymous_required,
    get_auth_token,
    get_session,
    login_required,
)
from api.environment import settings
from api.exceptions import (
    APIException,
    BannedUserException,
    CredentialsException,
    NotFoundException,
)
from api.models import User, UserRevokedToken
from api.schemas import DetailResponse
from api.schemas import auth as schema
from api.schemas.user import UserEmailIn, UserSetPasswordIn
from api.services.user import access_token_for_user
from api.utils.auth import generate_password_hash, verify_password
from api.utils.dates import utcnow
from api.utils.email import send_message

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/token",
    response_model=schema.AuthTokenOut,
    responses=AUTH_RESPONSES,
)
def log_in(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: db.Session = Depends(get_session),
    _=Depends(anonymous_required),
):
    """Log a user in and return a JWT authentication token to authenticate future requests.

    **Please note:** Only username and password are currently in use, and `username` must be the
    user's registered email.

    If you pass in `token:longterm` in the scopes, then you will be issued a long-lived token
    (defaults to one year before expiring).
    """
    email = form_data.username.lower()
    user = session.query(User).filter(User.email == email).first()
    if not user or not verify_password(form_data.password, user.password):
        raise CredentialsException(
            detail="Incorrect username or password",
        )
    if user.is_banned:
        raise BannedUserException()
    is_long_term = False
    for scope in form_data.scopes:
        if scope.lower() == "token:longterm":
            is_long_term = True
            break
    access_token = access_token_for_user(user, is_long_term=is_long_term)
    return {"access_token": access_token, "token_type": "bearer", "user": user}


@router.delete("/token", response_model=DetailResponse, responses=AUTH_RESPONSES)
def log_out(
    session: db.Session = Depends(get_session),
    jwt_payload: dict = Depends(get_auth_token),
    current_user: "User" = Depends(login_required),
):
    """Log a user out and revoke their JWT token's access rights.

    It's a good idea to invoke this whenever an authenticated user logs out, because tokens can otherwise be quite
    long-lived.
    """
    # Do some quick clean-up to keep our table lean and mean; deletes any tokens that expired more than 24 hours ago
    session.query(UserRevokedToken).filter(
        UserRevokedToken.expires < utcnow() - dt.timedelta(days=1)
    ).delete(synchronize_session=False)
    session.commit()
    # Then add our newly revoked token
    expires_at = dt.datetime.fromtimestamp(jwt_payload["exp"], tz=dt.timezone.utc)
    # No need to do `.get("jti")` here because a missing JTI would result in a credentials error in the dependencies
    revoked_hex = jwt_payload["jti"]
    revoked_uuid = uuid.UUID(hex=revoked_hex)
    revoked_token = UserRevokedToken(
        revoked_uuid=revoked_uuid, user_id=current_user.id, expires=expires_at
    )
    session.add(revoked_token)
    session.commit()
    return {"detail": "Token successfully revoked."}


@router.post(
    "/reset",
    response_model=DetailResponse,
    responses={
        404: {"model": DetailResponse, "description": "Email has not been registered."},
        **AUTH_RESPONSES,
    },
)
def request_password_reset(
    data: UserEmailIn,
    session: db.Session = Depends(get_session),
    _=Depends(anonymous_required),
):
    """Request a reset password link for the given email."""
    email = data.email.lower()
    user: User = session.query(User).filter(User.email == email).first()
    if not user:
        raise NotFoundException(detail="No account found for email.")
    if user.is_banned:
        raise BannedUserException()
    user.reset_uuid = uuid.uuid4()
    session.commit()
    if not send_message(
        recipient=user.email,
        template_name="reset_password",
        subject=f"Reset your {settings.site_name} password",
        data={"reset_token": str(user.reset_uuid), "email": user.email},
    ):
        if settings.debug:
            logger.debug(f"RESET TOKEN FOR {email}: {user.reset_uuid}")
        raise APIException(
            detail="Unable to send password reset email; please contact Skaak#0007 on Discord."
        )
    return {"detail": "A link to reset your password has been sent to your email!"}


@router.post(
    "/reset/{token}",
    response_model=schema.AuthTokenOut,
    responses={
        404: {"model": DetailResponse, "description": "Bad invitation token"},
        **AUTH_RESPONSES,
    },
)
def reset_password(
    token: UUID4,
    data: UserSetPasswordIn,
    session: db.Session = Depends(get_session),
    _=Depends(anonymous_required),
):
    """Reset the password for account associated with the given reset token."""
    user = session.query(User).filter(User.reset_uuid == token).first()
    if user is None:
        raise NotFoundException(
            detail="Token not found. Please request a new password reset."
        )
    user.password = generate_password_hash(data.password)
    user.reset_uuid = None
    session.commit()
    access_token = access_token_for_user(user)
    return {"access_token": access_token, "token_type": "bearer", "user": user}

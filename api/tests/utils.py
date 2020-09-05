from datetime import timedelta
import random
import string
from typing import Tuple

from api import db, models
from api.services.user import create_user
from api.utils.auth import create_access_token


def _create_user_password(session: db.Session) -> Tuple[models.User, str]:
    """Returns a new user, and their plaintext password"""
    email = f"{generate_random_chars(4)}@{generate_random_chars(6)}.fake"
    password = generate_random_chars(16)
    user = create_user(session, email=email, password=password)
    return user, password


def _create_user_token(session: db.Session) -> Tuple[models.User, str]:
    """Returns a new user, and their associated bearer token"""
    user, _ = _create_user_password(session)
    token = create_access_token(
        data={"sub": user.badge}, expires_delta=timedelta(minutes=15)
    )
    return user, token


def generate_random_chars(length=10) -> str:
    """Returns a random alphanumeric string of the given length"""
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))

import uuid
from datetime import timedelta

import bcrypt
from jose import jwt

from api.environment import settings
from api.utils.dates import utcnow


def generate_password_hash(password: str) -> str:
    """Generates the hash for a given plain text password"""
    return bcrypt.hashpw(
        bytes(password, encoding="utf-8"),
        bcrypt.gensalt(),
    ).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain text password against a saved hash"""
    return bcrypt.checkpw(
        bytes(plain_password, encoding="utf-8"),
        bytes(hashed_password, encoding="utf-8"),
    )


def create_access_token(data: dict, expires_delta: timedelta) -> str:
    """Returns a valid token wrapping the passed data plus the expiry (in minutes)"""
    to_encode = data.copy()
    expire = utcnow() + expires_delta
    to_encode.update(
        {
            "jti": uuid.uuid4().hex,
            "iat": utcnow(),
            "exp": expire,
        }
    )
    encoded_jwt = jwt.encode(to_encode, settings.secret_key)
    return encoded_jwt

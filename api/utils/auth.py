import uuid
from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from api.environment import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_password_hash(password: str) -> str:
    """Generates the hash for a given plain text password"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain text password against a saved hash"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta) -> str:
    """Returns a valid token wrapping the passed data plus the expiry (in minutes)"""
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update(
        {
            "jti": uuid.uuid4().hex,
            "iat": datetime.utcnow(),
            "exp": expire,
        }
    )
    encoded_jwt = jwt.encode(to_encode, settings.secret_key)
    return encoded_jwt

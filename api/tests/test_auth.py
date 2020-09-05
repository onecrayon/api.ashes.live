from datetime import datetime, timedelta
import random
import string
from typing import Tuple

from fastapi import status
from fastapi.testclient import TestClient
from freezegun import freeze_time
from jose import jwt

from api import db
from api.environment import settings
from .utils import _create_user_password, generate_random_chars, _create_user_token


def test_bad_username(client: TestClient, session: db.Session):
    """Logging in with invalid username must generate an error"""
    user, password = _create_user_password(session)
    bad_email = f"nope_{user.email}"
    response = client.post("/v2/token", {"username": bad_email, "password": password})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_bad_password(client: TestClient, session: db.Session):
    """Logging in with invalid password must generate an error"""
    user, password = _create_user_password(session)
    bad_password = generate_random_chars(len(password) + 2)
    response = client.post(
        "/v2/token", {"username": user.email, "password": bad_password}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_banned_user(client: TestClient, session: db.Session):
    """Login requests by banned users throw an error"""
    user, password = _create_user_password(session)
    user.is_banned = True
    session.commit()
    response = client.post("/v2/token", {"username": user.email, "password": password})
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.json()


def test_token(client: TestClient, session: db.Session):
    """Logging in with valid credentials must generate a JWT token"""
    # Create a user in the database with a random password
    user, password = _create_user_password(session)
    # Verify that we can log in with the random password
    response = client.post("/v2/token", {"username": user.email, "password": password})
    assert response.status_code == status.HTTP_200_OK, response.json()


def test_login_required(client: TestClient, session: db.Session):
    """login_required dependency works with a valid token"""
    user, token = _create_user_token(session)
    response = client.get(
        "/v2/players/me", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK, response.json()


def test_login_required_no_token(client: TestClient, session: db.Session):
    """login_required does in fact require a login"""
    response = client.get("/v2/players/me")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_login_required_old_token(client: TestClient, session: db.Session):
    """login_required dependency requires a current token"""
    user, token = _create_user_token(session)
    tomorrow = datetime.utcnow() + timedelta(days=1)
    with freeze_time(tomorrow):
        response = client.get(
            "/v2/players/me", headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_login_required_missing_sub(client: TestClient, session: db.Session):
    """login_required dependency requires the user badge in the `sub`"""
    expire = datetime.utcnow() + timedelta(minutes=15)
    fake_data = {"exp": expire}
    fake_token = jwt.encode(fake_data, settings.secret_key)
    response = client.get(
        "/v2/players/me", headers={"Authorization": f"Bearer {fake_token}"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_login_required_no_such_badge(client: TestClient, session: db.Session):
    """login_required dependency can handled badges that don't exist"""
    expire = datetime.utcnow() + timedelta(minutes=15)
    fake_data = {"exp": expire, "sub": "nopers"}
    fake_token = jwt.encode(fake_data, settings.secret_key)
    response = client.get(
        "/v2/players/me", headers={"Authorization": f"Bearer {fake_token}"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, resonse.json()


def test_login_required_banned_user(client: TestClient, session: db.Session):
    """login_required dependency does not allow banned users"""
    user, token = _create_user_token(session)
    user.is_banned = True
    session.commit()
    response = client.get(
        "/v2/players/me", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.json()

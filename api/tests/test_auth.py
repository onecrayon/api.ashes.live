import random
import string
from typing import Tuple

from fastapi import status
from fastapi.testclient import TestClient

from api import db
from .utils import _create_user_password, generate_random_chars


def test_bad_username(client: TestClient, session: db.Session):
    """Logging in with invalid username must generate an error"""
    user, password = _create_user_password(session)
    bad_email = f"nope_{user.email}"
    response = client.post("/token", {"username": bad_email, "password": password})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_bad_password(client: TestClient, session: db.Session):
    """Logging in with invalid password must generate an error"""
    user, password = _create_user_password(session)
    bad_password = generate_random_chars(len(password) + 2)
    response = client.post("/token", {"username": user.email, "password": bad_password})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_login(client: TestClient, session: db.Session):
    """Logging in with valid credentials must generate a JWT token"""
    # Create a user in the database with a random password
    user, password = _create_user_password(session)
    # Verify that we can log in with the random password
    response = client.post("/token", {"username": user.email, "password": password})
    assert response.status_code == status.HTTP_200_OK

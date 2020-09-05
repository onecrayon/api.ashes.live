from fastapi import status
from fastapi.testclient import TestClient

from api import db
from .utils import _create_user_token, generate_random_chars

# `/v2/players/me` is tested by the default auth dependency checks in `test_auth.py`


def test_get_user(client: TestClient, session: db.Session):
    """Get user must return for valid badges"""
    user, _ = _create_user_token(session)
    response = client.get(f"/v2/players/{user.badge}")
    assert response.status_code == status.HTTP_200_OK, response.json()


def test_get_banned_user(client: TestClient, session: db.Session):
    """Get user returns 404 for banned users"""
    user, _ = _create_user_token(session)
    user.is_banned = True
    session.commit()
    response = client.get(f"/v2/players/{user.badge}")
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.json()


def test_get_user_bad_badge(client: TestClient, session: db.Session):
    """Get user with a non-existent badge returns 404"""
    user, _ = _create_user_token(session)
    bad_badge = f"a{user.badge}"
    response = client.get(f"/v2/players/{bad_badge}")
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.json()

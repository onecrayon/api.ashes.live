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


def test_patch_user(client: TestClient, session: db.Session):
    """Patching user must only update the fields that were passed in"""
    user, token = _create_user_token(session)
    user.description = generate_random_chars(8)
    original_username = user.username
    session.commit()
    new_description = generate_random_chars(4)
    response = client.patch(
        "/v2/players/me",
        json={"description": new_description},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK, response.json()
    session.refresh(user)
    assert user.username == original_username
    assert user.description == new_description


def test_patch_user_validation_error(client: TestClient, session: db.Session):
    """Patching user with overlong username throws a validation error"""
    user, token = _create_user_token(session)
    response = client.patch(
        "/v2/players/me",
        json={"username": "a" * 45},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()

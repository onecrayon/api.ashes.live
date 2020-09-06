from fastapi import status
from fastapi.testclient import TestClient

from api import db
from . import utils

# `/v2/players/me` is tested by the default auth dependency checks in `test_auth.py`


def test_get_user(client: TestClient, session: db.Session):
    """Get user must return for valid badges"""
    user, _ = utils.create_user_token(session)
    response = client.get(f"/v2/players/{user.badge}")
    assert response.status_code == status.HTTP_200_OK, response.json()


def test_get_banned_user(client: TestClient, session: db.Session):
    """Get user returns 404 for banned users"""
    user, _ = utils.create_user_token(session)
    user.is_banned = True
    session.commit()
    response = client.get(f"/v2/players/{user.badge}")
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.json()


def test_get_user_bad_badge(client: TestClient, session: db.Session):
    """Get user with a non-existent badge returns 404"""
    user, _ = utils.create_user_token(session)
    bad_badge = f"a{user.badge}"
    response = client.get(f"/v2/players/{bad_badge}")
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.json()


def test_patch_user(client: TestClient, session: db.Session):
    """Patching user must only update the fields that were passed in"""
    user, token = utils.create_user_token(session)
    user.description = utils.generate_random_chars(8)
    original_username = user.username
    session.commit()
    new_description = utils.generate_random_chars(4)
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
    user, token = utils.create_user_token(session)
    response = client.patch(
        "/v2/players/me",
        json={"username": "a" * 45},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()


# Basic access to `/v2/players/{badge}` moderation endpoint is handled by test_auth.py
def test_moderate_user_self(client: TestClient, session: db.Session):
    """Users cannot moderat themselves"""
    admin, token = utils.create_admin_token(session)
    response = client.patch(
        f"/v2/players/{admin.badge}",
        headers={"Authorization": f"Bearer {token}"},
        json={"username": "newname", "moderation_notes": "Bad name."},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.json()


def test_moderate_user_nonexistent(client: TestClient, session: db.Session):
    """Cannot moderate non-existent users"""
    admin, token = utils.create_admin_token(session)
    user, _ = utils.create_user_token(session)
    response = client.patch(
        f"/v2/players/a{user.badge}",
        headers={"Authorization": f"Bearer {token}"},
        json={"username": "newname", "moderation_notes": "Bad name."},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.json()


def test_ban_user(client: TestClient, session: db.Session):
    """Admins can ban users"""
    admin, token = utils.create_admin_token(session)
    user, _ = utils.create_user_token(session)
    response = client.patch(
        f"/v2/players/{user.badge}",
        headers={"Authorization": f"Bearer {token}"},
        json={"is_banned": True, "moderation_notes": "Bad user."},
    )
    assert response.status_code == status.HTTP_200_OK, response.json()
    session.refresh(user)
    assert user.is_banned == True

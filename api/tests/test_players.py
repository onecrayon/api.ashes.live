import uuid

from fastapi import status
from fastapi.testclient import TestClient

import api.views.players
from api import db
from api.models import Invite, User
from api.services.user import get_invite_for_email
from api.utils.auth import verify_password

from . import utils

# Basic `/v2/players/new` behavior is tested by the default auth dependency checks in `test_auth.py`


def test_invite_requests_incremented(
    client: TestClient, session: db.Session, monkeypatch
):
    """Requesting an invite multiple times must increment the requests counter"""

    def _always_true(*args, **kwargs):
        return True

    # Just patch the whole send_email method; its behavior is tested elsewhere
    monkeypatch.setattr(api.views.players, "send_message", _always_true)
    fake_email = utils.generate_random_email()
    response = client.post("/v2/players/new", json={"email": fake_email})
    assert response.status_code == status.HTTP_201_CREATED, response.json()
    assert (
        session.query(Invite.requests).filter(Invite.email == fake_email).scalar() == 1
    )
    # Request a second time
    response = client.post("/v2/players/new", json={"email": fake_email})
    assert response.status_code == status.HTTP_201_CREATED, response.json()
    assert (
        session.query(Invite.requests).filter(Invite.email == fake_email).scalar() == 2
    )


def test_invite_existing_user(client: TestClient, session: db.Session):
    """Requesting an invite for a registered emails throws an error"""
    user, _ = utils.create_user_token(session)
    response = client.post("/v2/players/new", json={"email": user.email})
    assert response.status_code == status.HTTP_400_BAD_REQUEST, respone.json()
    assert session.query(Invite).filter(Invite.email == user.email).count() == 0


def test_invite_smtp_failure(client: TestClient, session: db.Session, monkeypatch):
    """Endpoint throws an error if SMTP fails"""

    def _always_false(*args, **kwargs):
        return False

    # Just patch the whole send_email method; its behavior is tested elsewhere
    monkeypatch.setattr(api.views.players, "send_message", _always_false)
    fake_email = utils.generate_random_email()
    response = client.post("/v2/players/new", json={"email": fake_email})
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.json()
    # Email failed, but the invite should still be created
    assert session.query(Invite).filter(Invite.email == fake_email).count() == 1


def test_register_user_different_passwords(client: TestClient, session: db.Session):
    """Throw a validation error when passwords do not match"""
    email = utils.generate_random_email()
    invite = get_invite_for_email(session, email)
    password = utils.generate_random_chars(10)
    password_confirm = utils.generate_random_chars(11)
    response = client.post(
        f"/v2/players/new/{invite.uuid}",
        json={"password": password, "password_confirm": password_confirm},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()
    assert session.query(User).count() == 0


def test_register_user_invalid_token(client: TestClient, session: db.Session):
    """No user created with an invalid token is passed"""
    bad_token = uuid.uuid4()
    password = utils.generate_random_chars(10)
    response = client.post(
        f"/v2/players/new/{bad_token}",
        json={"username": "test", "password": password, "password_confirm": password},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.json()
    assert session.query(User).count() == 0


def test_register_user(client: TestClient, session: db.Session):
    """User is created and invite destroyed upon registration"""
    email = utils.generate_random_email()
    invite = get_invite_for_email(session, email)
    password = utils.generate_random_chars(10)
    response = client.post(
        f"/v2/players/new/{invite.uuid}",
        json={"username": "test", "password": password, "password_confirm": password},
    )
    assert response.status_code == status.HTTP_201_CREATED, response.json()
    assert session.query(Invite).filter(Invite.email == email).count() == 0
    assert session.query(User).filter(User.email == email).count() == 1


# `/v2/players/me` is tested by the default auth dependency checks in `test_auth.py`


def test_user_post_password_mismatch_passwords(client: TestClient, session: db.Session):
    """Cannot update own password if new passwords do not match"""
    user, current_password = utils.create_user_password(session)
    user, token = utils.create_user_token(session, user=user)
    password = utils.generate_random_chars(8)
    password2 = f"a{password}"
    response = client.post(
        "/v2/players/me/password",
        json={
            "current_password": current_password,
            "password": password,
            "password_confirm": password2,
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_user_post_password_wrong_password(client: TestClient, session: db.Session):
    """Cannot update own password if current password is wrong"""
    user, current_password = utils.create_user_password(session)
    user, token = utils.create_user_token(session, user=user)
    password = utils.generate_random_chars(8)
    response = client.post(
        "/v2/players/me/password",
        json={
            "current_password": f"a{current_password}",
            "password": password,
            "password_confirm": password,
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_user_post_password(client: TestClient, session: db.Session):
    """Can update own password"""
    user, current_password = utils.create_user_password(session)
    user, token = utils.create_user_token(session, user=user)
    password = utils.generate_random_chars(8)
    response = client.post(
        "/v2/players/me/password",
        json={
            "current_password": current_password,
            "password": password,
            "password_confirm": password,
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    session.refresh(user)
    assert verify_password(password, user.password) is True


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


# Export Token Tests


def test_get_export_token_generates_new_uuid(
    client: TestClient, session: db.Session, monkeypatch
):
    """Test that a new export token UUID is generated for users who don't have one"""
    # Enable exports for this test
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Create user without export token
    user, token = utils.create_user_token(session)
    assert user.deck_export_uuid is None

    # Request export token
    response = client.get(
        "/v2/players/me/export", headers={"Authorization": f"Bearer {token}"}
    )

    data = response.json()
    assert response.status_code == status.HTTP_200_OK, data
    assert "export_token" in data
    assert data["export_token"] is not None

    # Verify token was saved to database
    session.refresh(user)
    assert user.deck_export_uuid is not None
    assert str(user.deck_export_uuid) == data["export_token"]


def test_get_export_token_returns_existing_uuid(
    client: TestClient, session: db.Session, monkeypatch
):
    """Test that existing export token UUID is returned without generating a new one"""
    # Enable exports for this test
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Create user with existing export token
    user, token = utils.create_user_token(session)
    existing_uuid = uuid.uuid4()
    user.deck_export_uuid = existing_uuid
    session.commit()

    # Request export token
    response = client.get(
        "/v2/players/me/export", headers={"Authorization": f"Bearer {token}"}
    )

    data = response.json()
    assert response.status_code == status.HTTP_200_OK, data
    assert data["export_token"] == str(existing_uuid)

    # Verify UUID wasn't changed in database
    session.refresh(user)
    assert user.deck_export_uuid == existing_uuid


def test_get_export_token_fails_when_exports_disabled(
    client: TestClient, session: db.Session, monkeypatch
):
    """Test that export token generation fails when ALLOW_EXPORTS=false"""
    # Ensure exports are disabled
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": False})

    user, token = utils.create_user_token(session)

    response = client.get(
        "/v2/players/me/export", headers={"Authorization": f"Bearer {token}"}
    )

    data = response.json()
    assert response.status_code == status.HTTP_400_BAD_REQUEST, data
    assert "export" in data["detail"].lower()

    # Verify no token was created
    session.refresh(user)
    assert user.deck_export_uuid is None


def test_get_export_token_requires_authentication(client: TestClient):
    """Test that export token endpoint requires user authentication"""
    response = client.get("/v2/players/me/export")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()

import uuid
from datetime import timedelta

from fastapi import status
from fastapi.testclient import TestClient
from freezegun import freeze_time
from jose import jwt

import api.views.players
from api import db
from api.environment import settings
from api.models import Invite, UserRevokedToken
from api.utils.dates import utcnow

from . import utils


def test_bad_username(client: TestClient, session: db.Session):
    """Logging in with invalid username must generate an error"""
    user, password = utils.create_user_password(session)
    bad_email = f"nope_{user.email}"
    response = client.post(
        "/v2/token", data={"username": bad_email, "password": password}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_bad_password(client: TestClient, session: db.Session):
    """Logging in with invalid password must generate an error"""
    user, password = utils.create_user_password(session)
    bad_password = utils.generate_random_chars(len(password) + 2)
    response = client.post(
        "/v2/token", data={"username": user.email, "password": bad_password}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_banned_user(client: TestClient, session: db.Session):
    """Login requests by banned users throw an error"""
    user, password = utils.create_user_password(session)
    user.is_banned = True
    session.commit()
    response = client.post(
        "/v2/token", data={"username": user.email, "password": password}
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.json()


def test_token(client: TestClient, session: db.Session):
    """Logging in with valid credentials must generate a JWT token"""
    # Create a user in the database with a random password
    user, password = utils.create_user_password(session)
    # Verify that we can log in with the random password
    response = client.post(
        "/v2/token", data={"username": user.email, "password": password}
    )
    assert response.status_code == status.HTTP_200_OK, response.json()


def test_longterm_token(client: TestClient, session: db.Session):
    """Requesting a long-term token must return a long-term token"""
    # Create a user
    user, password = utils.create_user_password(session)
    # Verify we can obtain a long-term token
    response = client.post(
        "/v2/token",
        data={"username": user.email, "password": password, "scope": "token:longterm"},
    )
    assert response.status_code == status.HTTP_200_OK, response.json()
    # Verify that the token is actually long-term
    with freeze_time(utcnow() + timedelta(days=60)):
        response = client.get(
            "/v2/players/me",
            headers={"Authorization": f"Bearer {response.json()['access_token']}"},
        )
        assert response.status_code == status.HTTP_200_OK, response.json()


def test_anonymous_required(client: TestClient, session: db.Session, monkeypatch):
    """Anonymous users can access endpoints that require anonymity"""

    def _always_true(*args, **kwargs):
        return True

    # Just patch the whole send_email method; its behavior is tested elsewhere
    monkeypatch.setattr(api.views.players, "send_message", _always_true)
    fake_email = utils.generate_random_email()
    response = client.post("/v2/players/new", json={"email": fake_email})
    assert response.status_code == status.HTTP_201_CREATED, response.json()
    assert session.query(Invite).filter(Invite.email == fake_email).count() == 1


def test_anonymous_required_authenticated_user(client: TestClient, session: db.Session):
    """Authenticated users cannot access endpoints that require anonymity"""
    _, token = utils.create_user_token(session)
    fake_email = utils.generate_random_email()
    response = client.post(
        "/v2/players/new",
        json={"email": fake_email},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()
    assert session.query(Invite).filter(Invite.email == fake_email).count() == 0


def test_login_required(client: TestClient, session: db.Session):
    """login_required dependency works with a valid token"""
    user, token = utils.create_user_token(session)
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
    user, token = utils.create_user_token(session)
    tomorrow = utcnow() + timedelta(days=1)
    with freeze_time(tomorrow):
        response = client.get(
            "/v2/players/me", headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_login_required_missing_sub(client: TestClient, session: db.Session):
    """login_required dependency requires the user badge in the `sub`"""
    expire = utcnow() + timedelta(minutes=15)
    fake_data = {"jti": uuid.uuid4().hex, "exp": expire}
    fake_token = jwt.encode(fake_data, settings.secret_key)
    response = client.get(
        "/v2/players/me", headers={"Authorization": f"Bearer {fake_token}"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_login_required_missing_jti(client: TestClient, session: db.Session):
    """login_required dependency requires a JWT ID in the `jti`"""
    user, _ = utils.create_user_token(session)
    expire = utcnow() + timedelta(minutes=15)
    fake_data = {"sub": user.badge, "exp": expire}
    fake_token = jwt.encode(fake_data, settings.secret_key)
    response = client.get(
        "/v2/players/me", headers={"Authorization": f"Bearer {fake_token}"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_login_required_no_such_badge(client: TestClient, session: db.Session):
    """login_required dependency can handled badges that don't exist"""
    expire = utcnow() + timedelta(minutes=15)
    fake_data = {"exp": expire, "sub": "nopers", "jti": uuid.uuid4().hex}
    fake_token = jwt.encode(fake_data, settings.secret_key)
    response = client.get(
        "/v2/players/me", headers={"Authorization": f"Bearer {fake_token}"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_login_required_banned_user(client: TestClient, session: db.Session):
    """login_required dependency does not allow banned users"""
    user, token = utils.create_user_token(session)
    user.is_banned = True
    session.commit()
    response = client.get(
        "/v2/players/me", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.json()


def test_admin_required(client: TestClient, session: db.Session):
    """Admins can access admin_required dependency paths"""
    admin, token = utils.create_admin_token(session)
    user, _ = utils.create_user_token(session)
    response = client.patch(
        f"/v2/players/{user.badge}",
        headers={"Authorization": f"Bearer {token}"},
        json={"username": "newname", "moderation_notes": "Bad name."},
    )
    assert response.status_code == status.HTTP_200_OK, response.json()


def test_admin_required_normal_user(client: TestClient, session: db.Session):
    """Non-admins cannot access admin_required dependency paths"""
    user1, token = utils.create_user_token(session)
    user2, _ = utils.create_user_token(session)
    user2.username = "oldname"
    session.commit()
    response = client.patch(
        f"/v2/players/{user2.badge}",
        headers={"Authorization": f"Bearer {token}"},
        json={"username": "newname", "moderation_notes": "Bad name."},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.json()
    session.refresh(user2)
    assert user2.username == "oldname"


def test_request_password_reset_banned_user(client: TestClient, session: db.Session):
    """Banned users cannot request password resets"""
    user, _ = utils.create_user_token(session)
    user.is_banned = True
    session.commit()
    response = client.post("/v2/reset", json={"email": user.email})
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_request_password_reset_bad_email(client: TestClient, session: db.Session):
    """Nonexistent emails cannot obtain password resets"""
    email = utils.generate_random_email()
    response = client.post("/v2/reset", json={"email": email})
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_request_password_reset_local_debugging(
    client: TestClient, session: db.Session, monkeypatch
):
    """Reset UUIDs are properly generated for password reset requests when debugging locally"""

    def _always_false(*args, **kwargs):
        return False

    # send_email is covered by unit tests, so it's safe to patch the whole function
    monkeypatch.setattr(api.views.auth, "send_message", _always_false)
    utils.monkeypatch_settings(monkeypatch, {"debug": True})
    user, _ = utils.create_user_token(session)
    assert user.reset_uuid is None
    response = client.post("/v2/reset", json={"email": user.email})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    session.refresh(user)
    assert user.reset_uuid is not None


def test_request_password_reset(client: TestClient, session: db.Session, monkeypatch):
    """Password reset works properly when emailing the request"""

    def _always_true(*args, **kwargs):
        return True

    # send_email is covered by unit tests, so it's safe to patch the whole function
    monkeypatch.setattr(api.views.auth, "send_message", _always_true)
    user, _ = utils.create_user_token(session)
    assert user.reset_uuid is None
    response = client.post("/v2/reset", json={"email": user.email})
    assert response.status_code == status.HTTP_200_OK
    session.refresh(user)
    assert user.reset_uuid is not None


def test_request_password_reset_twice(
    client: TestClient, session: db.Session, monkeypatch
):
    """Password reset token is regenerated when requesting a second time"""

    def _always_true(*args, **kwargs):
        return True

    # send_email is covered by unit tests, so it's safe to patch the whole function
    monkeypatch.setattr(api.views.auth, "send_message", _always_true)
    user, _ = utils.create_user_token(session)
    assert user.reset_uuid is None
    response = client.post("/v2/reset", json={"email": user.email})
    assert response.status_code == status.HTTP_200_OK
    session.refresh(user)
    assert user.reset_uuid is not None
    original_token = user.reset_uuid
    # Send a second reset request
    response = client.post("/v2/reset", json={"email": user.email})
    assert response.status_code == status.HTTP_200_OK
    session.refresh(user)
    assert original_token != user.reset_uuid


def test_reset_password_bad_token(client: TestClient, session: db.Session):
    """Cannot change password with a bad token"""
    bad_token = uuid.uuid4()
    password = utils.generate_random_chars(8)
    response = client.post(
        f"/v2/reset/{bad_token}",
        json={"password": password, "password_confirm": password},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_reset_password_bad_passwords(client: TestClient, session: db.Session):
    """Password must match confirmation value"""
    user, _ = utils.create_user_token(session)
    user.reset_uuid = uuid.uuid4()
    session.commit()
    password = utils.generate_random_chars(8)
    password2 = f"a{password}"
    response = client.post(
        f"/v2/reset/{user.reset_uuid}",
        json={"password": password, "password_confirm": password2},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_reset_password(client: TestClient, session: db.Session):
    """Password reset must reset the password"""
    user, _ = utils.create_user_token(session)
    user.reset_uuid = uuid.uuid4()
    session.commit()
    new_password = utils.generate_random_chars(8)
    original_hash = user.password
    response = client.post(
        f"/v2/reset/{user.reset_uuid}",
        json={"password": new_password, "password_confirm": new_password},
    )
    assert response.status_code == status.HTTP_200_OK
    session.refresh(user)
    assert original_hash != user.password


def test_reset_password_then_login(
    client: TestClient, session: db.Session, monkeypatch
):
    """Users must be able to log in after requesting a password reset"""

    def _always_true(*args, **kwargs):
        return True

    # send_email is covered by unit tests, so it's safe to patch the whole function
    monkeypatch.setattr(api.views.auth, "send_message", _always_true)
    user, password = utils.create_user_password(session)
    response = client.post("/v2/reset", json={"email": user.email})
    assert response.status_code == status.HTTP_200_OK
    session.refresh(user)
    assert user.reset_uuid is not None
    # And then verify that we can login
    response = client.post(
        "/v2/token", data={"username": user.email, "password": password}
    )
    assert response.status_code == status.HTTP_200_OK


def test_revoke_token(client: TestClient, session: db.Session):
    """Revoking the token must disallow access to the API with that token"""
    # Create a token, then revoke it
    user, token = utils.create_user_token(session)
    response = client.delete("/v2/token", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    # Verify that we added the token to the "revert token" table
    payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
    jwt_uuid = uuid.UUID(hex=payload["jti"])
    assert (
        session.query(UserRevokedToken)
        .filter(UserRevokedToken.revoked_uuid == jwt_uuid)
        .count()
        == 1
    )
    # Verify that we cannot make further authenticated requests with this token
    response = client.get(
        "/v2/players/me", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_revoke_token_cleanup(client: TestClient, session: db.Session):
    """Revoking a token must clean up old revoked tokens"""

    def revoke_token(time):
        with freeze_time(time):
            user, token = utils.create_user_token(session)
            response = client.delete(
                "/v2/token", headers={"Authorization": f"Bearer {token}"}
            )
            assert response.status_code == status.HTTP_200_OK, response.json()

    now = utcnow()
    # Revoke a token 2 days ago
    one_day = now - timedelta(days=2)
    revoke_token(one_day)
    assert session.query(UserRevokedToken).count() == 1
    # Revoke a token now, so that the first token should get purged
    revoke_token(now)
    assert session.query(UserRevokedToken).count() == 1

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.services.deck import create_snapshot_for_deck
from api.tests.decks.deck_utils import create_deck_for_user
from api.tests.utils import create_user_token


@pytest.fixture(scope="module", autouse=True)
def user_token(decks_session):
    user, token = create_user_token(decks_session)
    return user, token


@pytest.fixture(scope="module", autouse=True)
def user2_token(decks_session):
    user, token = create_user_token(decks_session)
    return user, token


@pytest.fixture(scope="module")
def deck(decks_session, user_token):
    user, _ = user_token
    return create_deck_for_user(decks_session, user)


@pytest.fixture(scope="module", autouse=True)
def public_snapshot(decks_session, user_token, deck):
    user, _ = user_token
    return create_snapshot_for_deck(
        decks_session,
        user,
        deck,
        title="Public Snapshot",
        description="Public description",
        is_public=True,
    )


@pytest.fixture(scope="module", autouse=True)
def deck2(decks_session, user_token):
    user, _ = user_token
    return create_deck_for_user(decks_session, user)


@pytest.fixture(scope="module", autouse=True)
def snapshot(decks_session, user_token, deck2):
    user, _ = user_token
    return create_snapshot_for_deck(
        decks_session,
        user,
        deck2,
        title="Private Snapshot",
        description="Private description",
        is_public=False,
    )


def test_toggle_red_rains_others_deck(
    client: TestClient, session: db.Session, deck, user2_token
):
    """Red Rains status for a deck cannot be toggled by other users"""
    _, token = user2_token
    response = client.post(
        f"/v2/decks/{deck.id}/toggle-red-rains",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_toggle_red_rains_others_snapshot(
    client: TestClient, session: db.Session, snapshot, user2_token
):
    """Red Rains status for a deck cannot be toggled by other users"""
    _, token = user2_token
    response = client.post(
        f"/v2/decks/{snapshot.id}/toggle-red-rains",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_toggle_red_rains_others_public_snapshot(
    client: TestClient, session: db.Session, public_snapshot, user2_token
):
    """Red Rains status for a deck cannot be toggled by other users"""
    _, token = user2_token
    response = client.post(
        f"/v2/decks/{public_snapshot.id}/toggle-red-rains",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_toggle_red_rains_legacy_deck(
    client: TestClient, session: db.Session, deck, user_token
):
    """Cannot toggle Red Rains on a legacy deck"""
    deck.is_legacy = True
    session.commit()
    _, token = user_token
    response = client.post(
        f"/v2/decks/{deck.id}/toggle-red-rains",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_toggle_red_rains_public_snapshot(
    client: TestClient, session: db.Session, public_snapshot, user_token
):
    """Cannot toggle Red Rains on a public snapshot"""
    _, token = user_token
    response = client.post(
        f"/v2/decks/{public_snapshot.id}/toggle-red-rains",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_toggle_red_rains_deleted_deck(
    client: TestClient, session: db.Session, deck, user_token
):
    """Cannot toggle Red Rains on a deleted deck"""
    deck.is_deleted = True
    session.commit()
    _, token = user_token
    response = client.post(
        f"/v2/decks/{deck.id}/toggle-red-rains",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_toggle_red_rains_deck_with_public_snapshot(
    client: TestClient, session: db.Session, deck, user_token
):
    """Cannot toggle Red Rains on a legacy deck"""
    _, token = user_token
    response = client.post(
        f"/v2/decks/{deck.id}/toggle-red-rains",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_toggle_red_rains(client: TestClient, session: db.Session, deck2, user_token):
    """Toggling red rains mode works"""
    assert deck2.is_red_rains is False
    _, token = user_token
    response = client.post(
        f"/v2/decks/{deck2.id}/toggle-red-rains",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    session.refresh(deck2)
    assert deck2.is_red_rains is True

import urllib.parse

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.services.deck import create_snapshot_for_deck

from ..utils import create_user_token
from .deck_utils import create_deck_for_user


@pytest.fixture(scope="module", autouse=True)
def user1(cards_session):
    user1, _ = create_user_token(cards_session)
    return user1


@pytest.fixture(scope="module", autouse=True)
def deck1(cards_session, user1):
    return create_deck_for_user(cards_session, user1, release_stub="master-set")


@pytest.fixture(scope="module", autouse=True)
def snapshot1(cards_session, user1, deck1):
    return create_snapshot_for_deck(
        cards_session,
        user1,
        deck1,
        title="User1 Snapshot",
        is_public=True,
    )


@pytest.fixture(scope="module", autouse=True)
def private_deck1(cards_session, user1):
    return create_deck_for_user(cards_session, user1, release_stub="expansion")


@pytest.fixture(scope="module", autouse=True)
def user2(cards_session):
    user2, _ = create_user_token(cards_session)
    return user2


@pytest.fixture(scope="module", autouse=True)
def deck2(cards_session, user2):
    return create_deck_for_user(cards_session, user2, release_stub="expansion")


@pytest.fixture(scope="module", autouse=True)
def snapshot2(cards_session, user2, deck2):
    return create_snapshot_for_deck(
        cards_session,
        user2,
        deck2,
        title="User2 Snapshot",
        is_public=True,
    )


def test_get_decks(client: TestClient, session: db.Session, snapshot1, snapshot2):
    """Basic deck filtration must work properly"""
    # Public deck listings return all public decks, but no private decks
    response = client.get("/v2/decks")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 2
    # Decks are in reverse chronological order, hence the index order being backward
    assert data["results"][1]["id"] == snapshot1.id
    assert data["results"][0]["id"] == snapshot2.id


def test_get_decks_legacy_decks(
    client: TestClient, session: db.Session, user1, snapshot1, snapshot2
):
    """Legacy decks must be shown when requested, and not otherwise"""
    # We can't create legacy decks, so for the purposes of this test we'll fake it
    legacy_deck = create_deck_for_user(session, user1)
    legacy_snapshot = create_snapshot_for_deck(
        session, user1, legacy_deck, title="Legacy Deck", is_public=True
    )
    legacy_deck.is_legacy = True
    legacy_snapshot.is_legacy = True
    session.commit()
    response = client.get("/v2/decks")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 2
    assert data["results"][1]["id"] == snapshot1.id
    assert data["results"][0]["id"] == snapshot2.id
    response = client.get("/v2/decks?show_legacy=true")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["id"] == legacy_snapshot.id


def test_get_decks_deleted_snapshots(
    client: TestClient, session: db.Session, snapshot1, user1, deck1
):
    """Deleted snapshots must be excluded from the listing"""
    snapshot1_2 = create_snapshot_for_deck(session, user1, deck1, is_public=True)
    # Verify our new snapshot is the first item in the listing
    response = client.get("/v2/decks")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["results"][0]["id"] == snapshot1_2.id
    # Delete our snapshot, and verify it is gone
    snapshot1_2.is_deleted = True
    session.commit()
    response = client.get("/v2/decks")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["results"][0]["id"] != snapshot1_2.id


def test_get_decks_filter_preconstructed(
    client: TestClient, session: db.Session, user1
):
    """Filtering by preconstructed decks must work"""
    # Create a preconstructed deck
    precon_deck = create_deck_for_user(session, user1, release_stub="master-set")
    precon_snapshot = create_snapshot_for_deck(
        session, user1, precon_deck, is_public=True
    )
    precon_snapshot.is_preconstructed = True
    session.commit()
    response = client.get("/v2/decks?show_preconstructed=true")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["id"] == precon_snapshot.id


def test_get_decks_filter_title(client: TestClient, session: db.Session, snapshot1):
    """Filtering by snapshot title must work"""
    response = client.get(f"/v2/decks?q={snapshot1.title}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["id"] == snapshot1.id


def test_get_decks_filter_phoenixborn(
    client: TestClient, session: db.Session, snapshot1
):
    """Filtering by snapshot Phoenixborn must work"""
    response = client.get("/v2/decks?phoenixborn=one-phoenixborn")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["id"] == snapshot1.id


def test_get_decks_filter_card(client: TestClient, session: db.Session, snapshot2):
    """Filtering by included card must work"""
    response = client.get("/v2/decks?card=two-ready-spell")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["id"] == snapshot2.id


def test_get_decks_filter_user(
    client: TestClient, session: db.Session, user1, snapshot1
):
    """Filtering by user badge must work"""
    # Public deck listings offer filtration by user
    response = client.get(f"/v2/decks?player={urllib.parse.quote(user1.badge)}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["id"] == snapshot1.id

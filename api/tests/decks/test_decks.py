import urllib.parse
from datetime import timedelta

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.services.deck import create_snapshot_for_deck
from api.utils.auth import create_access_token

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
        title="First Snapshot",
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
        title="Second Snapshot",
        is_public=True,
    )


def test_get_decks(client: TestClient, snapshot1, snapshot2):
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


def test_get_decks_filter_title(client: TestClient, session, snapshot1):
    """Filtering by snapshot title must work"""
    response = client.get(f"/v2/decks?q={urllib.parse.quote(snapshot1.title)}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1, data
    assert data["results"][0]["id"] == snapshot1.id, data


def test_get_decks_filter_phoenixborn(client: TestClient, snapshot1):
    """Filtering by snapshot Phoenixborn must work"""
    response = client.get("/v2/decks?phoenixborn=one-phoenixborn")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["id"] == snapshot1.id


def test_get_decks_filter_card(client: TestClient, snapshot2):
    """Filtering by included card must work"""
    response = client.get("/v2/decks?card=two-ready-spell")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["id"] == snapshot2.id


def test_get_decks_filter_user(client: TestClient, user1, snapshot1):
    """Filtering by user badge must work"""
    # Public deck listings offer filtration by user
    response = client.get(f"/v2/decks?player={urllib.parse.quote(user1.badge)}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["id"] == snapshot1.id


def test_get_mine(client: TestClient, user1, deck1, private_deck1):
    """Listing private decks returns the current user's decks"""
    # This endpoint is functionally identical to the generic deck filter, aside from returning saved
    #  decks, so no need to test all the filters
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    response = client.get(
        f"/v2/decks/mine", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 2
    assert data["results"][0]["id"] == private_deck1.id
    assert data["results"][1]["id"] == deck1.id


def test_get_private_share_deck(client: TestClient, private_deck1):
    """Direct share UUIDs must allow access to the exact deck or snapshot"""
    response = client.get(f"/v2/decks/shared/{private_deck1.direct_share_uuid}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == private_deck1.id


def test_get_private_share_published_snapshot(client: TestClient, snapshot1):
    """Direct share UUIDs must allow access to public snapshots"""
    response = client.get(f"/v2/decks/shared/{snapshot1.direct_share_uuid}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == snapshot1.id


def test_get_private_share_deleted(
    client: TestClient, session: db.Session, user1, deck1
):
    """Deleted decks must throw an error when accessing their direct share UUID"""
    snapshot2 = create_snapshot_for_deck(session, user1, deck1)
    snapshot2.is_deleted = True
    session.commit()
    response = client.get(f"/v2/decks/shared/{snapshot2.direct_share_uuid}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_deck_deleted(client: TestClient, session: db.Session, user1):
    """Deleted decks must not provide access"""
    deck = create_deck_for_user(session, user1)
    deck.is_deleted = True
    session.commit()
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    # Invisible to the owning user
    response = client.get(
        f"/v2/decks/{deck.id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    # Invisible to unauthenticated, too
    response = client.get(f"/v2/decks/{deck.id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_deck_no_record(client: TestClient, session: db.Session, user1):
    """Trying to fetch an ID that no longer exists must fail correctly"""
    deck = create_deck_for_user(session, user1)
    deleted_id = deck.id
    session.delete(deck)
    session.commit()
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    response = client.get(
        f"/v2/decks/{deleted_id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_deck_deleted_public_snapshot(
    client: TestClient, session: db.Session, user1
):
    """Decks with a deleted public snapshot must throw an error"""
    deck = create_deck_for_user(session, user1)
    snapshot = create_snapshot_for_deck(session, user1, deck, is_public=True)
    snapshot.is_deleted = True
    session.commit()
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    # Invisible to the owning user
    response = client.get(
        f"/v2/decks/{deck.id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    # Invisible to unauthenticated, too
    response = client.get(f"/v2/decks/{deck.id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_deck_private_snapshot(client: TestClient, session: db.Session, user1):
    """Unauthenticated users must not be able to access private snapshots"""
    deck = create_deck_for_user(session, user1)
    snapshot = create_snapshot_for_deck(session, user1, deck)
    response = client.get(f"/v2/decks/{snapshot.id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_get_deck_private_saved(client: TestClient, deck1):
    """Unauthenticated users must not be able to access private decks via show_saved"""
    response = client.get(f"/v2/decks/{deck1.id}", params={"show_saved": True})
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_get_deck_public_snapshot(client: TestClient, snapshot1):
    """Public snapshots must return the snapshot"""
    response = client.get(f"/v2/decks/{snapshot1.id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["deck"]["id"] == snapshot1.id


def test_get_deck_private_snapshot_owned(
    client: TestClient, session: db.Session, user1
):
    """Private snapshots must be returned if requested by the owner"""
    deck = create_deck_for_user(session, user1)
    snapshot = create_snapshot_for_deck(session, user1, deck)
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    response = client.get(
        f"/v2/decks/{snapshot.id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["deck"]["id"] == snapshot.id


def test_get_deck(client: TestClient, deck1, snapshot1):
    """By default, the latest public snapshot is returned"""
    response = client.get(f"/v2/decks/{deck1.id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["deck"]["id"] == snapshot1.id


def test_get_deck_saved(client: TestClient, deck1, user1):
    """Showing saved decks must work for the owner"""
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    response = client.get(
        f"/v2/decks/{deck1.id}",
        params={"show_saved": True},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["deck"]["id"] == deck1.id
    assert data["deck"]["is_saved"] == True

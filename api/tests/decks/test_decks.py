import urllib.parse
from datetime import timedelta

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models import Subscription
from api.services.deck import create_snapshot_for_deck
from api.utils.auth import create_access_token

from ..utils import create_admin_token, create_user_token
from .deck_utils import create_deck_for_user


@pytest.fixture(scope="function", autouse=True)
def user1(session):
    user1, _ = create_user_token(session)
    return user1


@pytest.fixture(scope="function", autouse=True)
def deck1(session, user1):
    return create_deck_for_user(session, user1, release_stub="master-set")


@pytest.fixture(scope="function", autouse=True)
def snapshot1(session, user1, deck1):
    return create_snapshot_for_deck(
        session,
        user1,
        deck1,
        title="First Snapshot",
        description="First description",
        is_public=True,
    )


@pytest.fixture(scope="function", autouse=True)
def private_snapshot1(session, user1, deck1):
    return create_snapshot_for_deck(
        session,
        user1,
        deck1,
        title="Private Snapshot",
        description="Private description",
        is_public=False,
    )


@pytest.fixture(scope="function", autouse=True)
def private_deck1(session, user1):
    return create_deck_for_user(session, user1, release_stub="expansion")


@pytest.fixture(scope="function", autouse=True)
def user2(session):
    user2, _ = create_user_token(session)
    return user2


@pytest.fixture(scope="function", autouse=True)
def deck2(session, user2):
    return create_deck_for_user(session, user2, release_stub="expansion")


@pytest.fixture(scope="function", autouse=True)
def snapshot2(session, user2, deck2):
    return create_snapshot_for_deck(
        session,
        user2,
        deck2,
        title="Second Snapshot",
        is_public=True,
    )


@pytest.fixture(scope="function", autouse=True)
def user3(session):
    user3, _ = create_user_token(session)
    return user3


@pytest.fixture(scope="function", autouse=True)
def deck3(session, user3):
    deck3 = create_deck_for_user(session, user3, release_stub="expansion2")
    deck3.is_red_rains = True
    session.commit()
    return deck3


@pytest.fixture(scope="function", autouse=True)
def snapshot3(session, user3, deck3):
    return create_snapshot_for_deck(
        session,
        user3,
        deck3,
        title="Red Rains Snapshot",
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
    assert data["count"] == 1, data
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


def test_get_decks_filter_red_rains(client: TestClient, snapshot3):
    """Filtering for Red Rains decks must work"""
    response = client.get(f"/v2/decks?show_red_rains=true")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["id"] == snapshot3.id


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


def test_get_deck_last_seen_entity_id(
    client: TestClient, session: db.Session, deck1, snapshot1, user2
):
    """Last seen entity ID for a deck must be output properly"""
    sub = Subscription(
        user_id=user2.id,
        source_entity_id=deck1.entity_id,
        last_seen_entity_id=snapshot1.entity_id,
    )
    session.add(sub)
    session.commit()
    token = create_access_token(
        data={"sub": user2.badge},
        expires_delta=timedelta(minutes=15),
    )
    response = client.get(
        f"/v2/decks/{deck1.id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["last_seen_entity_id"] == snapshot1.entity_id


def test_list_snapshots_bad_id(client: TestClient, session: db.Session, user1):
    """Not found error thrown when viewing non-existent deck"""
    deck = create_deck_for_user(session, user1)
    deleted_id = deck.id
    session.delete(deck)
    session.commit()
    response = client.get(f"/v2/decks/{deleted_id}/snapshots")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_list_snapshots_deleted_deck(client: TestClient, session: db.Session, deck1):
    """Not found error thrown when viewing a deleted deck"""
    deck1.is_deleted = True
    session.commit()
    response = client.get(f"/v2/decks/{deck1.id}/snapshots")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_list_snapshots_snapshot_id(client: TestClient, snapshot1):
    """Not found error thrown when viewing a snapshot instead of a source deck"""
    response = client.get(f"/v2/decks/{snapshot1.id}/snapshots")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_list_snapshots_anonymous_user(client: TestClient, private_snapshot1):
    """Anonymous users can only view public snapshots"""
    response = client.get(f"/v2/decks/{private_snapshot1.source_id}/snapshots")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert len(data["results"]) == 1


def test_list_snapshots_other_user(client: TestClient, user2, private_snapshot1):
    """Users cannot view private snapshots for other user's decks"""
    token = create_access_token(
        data={"sub": user2.badge},
        expires_delta=timedelta(minutes=15),
    )
    response = client.get(
        f"/v2/decks/{private_snapshot1.source_id}/snapshots",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert len(data["results"]) == 1


def test_list_snapshots(client: TestClient, user1, private_snapshot1):
    """Users can view both private and public snapshots for decks they own"""
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    response = client.get(
        f"/v2/decks/{private_snapshot1.source_id}/snapshots",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 2
    assert len(data["results"]) == 2


def test_list_snapshots_public_only(client: TestClient, user1, private_snapshot1):
    """Users can view listings that include only public snapshots"""
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    response = client.get(
        f"/v2/decks/{private_snapshot1.source_id}/snapshots",
        params={"show_public_only": True},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 1
    assert len(data["results"]) == 1


def test_edit_snapshot_bad_id(client: TestClient, session: db.Session, user1, deck1):
    """Not found error thrown when viewing non-existent ID"""
    snapshot = create_snapshot_for_deck(session, user1, deck1)
    deleted_id = snapshot.id
    session.delete(snapshot)
    session.commit()
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    response = client.patch(
        f"/v2/decks/snapshots/{deleted_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "New title"},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.json()


def test_edit_snapshot_others_snapshot(client: TestClient, user1, snapshot2):
    """Permissions error when attempting to edit other people's decks"""
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    response = client.patch(
        f"/v2/decks/snapshots/{snapshot2.id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "New title"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_edit_snaphot_not_snapshot(client: TestClient, user1, deck1):
    """Generic error when trying to edit something that is not a snapshot"""
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    response = client.patch(
        f"/v2/decks/snapshots/{deck1.id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "New title"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_edit_snapshot_notes_required_for_moderation(
    client: TestClient, session: db.Session, snapshot1
):
    """Moderation notes are required for admin moderation"""
    admin, token = create_admin_token(session)
    response = client.patch(
        f"/v2/decks/snapshots/{snapshot1.id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "New title"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_edit_snapshot_moderate_description(
    client: TestClient, session: db.Session, snapshot1
):
    """Moderating a description saves the old description"""
    admin, token = create_admin_token(session)
    old_description = snapshot1.description
    new_description = "New description"
    moderation_notes = "Changed description"
    response = client.patch(
        f"/v2/decks/snapshots/{snapshot1.id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"description": new_description, "moderation_notes": moderation_notes},
    )
    assert response.status_code == status.HTTP_200_OK
    session.refresh(snapshot1)
    assert snapshot1.description == new_description
    assert snapshot1.original_description == old_description
    assert snapshot1.is_moderated is True
    assert snapshot1.moderation_notes == moderation_notes


def test_edit_snapshot(client: TestClient, session: db.Session, user1, snapshot1):
    """Users can edit their own snapshots"""
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    new_title = "New title"
    new_description = "New description"
    response = client.patch(
        f"/v2/decks/snapshots/{snapshot1.id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": new_title, "description": new_description},
    )
    assert response.status_code == status.HTTP_200_OK
    session.refresh(snapshot1)
    assert snapshot1.title == new_title
    assert snapshot1.description == new_description


def test_edit_snapshot_clear_description(
    client: TestClient, session: db.Session, user1, snapshot1
):
    """Users can pass empty strings to clear descriptions"""
    token = create_access_token(
        data={"sub": user1.badge},
        expires_delta=timedelta(minutes=15),
    )
    old_title = snapshot1.title
    new_description = ""
    response = client.patch(
        f"/v2/decks/snapshots/{snapshot1.id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"description": new_description},
    )
    assert response.status_code == status.HTTP_200_OK
    session.refresh(snapshot1)
    assert snapshot1.title == old_title
    assert snapshot1.description is None

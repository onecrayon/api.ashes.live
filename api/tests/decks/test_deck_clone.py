import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models import Deck
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


@pytest.fixture(scope="module", autouse=True)
def deck(decks_session, user_token):
    user, _ = user_token
    return create_deck_for_user(decks_session, user)


@pytest.fixture(scope="module", autouse=True)
def snapshot(decks_session, user_token, deck):
    user, _ = user_token
    return create_snapshot_for_deck(
        decks_session,
        user,
        deck,
        title="First Snapshot",
        description="First description",
        is_public=False,
    )


@pytest.fixture(scope="module", autouse=True)
def public_snapshot(decks_session, user_token, deck):
    user, _ = user_token
    return create_snapshot_for_deck(
        decks_session,
        user,
        deck,
        title="Second Snapshot",
        description="Second description",
        is_public=True,
    )


def test_clone_others_deck(client: TestClient, deck, user2_token):
    """Cannot clone a deck owned by someone else"""
    _, token = user2_token
    response = client.get(
        f"/v2/decks/{deck.id}/clone", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_clone_others_private_snapshot(client: TestClient, snapshot, user2_token):
    """Cannot clone a private snapshot owned by someone else"""
    _, token = user2_token
    response = client.get(
        f"/v2/decks/{snapshot.id}/clone", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_clone_public_snapshot(
    client: TestClient, session: db.Session, user2_token, public_snapshot
):
    """Can clone a public snapshot from another user"""
    user, token = user2_token
    response = client.get(
        f"/v2/decks/{public_snapshot.id}/clone",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    # One is the new deck object, and the other is the source ID snapshot
    assert session.query(Deck).filter(Deck.user_id == user.id).count() == 2


def test_clone_private_snapshot(
    client: TestClient, session: db.Session, snapshot, user_token
):
    """Can clone own private snapshot"""
    user, token = user_token
    # Verify that we have three "decks" (original deck, private snapshot, public snapshot)
    assert session.query(Deck).filter(Deck.user_id == user.id).count() == 3
    response = client.get(
        f"/v2/decks/{snapshot.id}/clone",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    # Check that we now have two more decks than before: new deck, and source snapshot
    assert session.query(Deck).filter(Deck.user_id == user.id).count() == 5


def test_clone_deck(client: TestClient, session: db.Session, deck, user_token):
    """Can clone own deck"""
    user, token = user_token
    # Verify that we have three "decks" (original deck, private snapshot, public snapshot)
    assert session.query(Deck).filter(Deck.user_id == user.id).count() == 3
    response = client.get(
        f"/v2/decks/{deck.id}/clone",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    # Check that we now have two more decks than before: new deck, and source snapshot
    assert session.query(Deck).filter(Deck.user_id == user.id).count() == 5


def test_clone_private_shared_deck(
    client: TestClient, session: db.Session, snapshot, user2_token
):
    """Can clone a private shared deck with direct_share_uuid"""
    user, token = user2_token
    response = client.get(
        f"/v2/decks/{snapshot.id}/clone",
        params={"direct_share_uuid": str(snapshot.direct_share_uuid)},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK, response.json()
    # One is the new deck object, and the other is the source ID snapshot
    assert session.query(Deck).filter(Deck.user_id == user.id).count() == 2


def test_clone_deck_red_rains(
    client: TestClient, session: db.Session, public_snapshot, user2_token
):
    """Can clone a deck as a Red Rains deck"""
    assert public_snapshot.is_red_rains is False
    user, token = user2_token
    response = client.get(
        f"/v2/decks/{public_snapshot.id}/clone",
        params={"red_rains": True},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    # Verify that we have two decks (deck and snapshot) and both are marked as Red Rains decks
    assert (
        session.query(Deck)
        .filter(Deck.user_id == user.id, Deck.is_red_rains.is_(True))
        .count()
        == 2
    )

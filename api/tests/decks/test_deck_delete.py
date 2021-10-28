import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models import Deck, Stream
from api.services.deck import create_snapshot_for_deck
from api.tests.decks.deck_utils import create_deck_for_user
from api.tests.utils import create_user_token


@pytest.fixture(scope="module", autouse=True)
def user_token(decks_session):
    user, token = create_user_token(decks_session)
    return user, token


@pytest.fixture(scope="module")
def deck(decks_session, user_token):
    user, _ = user_token
    return create_deck_for_user(decks_session, user)


def test_delete_deck_bad_deck(client: TestClient, session: db.Session, user_token):
    """Must disallow access to deck IDs that don't exist"""
    user, token = user_token
    deck = create_deck_for_user(session, user)
    bad_id = deck.id
    session.delete(deck)
    session.commit()
    response = client.delete(
        f"/v2/decks/{bad_id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_delete_deck_anonymous(client: TestClient, session: db.Session, deck):
    """Anonymous requests to delete decks must fail"""
    response = client.delete(f"/v2/decks/{deck.id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_delete_deck_wrong_user(client: TestClient, session: db.Session, deck):
    """Requests to delete a deck by the wrong user must fail"""
    user2, token = create_user_token(session)
    response = client.delete(
        f"/v2/decks/{deck.id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_delete_deck_legacy(client: TestClient, session: db.Session, user_token):
    """Requests to delete a legacy deck must fail"""
    user, token = user_token
    deck = create_deck_for_user(session, user)
    deck.is_legacy = True
    session.commit()
    response = client.delete(
        f"/v2/decks/{deck.id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_delete_deck_already_deleted(
    client: TestClient, session: db.Session, user_token
):
    """Must return success if deck was previously deleted"""
    user, token = user_token
    deck = create_deck_for_user(session, user)
    deck.is_deleted = True
    session.commit()
    response = client.delete(
        f"/v2/decks/{deck.id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_deck_no_snapshots(
    client: TestClient, session: db.Session, user_token, deck
):
    """Must actually delete the deck if it has no snapshots"""
    user, token = user_token
    old_id = deck.id
    response = client.delete(
        f"/v2/decks/{deck.id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert session.query(Deck).filter(Deck.id == old_id).first() is None


def test_delete_public_snapshot(
    client: TestClient, session: db.Session, user_token, deck
):
    """Must properly clean up stream entries when deleting a public snapshot"""
    user, token = user_token
    snapshot = create_snapshot_for_deck(session, user, deck, is_public=True)
    assert session.query(Stream).count() == 1
    response = client.delete(
        f"/v2/decks/{snapshot.id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert session.query(Stream).count() == 0
    session.refresh(snapshot)
    assert snapshot.is_deleted == True


def test_delete_latest_public_snapshot(
    client: TestClient, session: db.Session, user_token, deck
):
    """Must properly revert to older snapshot in stream when deleting a public snapshot"""
    user, token = user_token
    snapshot1 = create_snapshot_for_deck(session, user, deck, is_public=True)
    snapshot2 = create_snapshot_for_deck(session, user, deck, is_public=True)
    assert session.query(Stream).count() == 1
    response = client.delete(
        f"/v2/decks/{snapshot2.id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    stream_entry = session.query(Stream).first()
    assert stream_entry.entity_id == snapshot1.entity_id
    session.refresh(snapshot2)
    assert snapshot2.is_deleted == True


def test_delete_root_deck(client: TestClient, session: db.Session, user_token):
    """Must delete stream entry and mark all snapshots deleted when deleting root deck"""
    user, token = user_token
    deck = create_deck_for_user(session, user)
    private_snapshot = create_snapshot_for_deck(session, user, deck)
    public_snapshot = create_snapshot_for_deck(session, user, deck, is_public=True)
    assert session.query(Stream).count() == 1
    response = client.delete(
        f"/v2/decks/{deck.id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert session.query(Stream).count() == 0
    session.refresh(deck)
    session.refresh(private_snapshot)
    session.refresh(public_snapshot)
    assert deck.is_deleted == True
    assert private_snapshot.is_deleted == True
    assert public_snapshot.is_deleted == True

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models import Deck
from api.tests.decks.deck_utils import create_deck_for_user
from api.tests.utils import create_user_token


@pytest.fixture(scope="module", autouse=True)
def user_token(cards_session):
    user, token = create_user_token(cards_session)
    return user, token


@pytest.fixture(scope="module")
def deck(cards_session, user_token):
    user, _ = user_token
    return create_deck_for_user(cards_session, user)


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

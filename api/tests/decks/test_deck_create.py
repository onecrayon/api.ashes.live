import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models import Card
from api.services.deck import create_snapshot_for_deck
from api.tests.decks.deck_utils import (
    CONJURATION_TYPES,
    create_deck_for_user,
    get_phoenixborn_cards_dice,
)
from api.tests.utils import create_user_token, generate_random_chars


@pytest.fixture(scope="module", autouse=True)
def user_token(cards_session):
    user, token = create_user_token(cards_session)
    return user, token


def _valid_deck_dict(session: db.Session) -> dict:
    """Generates a minimal valid deck dict for PUT-ing"""
    phoenixborn, card_dicts, dice_dicts = get_phoenixborn_cards_dice(session)
    return {
        "title": generate_random_chars(),
        "phoenixborn": phoenixborn.stub,
        "dice": dice_dicts,
        "cards": card_dicts,
    }


def test_put_deck_bad_id(client: TestClient, session: db.Session, user_token):
    """Must not allow uploading a deck with a bad ID"""
    # Create a deck so that we can ensure no accidental ID collisions
    user, token = user_token
    deck = create_deck_for_user(session, user)
    bad_id = deck.id
    session.delete(deck)
    session.commit()
    valid_deck = _valid_deck_dict(session)
    valid_deck["id"] = bad_id
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_put_deck_others_id(client: TestClient, session: db.Session, user_token):
    """Must not allow uploading a deck with an ID owned by another user"""
    user, token = user_token
    user2, _ = create_user_token(session)
    deck = create_deck_for_user(session, user2)
    valid_deck = _valid_deck_dict(session)
    valid_deck["id"] = deck.id
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_put_deck_legacy(client: TestClient, session: db.Session, user_token):
    """Must not allow saving legacy decks"""
    user, token = user_token
    deck = create_deck_for_user(session, user)
    deck.is_legacy = True
    session.commit()
    valid_deck = _valid_deck_dict(session)
    valid_deck["id"] = deck.id
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_put_deck_snapshot(client: TestClient, session: db.Session, user_token):
    """Must not allow saving over a snapshot ID"""
    user, token = user_token
    deck = create_deck_for_user(session, user)
    snapshot = create_snapshot_for_deck(session, user, deck)
    valid_deck = _valid_deck_dict(session)
    valid_deck["id"] = snapshot.id
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_put_deck_deleted(client: TestClient, session: db.Session, user_token):
    """Must not allow saving over a deleted deck"""
    user, token = user_token
    deck = create_deck_for_user(session, user)
    deck.is_deleted = True
    session.commit()
    valid_deck = _valid_deck_dict(session)
    valid_deck["id"] = deck.id
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_put_deck_fake_phoenixborn(client: TestClient, session: db.Session, user_token):
    """Must not allow submitting a deck with a wrong Phoenixborn stub"""
    user, token = user_token
    valid_deck = _valid_deck_dict(session)
    valid_deck["phoenixborn"] = "not_a_phoenixborn"
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_put_deck_phoenixborn_in_deck(
    client: TestClient, session: db.Session, user_token
):
    """Must not allow creating a deck with a Phoenixborn in the deck"""
    user, token = user_token
    valid_deck = _valid_deck_dict(session)
    valid_deck["cards"].append(
        {
            "stub": valid_deck["phoenixborn"],
            "count": 3,
        }
    )
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_put_deck_bad_unique_in_deck(
    client: TestClient, session: db.Session, user_token
):
    """Must not allow saving a deck with a PB unique for the wrong PB"""
    user, token = user_token
    valid_deck = _valid_deck_dict(session)
    # Add all PB uniques to the deck (easiest way to ensure we have the wrong one)
    pb_uniques_query = session.query(Card.stub).filter(
        Card.phoenixborn.isnot(None),
        Card.card_type.notin_(CONJURATION_TYPES),
    )
    for unique in pb_uniques_query.all():
        valid_deck["cards"].append(
            {
                "stub": unique.stub,
                "count": 3,
            }
        )
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_put_deck_conjuration_in_deck(
    client: TestClient, session: db.Session, user_token
):
    """Must not allow saving a deck with conjurations in the card list"""
    user, token = user_token
    valid_deck = _valid_deck_dict(session)
    conjuration_stub = (
        session.query(Card.stub)
        .filter(Card.card_type.in_(CONJURATION_TYPES))
        .limit(1)
        .scalar()
    )
    valid_deck["cards"].append(
        {
            "stub": conjuration_stub,
            "count": 3,
        }
    )
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_put_deck(client: TestClient, session: db.Session, user_token):
    """Must allow saving a valid deck"""
    user, token = user_token
    valid_deck = _valid_deck_dict(session)
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK


def test_put_deck_update(client: TestClient, session: db.Session, user_token):
    """Must allow saving a new copy of an existing deck"""
    user, token = user_token
    deck = create_deck_for_user(session, user)
    valid_deck = _valid_deck_dict(session)
    valid_deck["id"] = deck.id
    new_title = generate_random_chars(8)
    assert new_title != deck.title
    valid_deck["title"] = new_title
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    session.refresh(deck)
    assert deck.title == new_title


def test_put_deck_too_many_dice(client: TestClient, session: db.Session, user_token):
    """Must not save more than 10 dice"""
    user, token = user_token
    valid_deck = _valid_deck_dict(session)
    valid_deck["dice"] = [
        {"name": "natural", "count": 8},
        {"name": "sympathy", "count": 10},
        {"name": "charm", "count": 5},
    ]
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["dice"][0]["name"] == "natural"
    assert data["dice"][0]["count"] == 8
    assert data["dice"][1]["name"] == "sympathy"
    assert data["dice"][1]["count"] == 2

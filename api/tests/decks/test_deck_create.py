import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models import Card, Deck, DeckSelectedCard, Release
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


@pytest.fixture(scope="module")
def deck(cards_session, user_token):
    user, _ = user_token
    return create_deck_for_user(cards_session, user)


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


def test_put_deck_snapshot(client: TestClient, session: db.Session, user_token, deck):
    """Must not allow saving over a snapshot ID"""
    user, token = user_token
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


def test_put_deck_first_five(client: TestClient, session: db.Session, user_token):
    """Must properly handle both good and bogus cards within the first five list"""
    user, token = user_token
    valid_deck = _valid_deck_dict(session)
    valid_stubs = [x["stub"] for x in valid_deck["cards"]]
    bad_stub = (
        session.query(Card.stub)
        .filter(
            Card.phoenixborn.is_(None),
            Card.card_type.notin_(CONJURATION_TYPES),
            Card.card_type != "Phoenixborn",
            Card.stub.notin_(valid_stubs),
        )
        .limit(1)
        .scalar()
    )
    valid_deck["first_five"] = [valid_stubs[x] for x in range(0, 4)]
    valid_deck["first_five"].append(bad_stub)
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert bad_stub not in data["first_five"]
    assert valid_stubs[0] in data["first_five"]


def test_put_deck_effect_costs(client: TestClient, session: db.Session, user_token):
    """Must properly handle both good and bogus cards within the effect costs"""
    user, token = user_token
    valid_deck = _valid_deck_dict(session)
    valid_stubs = [x["stub"] for x in valid_deck["cards"]]
    bad_stub = (
        session.query(Card.stub)
        .filter(
            Card.phoenixborn.is_(None),
            Card.card_type.notin_(CONJURATION_TYPES),
            Card.card_type != "Phoenixborn",
            Card.stub.notin_(valid_stubs),
        )
        .limit(1)
        .scalar()
    )
    valid_deck["first_five"] = [valid_stubs[x] for x in range(0, 5)]
    valid_deck["effect_costs"] = [valid_stubs[x] for x in range(0, 4)]
    valid_deck["effect_costs"].append(bad_stub)
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert bad_stub not in data["effect_costs"]
    assert valid_stubs[0] in data["effect_costs"]


def test_put_deck_tutor_map(client: TestClient, session: db.Session, user_token):
    """Must properly handle both good and bogus cards within tutor map"""
    user, token = user_token
    valid_deck = _valid_deck_dict(session)
    valid_stubs = [x["stub"] for x in valid_deck["cards"]]
    bad_stub = (
        session.query(Card.stub)
        .filter(
            Card.phoenixborn.is_(None),
            Card.card_type.notin_(CONJURATION_TYPES),
            Card.card_type != "Phoenixborn",
            Card.stub.notin_(valid_stubs),
        )
        .limit(1)
        .scalar()
    )
    valid_deck["tutor_map"] = {
        valid_stubs[0]: valid_stubs[1],
        bad_stub: valid_stubs[2],
        valid_stubs[3]: bad_stub,
    }
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert bad_stub not in data["tutor_map"].keys()
    assert bad_stub not in data["tutor_map"].values()
    assert valid_stubs[0] in data["tutor_map"].keys()
    assert valid_stubs[1] in data["tutor_map"].values()


def test_post_snapshot_bad_deck_id(client: TestClient, session: db.Session, user_token):
    """Must not allow creating a snapshot for a bad deck ID"""
    # Create a deck so that we can ensure no accidental ID collisions
    user, token = user_token
    deck = create_deck_for_user(session, user)
    bad_id = deck.id
    session.delete(deck)
    session.commit()
    response = client.post(
        f"/v2/decks/{bad_id}/snapshot",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_post_snapshot_other_users_deck(
    client: TestClient, session: db.Session, user_token, deck
):
    """Must not allow creating a snapshot from another user's deck"""
    # Create a deck so that we can ensure no accidental ID collisions
    user, _ = user_token
    user2, token2 = create_user_token(session)
    response = client.post(
        f"/v2/decks/{deck.id}/snapshot",
        headers={"Authorization": f"Bearer {token2}"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_post_snapshot_legacy_deck(client: TestClient, session: db.Session, user_token):
    """Must not allow posting snapshots for legacy decks"""
    user, token = user_token
    deck = create_deck_for_user(session, user)
    deck.is_legacy = True
    session.commit()
    response = client.post(
        f"/v2/decks/{deck.id}/snapshot",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_post_snapshot_for_snapshot(
    client: TestClient, session: db.Session, user_token, deck
):
    """Must not allow creating a snapshot from another snapshot"""
    user, token = user_token
    snapshot = create_snapshot_for_deck(session, user, deck)
    response = client.post(
        f"/v2/decks/{snapshot.id}/snapshot",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_post_snapshot_deleted_deck(
    client: TestClient, session: db.Session, user_token
):
    """Must not allow creating snapshots for a deleted deck"""
    user, token = user_token
    deck = create_deck_for_user(session, user)
    deck.is_deleted = True
    session.commit()
    response = client.post(
        f"/v2/decks/{deck.id}/snapshot",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_post_snapshot(client: TestClient, session: db.Session, user_token, deck):
    """Must allow creating a straight copy snapshot"""
    user, token = user_token
    response = client.post(
        f"/v2/decks/{deck.id}/snapshot",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_post_snapshot_public_bad_dice(
    client: TestClient, session: db.Session, user_token
):
    """Must stop creation of a public snapshot if not 10 dice"""
    user, token = user_token
    valid_deck = _valid_deck_dict(session)
    valid_deck["dice"].pop()
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    # Then try to create a public snapshot
    response = client.post(
        f"/v2/decks/{response.json()['id']}/snapshot",
        json={"is_public": True},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_post_snapshot_public_bad_cards(
    client: TestClient, session: db.Session, user_token
):
    """Must stop creation of a public snapshot if not 10 dice"""
    user, token = user_token
    valid_deck = _valid_deck_dict(session)
    valid_deck["cards"].pop()
    response = client.put(
        "/v2/decks", json=valid_deck, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    # Then try to create a public snapshot
    response = client.post(
        f"/v2/decks/{response.json()['id']}/snapshot",
        json={"is_public": True},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_post_snapshot_precon_non_admin(
    client: TestClient, session: db.Session, user_token
):
    """Must stop creation of preconstructed release snapshots if not an admin"""
    user, token = user_token
    deck = create_deck_for_user(session, user, release_stub="expansion")
    response = client.post(
        f"/v2/decks/{deck.id}/snapshot",
        json={"preconstructed_release": "expansion", "is_public": True},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_post_snapshot_precon_non_public(client: TestClient, session: db.Session):
    """Must stop creation of preconstructed release if not a public snapshot"""
    admin, token = create_user_token(session)
    admin.is_admin = True
    session.commit()
    deck = create_deck_for_user(session, admin, release_stub="expansion")
    response = client.post(
        f"/v2/decks/{deck.id}/snapshot",
        json={"preconstructed_release": "expansion"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_post_snapshot_precon_already_exists(client: TestClient, session: db.Session):
    """Must not allow posting a precon snapshot if it already exists"""
    admin, token = create_user_token(session)
    admin.is_admin = True
    session.commit()
    release_id = session.query(Release.id).filter(Release.stub == "expansion").scalar()
    deck = create_deck_for_user(session, admin, release_stub="expansion")
    snapshot = create_snapshot_for_deck(
        session, admin, deck, is_public=True, preconstructed_release_id=release_id
    )
    response = client.post(
        f"/v2/decks/{deck.id}/snapshot",
        json={"preconstructed_release": "expansion", "is_public": True},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_post_snapshot(client: TestClient, session: db.Session, user_token, deck):
    """Posting a snapshot must inherit the old deck's details"""
    user, token = user_token
    response = client.post(
        f"/v2/decks/{deck.id}/snapshot",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    snapshot = session.query(Deck).order_by(Deck.id.desc()).first()
    assert snapshot.title == deck.title
    assert snapshot.description == deck.description


def test_post_snapshot_clear_description(
    client: TestClient, session: db.Session, user_token, deck
):
    """Posting a snapshot with an empty description must use an empty description"""
    user, token = user_token
    new_title = generate_random_chars(4)
    response = client.post(
        f"/v2/decks/{deck.id}/snapshot",
        json={"title": new_title, "description": ""},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    snapshot = session.query(Deck).order_by(Deck.id.desc()).first()
    assert snapshot.title == new_title
    assert snapshot.description is None


def test_post_snapshot_new_description(
    client: TestClient, session: db.Session, user_token, deck
):
    """Posting a snapshot must allow replacing the description"""
    user, token = user_token
    new_description = generate_random_chars(9)
    response = client.post(
        f"/v2/decks/{deck.id}/snapshot",
        json={"description": new_description},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    snapshot = session.query(Deck).order_by(Deck.id.desc()).first()
    assert snapshot.description == new_description


def test_post_snapshot_first_five(client: TestClient, session: db.Session, user_token):
    """Private snapshots must include First Five information"""
    user, token = user_token
    deck = create_deck_for_user(session, user)
    deck.selected_cards = [
        DeckSelectedCard(
            deck_id=deck.id, card_id=deck.cards[0].card_id, is_first_five=True
        )
    ]
    session.commit()
    response = client.post(
        f"/v2/decks/{deck.id}/snapshot",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    snapshot = (
        session.query(Deck).order_by(Deck.id.desc(), Deck.is_snapshot.is_(True)).first()
    )
    assert len(snapshot.selected_cards) == 1


def test_post_snapshot_no_first_five_public(
    client: TestClient, session: db.Session, user_token
):
    """Public snapshots must default to no First Five info"""
    user, token = user_token
    deck = create_deck_for_user(session, user)
    deck.selected_cards = [
        DeckSelectedCard(
            deck_id=deck.id, card_id=deck.cards[0].card_id, is_first_five=True
        )
    ]
    session.commit()
    response = client.post(
        f"/v2/decks/{deck.id}/snapshot",
        json={"is_public": True},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    snapshot = (
        session.query(Deck).order_by(Deck.id.desc(), Deck.is_snapshot.is_(True)).first()
    )
    assert len(snapshot.selected_cards) == 0

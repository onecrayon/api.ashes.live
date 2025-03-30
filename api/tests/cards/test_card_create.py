from copy import copy

from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models.card import Card, CardConjuration
from api.models.release import Release

from ..utils import create_admin_token

MINIMUM_VALID_CARD = {
    "name": "Example Card",
    "card_type": "Action Spell",
    "placement": "Discard",
    "release": "The Example Release",
    "text": "Do something and then something else.",
}


def test_create_card_require_name(client: TestClient, session: db.Session):
    """Creating a card requires a name"""
    admin, token = create_admin_token(session)
    card_data = copy(MINIMUM_VALID_CARD)
    del card_data["name"]
    response = client.post(
        "/v2/cards",
        json=card_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()


def test_create_card_require_card_type(client: TestClient, session: db.Session):
    """Creating a card requires a card type"""
    admin, token = create_admin_token(session)
    card_data = copy(MINIMUM_VALID_CARD)
    del card_data["card_type"]
    response = client.post(
        "/v2/cards",
        json=card_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()


def test_create_card_invalid_card_type(client: TestClient, session: db.Session):
    """Creating a card requires a valid card type"""
    admin, token = create_admin_token(session)
    card_data = copy(MINIMUM_VALID_CARD)
    card_data["card_type"] = "Action"
    response = client.post(
        "/v2/cards",
        json=card_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()


def test_create_card_require_valid_placement(client: TestClient, session: db.Session):
    """Creating a card requires a placement"""
    admin, token = create_admin_token(session)
    card_data = copy(MINIMUM_VALID_CARD)
    card_data["placement"] = "Ceiling"
    response = client.post(
        "/v2/cards",
        json=card_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()


def test_create_card_require_placement_non_phoenixborn(
    client: TestClient, session: db.Session
):
    """Creating a card that isn't a Phoenixborn requires a placement"""
    admin, token = create_admin_token(session)
    card_data = copy(MINIMUM_VALID_CARD)
    del card_data["placement"]
    response = client.post(
        "/v2/cards",
        json=card_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()


def test_create_card_placement_optional_phoenixborn(
    client: TestClient, session: db.Session
):
    """Creating a Phoenixborn doesn't require a placement"""
    admin, token = create_admin_token(session)
    card_data = copy(MINIMUM_VALID_CARD)
    del card_data["placement"]
    card_data["card_type"] = "Phoenixborn"
    response = client.post(
        "/v2/cards",
        json=card_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED, response.json()


def test_create_card_implicit_release(client: TestClient, session: db.Session):
    """Creating a card implicitly creates an unpublished release"""
    # Verify that the number of releases is what we expect
    release_query = (
        session.query(Release)
        .filter(Release.is_legacy.is_(False))
        .order_by(Release.id.desc())
    )
    assert release_query.count() == 2
    admin, token = create_admin_token(session)
    response = client.post(
        "/v2/cards",
        json=MINIMUM_VALID_CARD,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED, response.json()
    assert release_query.count() == 3
    release: Release = release_query.first()
    assert release.name == MINIMUM_VALID_CARD["release"]
    assert release.is_public == False
    # And verify we don't end up with multiple releases on subsequent cards
    card_data = copy(MINIMUM_VALID_CARD)
    card_data["name"] += " 2"
    response = client.post(
        "/v2/cards",
        json=card_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED, response.json()
    assert release_query.count() == 3


def test_create_card_missing_conjuration(client: TestClient, session: db.Session):
    """Creating a card requires all conjurations to be created first"""
    admin, token = create_admin_token(session)
    card_data = copy(MINIMUM_VALID_CARD)
    card_data["text"] = (
        "Place a [[Missing Conjuration]] conjuration on your battlefield."
    )
    response = client.post(
        "/v2/cards",
        json=card_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.json()


def test_create_card_populates_conjurations(client: TestClient, session: db.Session):
    """Creating a card adds its conjuration relationships"""
    # Verify that the pre-existing number of conjurations is what we expect
    assert session.query(CardConjuration).count() == 6
    admin, token = create_admin_token(session)
    # Create the conjuration first
    conj_data = copy(MINIMUM_VALID_CARD)
    conj_data["card_type"] = "Conjuration"
    conj_data["copies"] = 1
    conj_response = client.post(
        "/v2/cards", json=conj_data, headers={"Authorization": f"Bearer {token}"}
    )
    assert conj_response.status_code == status.HTTP_201_CREATED, conj_response.json()
    # Then create the card that summons the conjuration
    card_data = copy(MINIMUM_VALID_CARD)
    card_data["name"] = "Summon Example Card"
    card_data["text"] = "Place an [[Example Card]] conjuration on your battlefield."
    card_response = client.post(
        "/v2/cards", json=card_data, headers={"Authorization": f"Bearer {token}"}
    )
    assert card_response.status_code == status.HTTP_201_CREATED, card_response.json()
    # Then verify that the conjuration is linked to the card
    assert session.query(CardConjuration).count() == 7


def test_create_card_conjuration_copies_required(
    client: TestClient, session: db.Session
):
    """Copies is a required field when creating a conjuration"""
    admin, token = create_admin_token(session)
    card_data = copy(MINIMUM_VALID_CARD)
    card_data["card_type"] = "Conjuration"
    response = client.post(
        "/v2/cards",
        json=card_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()
    # And verify that it works when copies is passed in
    card_data["copies"] = 1
    response = client.post(
        "/v2/cards",
        json=card_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED, response.json()


def test_create_card_duplicate(client: TestClient, session: db.Session):
    """Creating a duplicate card fails properly"""
    admin, token = create_admin_token(session)
    response = client.post(
        "/v2/cards",
        json=MINIMUM_VALID_CARD,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED, response.json()
    # And try to duplicate
    response = client.post(
        "/v2/cards",
        json=MINIMUM_VALID_CARD,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.json()

from copy import copy

from fastapi import status
from fastapi.testclient import TestClient

from api import db

from .utils import create_admin_token


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

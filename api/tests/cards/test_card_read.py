from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models import Card


def test_get_legacy_card(client: TestClient, session: db.Session):
    """Must be able to read JSON for a legacy card"""
    # This is handled by a migration normally (legacy cards can't normally be created by this API)
    card = (
        session.query(Card)
        .filter(Card.stub == "example-phoenixborn", Card.is_legacy == True)
        .first()
    )
    card.json["release"]["is_legacy"] = True
    card.json["is_legacy"] = True
    db.flag_modified(card, "json")
    session.commit()
    response = client.get("/v2/cards/example-phoenixborn", params={"show_legacy": True})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["is_legacy"] == True, response.json()


def test_get_card(client: TestClient, session: db.Session):
    """Must be able to read non-Legacy JSON"""
    response = client.get("/v2/cards/example-phoenixborn")
    assert response.status_code == status.HTTP_200_OK
    assert "is_legacy" not in response.json(), response.json()


def test_get_nonexistent_card(client: TestClient, session: db.Session):
    """Must throw an error when the card doesn't exist"""
    response = client.get("/v2/cards/no-luck")
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.json()


def test_get_details_no_card(client: TestClient, session: db.Session):
    """Must fail properly when requesting non-existent card"""
    response = client.get("/v2/cards/no-luck/details")
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.json()


def test_get_details_root_phoenixborn(client: TestClient, session: db.Session):
    """Must properly find root Phoenixborn cards"""
    response = client.get("/v2/cards/example-conjured-alteration/details")
    assert response.status_code == status.HTTP_200_OK


def test_get_details_root_non_phoenixborn(client: TestClient, session: db.Session):
    """Must properly find root non-Phoenixborn cards"""
    response = client.get("/v2/cards/summon-example-conjuration/details")
    assert response.status_code == status.HTTP_200_OK


def test_get_details_root_phoenixborn_conjurations(
    client: TestClient, session: db.Session
):
    """Must properly find conjurations when looking up Phoenixborn unique"""
    response = client.get("/v2/cards/example-ally/details")
    assert response.status_code == status.HTTP_200_OK


def test_get_details_phoenixborn(client: TestClient, session: db.Session):
    """Must properly find connected cards when looking up Phoenixborn"""
    response = client.get("/v2/cards/example-phoenixborn/details")
    assert response.status_code == status.HTTP_200_OK

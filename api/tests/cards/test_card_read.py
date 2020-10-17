from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models.release import Release
from api.services.card import create_card


def _create_legacy_and_normal_cards(session: db.Session):
    release_legacy = Release(name="Example")
    release_legacy.is_public = True
    release_legacy.is_legacy = True
    session.add(release_legacy)
    session.commit()
    card = create_card(
        session,
        **{
            "name": "Example",
            "card_type": "Action Spell",
            "placement": "Discard",
            "release": release_legacy,
            "text": "Text.",
        },
    )
    card.is_legacy = True
    # This is handled by a migration normally (legacy cards can't normally be created by this API)
    card.json["release"]["is_legacy"] = True
    card.json["is_legacy"] = True
    db.flag_modified(card, "json")
    session.commit()
    # And create a non-legacy version
    release = Release(name="Example")
    release.is_public = True
    session.add(release)
    session.commit()
    create_card(
        session,
        **{
            "name": "Example",
            "card_type": "Reaction Spell",
            "placement": "Discard",
            "release": release,
            "text": "Text.",
        },
    )


def test_get_legacy_card(client: TestClient, session: db.Session):
    """Must be able to read JSON for a legacy card"""
    _create_legacy_and_normal_cards(session)
    response = client.get("/v2/cards/example", params={"show_legacy": True})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["is_legacy"] == True, response.json()


def test_get_card(client: TestClient, session: db.Session):
    """Must be able to read non-Legacy JSON"""
    _create_legacy_and_normal_cards(session)
    response = client.get("/v2/cards/example")
    assert response.status_code == status.HTTP_200_OK
    assert "is_legacy" not in response.json(), response.json()


def test_get_nonexistant_card(client: TestClient, session: db.Session):
    """Must throw an error when the card doesn't exist"""
    response = client.get("/v2/cards/no-luck")
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.json()

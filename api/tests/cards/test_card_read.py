from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models import Card, Comment, Subscription
from api.services.stream import create_entity
from api.tests.utils import create_user_token


def test_get_legacy_card(client: TestClient):
    """Must be able to read JSON for a legacy card"""
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


def test_get_details_non_phoenixborn_conjuration(
    client: TestClient, session: db.Session
):
    """Must properly find root summons for non-Phoenixborn conjurations"""
    response = client.get("/v2/cards/example-conjuration/details")
    assert response.status_code == status.HTTP_200_OK


def test_get_details_phoenixborn(client: TestClient, session: db.Session):
    """Must properly find connected cards when looking up Phoenixborn"""
    response = client.get("/v2/cards/example-phoenixborn/details")
    assert response.status_code == status.HTTP_200_OK


def test_get_details_last_seen_entity_id(client: TestClient, session: db.Session):
    """Must properly output last seen entity ID for cards with comments and subscriptions"""
    user, token = create_user_token(session)
    card = session.query(Card).filter(Card.is_legacy == False).first()
    comment = Comment(
        entity_id=create_entity(session),
        user_id=user.id,
        source_entity_id=card.entity_id,
        source_type="card",
        source_version=card.version,
        text="My first comment",
        ordering_increment=1,
    )
    session.add(comment)
    sub = Subscription(
        user_id=user.id,
        source_entity_id=card.entity_id,
        last_seen_entity_id=comment.entity_id,
    )
    session.add(sub)
    session.commit()
    response = client.get(
        f"/v2/cards/{card.stub}/details", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["last_seen_entity_id"] == comment.entity_id


def test_get_card_fuzzy_lookup_required_query(client: TestClient):
    """Must require querystring"""
    response = client.get("/v2/cards/fuzzy-lookup")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    response = client.get("/v2/cards/fuzzy-lookup?q=%20%20")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_card_fuzzy_lookup_legacy(client: TestClient):
    """Must fetch legacy cards properly"""
    response = client.get("/v2/cards/fuzzy-lookup?q=action&show_legacy=true")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["is_legacy"] is True, data


def test_get_card_fuzzy_lookup_bad_query(client: TestClient):
    """Must throw appropriate error when search returns no results"""
    response = client.get("/v2/cards/fuzzy-lookup?q=nada")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_card_fuzzy_lookup_exact_stub(client: TestClient):
    """Must correctly select when the stub is exact"""
    response = client.get("/v2/cards/fuzzy-lookup?q=Example%20Conjuration")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["stub"] == "example-conjuration"


def test_get_fuzzy_lookup_summon_stub(client: TestClient):
    response = client.get("/v2/cards/fuzzy-lookup?q=Summon%20Example")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["stub"] == "summon-example-conjuration"

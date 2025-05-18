from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models import Card
from api.tests.utils import create_admin_token


def test_patch_card_anonymous(client: TestClient, session: db.Session):
    """Anonymous users cannot patch cards"""
    response = client.patch("/v2/cards/example-phoenixborn", json={"name": "Wesley"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_patch_card_missing(client: TestClient, session: db.Session):
    """Cannot patch cards that do not exist"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/nowayinheck",
        json={"name": "Wesley"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_patch_card_errata(client: TestClient, session: db.Session):
    """Marking as errata increases the version"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-phoenixborn",
        json={"name": "Wesley", "is_errata": True},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    card = session.query(Card).filter(Card.stub == "wesley").first()
    assert card.version == 2


def test_patch_card_name(client: TestClient, session: db.Session):
    """Editing the name must update the name, search text, and stub"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-phoenixborn",
        json={"name": "Wesley"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    card_data = response.json()
    assert card_data["name"] == "Wesley", card_data
    assert card_data["stub"] == "wesley", card_data
    card = session.query(Card).filter(Card.stub == "wesley").first()
    assert card.search_text.startswith("Wesley"), card.search_text


def test_patch_card_search_keywords(client: TestClient, session: db.Session):
    """Editing the search keywords must update the search text"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-phoenixborn",
        json={"search_keywords": "nonesuch"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    card = session.query(Card).filter(Card.stub == "example-phoenixborn").first()
    assert card.search_text.startswith("Example Phoenixborn nonesuch"), card.search_text


def test_patch_card_text(client: TestClient, session: db.Session):
    """Modifying the text must update the card text"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-phoenixborn",
        json={"text": "Whatever"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["text"] == "Whatever"


def test_patch_card_remove_text(client: TestClient, session: db.Session):
    """Removing the card text must delete the property"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-phoenixborn",
        json={"text": ""},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert "text" not in response.json(), response.json()


def test_patch_card_copies(client: TestClient, session: db.Session):
    """Modifying card copies must update both JSON and Card"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-conjuration",
        json={"copies": 17},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["copies"] == 17
    card = session.query(Card).filter(Card.stub == "example-conjuration").first()
    assert card.copies == 17


def test_patch_card_copies_removal(client: TestClient, session: db.Session):
    """Removing card copies must update both JSON and card"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-conjuration",
        json={"copies": 0},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert "copies" not in response.json(), response.json()
    card = session.query(Card).filter(Card.stub == "example-conjuration").first()
    assert card.copies is None


def test_patch_card_cost(client: TestClient, session: db.Session):
    """Updating costs updates weight, JSON, and magic cost"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-ally",
        json={"cost": ["[[main]]", "1 [[natural:class]]"]},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    card = session.query(Card).filter(Card.stub == "example-ally").first()
    assert card.cost_weight == 106
    card_data = response.json()
    assert card_data["cost"] == ["[[main]]", "1 [[natural:class]]"], card_data
    assert card_data["magicCost"] == {"natural:class": 1}


def test_patch_card_dice(client: TestClient, session: db.Session):
    """Updating dice modifies the flags, as well"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-ally",
        json={"dice": ["illusion"]},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["dice"] == ["illusion"]
    card = session.query(Card).filter(Card.stub == "example-ally").first()
    assert card.dice_flags == 4


def test_patch_card_dice_removal(client: TestClient, session: db.Session):
    """Removing dice removes from both flags and JSON"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-ally",
        json={"dice": []},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert "dice" not in response.json(), response.json()
    card = session.query(Card).filter(Card.stub == "example-ally").first()
    assert card.dice_flags == 0


def test_patch_card_alt_dice(client: TestClient, session: db.Session):
    """Updating alt dice modifies the flags, as well"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-ally",
        json={"altDice": ["illusion"]},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["altDice"] == ["illusion"]
    card = session.query(Card).filter(Card.stub == "example-ally").first()
    assert card.alt_dice_flags == 4


def test_patch_card_alt_dice_removal(client: TestClient, session: db.Session):
    """Removing dice removes from both flags and JSON"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-ally",
        json={"altDice": []},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert "altDice" not in response.json(), response.json()
    card = session.query(Card).filter(Card.stub == "example-ally").first()
    assert card.alt_dice_flags == 0


def test_patch_cards_magic_costs(client: TestClient, session: db.Session):
    """Updating magic costs updates the JSON"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-ally",
        json={"magicCost": {"natural:power": 1}},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["magicCost"] == {"natural:power": 1}


def test_patch_cards_magic_costs_removal(client: TestClient, session: db.Session):
    """Removing magic costs updates the JSON"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-ally",
        json={"magicCost": {}},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert "magicCost" not in response.json()


def test_patch_card_stats(client: TestClient, session: db.Session):
    """Updating the card's stat values works"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-conjuration",
        json={"attack": "5", "life": 10},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    card_data = response.json()
    assert card_data["attack"] == 5, card_data
    assert card_data["life"] == 10, card_data


def test_patch_card_stat_removal(client: TestClient, session: db.Session):
    """Removing stat values works"""
    admin, token = create_admin_token(session)
    response = client.patch(
        "/v2/cards/example-conjuration",
        json={"attack": ""},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert "attack" not in response.json(), response.json()

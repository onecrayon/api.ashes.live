from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy import select

from api import db
from api.models.release import Release, UserRelease
from api.services.card import create_card

from ..utils import create_user_token


def names_from_results(response):
    """Returns card names from results as a list"""
    return [x["name"] for x in response.json()["results"]]


def test_card_filters_legacy(client: TestClient, session: db.Session):
    """Legacy cards must only be shown when requested"""
    # Listing endpoint only includes legacy cards when requesting legacy cards
    response = client.get("/v2/cards", params={"show_legacy": True})
    assert response.status_code == status.HTTP_200_OK, response.json()
    # There are 9 different types of cards in our fake card database
    assert len(response.json()["results"]) == 10, names_from_results(response)


def test_card_filters(client: TestClient, session: db.Session):
    """Non-legacy cards must return by default"""
    # And request non-legacy cards
    response = client.get("/v2/cards")
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 10, names_from_results(response)


def test_card_filters_query(client: TestClient, session: db.Session):
    """Filtering by query string must search properly"""
    # Filtering by query works; there are two cards with the word "stuff" in their text
    response = client.get("/v2/cards", params={"q": "stuff"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 2, names_from_results(response)
    # And two with the word "alteration" in their title, and one with "alteration" in its text
    response = client.get("/v2/cards", params={"q": "alteration"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 3, names_from_results(response)


def test_card_filters_card_type(client: TestClient, session: db.Session):
    """Filtering by card type must be accurate"""
    # Filtering by card type works
    response = client.get(
        "/v2/cards", params={"types": ["alteration_spell", "ready_spell"]}
    )
    assert response.status_code == status.HTTP_200_OK, response.json()
    # There are three cards: two ready spells, one alteration spell, and one conjured alteration spell
    assert len(response.json()["results"]) == 4, names_from_results(response)
    # Filtering by "conjurations" shortcut works
    response = client.get("/v2/cards", params={"types": "conjurations"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 3, names_from_results(response)


def test_card_filters_deckbuilder_mode(client: TestClient, session: db.Session):
    """Deckbuilder mode must filter out Phoenixborn, their uniques, and conjurations"""
    # Exclude Phoenixborn, their uniques, and conjurations in "deckbuilder" mode
    response = client.get("/v2/cards", params={"mode": "deckbuilder"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 5, names_from_results(response)


def test_card_filters_summons(client: TestClient, session: db.Session):
    """Filtering by summons must only return "summon" cards"""
    # Show only "summon" cards if requested
    response = client.get("/v2/cards", params={"show_summons": True})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 1, names_from_results(response)


def test_card_filters_basic_cost(client: TestClient, session: db.Session):
    """Filtering by basic costs must not return any cards with non-basic costs"""
    # Show only cards with basic costs
    response = client.get("/v2/cards", params={"dice": "basic"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    # There are two cards that require basic or no costs: the ready spell and alteration
    #  (conjurations are intentionally excluded)
    assert len(response.json()["results"]) == 2, names_from_results(response)


def test_card_filters_dice_costs(client: TestClient, session: db.Session):
    """Must show cards that have either specified dice costs, but no other cards"""
    # Show only cards with ceremonial or charm costs
    response = client.get("/v2/cards", params={"dice": ["ceremonial", "charm"]})
    assert response.status_code == status.HTTP_200_OK, response.json()
    # There are two cards that require ceremonial or charm: summon spell and reaction
    assert len(response.json()["results"]) == 2, names_from_results(response)


def test_card_filters_dice_costs_all(client: TestClient, session: db.Session):
    """Must show cards that have all specified dice costs"""
    # Show only cards that require natural AND illusion
    response = client.get(
        "/v2/cards", params={"dice": ["natural", "illusion"], "dice_logic": "all"}
    )
    assert response.status_code == status.HTTP_200_OK, response.json()
    # Only the Ally requires both these colors
    assert len(response.json()["results"]) == 1, names_from_results(response)


def test_card_filters_dice_costs_includes(client: TestClient, session: db.Session):
    """Must show cars that have at least one of the specified dice costs"""
    response = client.get(
        "/v2/cards", params={"dice": ["natural", "illusion"], "dice_logic": "includes"}
    )
    assert response.status_code == status.HTTP_200_OK, response.json()
    # The Ally and the Phoenixborn requires one or more of these colors
    assert len(response.json()["results"]) == 2, names_from_results(response)


def test_card_filters_deckbuilder_with_uniques(client: TestClient, session: db.Session):
    """Must include uniques when a Phoenixborn is specified in deckbuilder mode"""
    # Include Phoenixborn uniques in deckbuilder mode
    response = client.get(
        "/v2/cards",
        params={"mode": "deckbuilder", "include_uniques_for": "Example Phoenixborn"},
    )
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 6, names_from_results(response)


def test_card_filters_sort(client: TestClient, session: db.Session):
    """Must sort by name by default"""
    # Sort by name (default)
    response = client.get("/v2/cards")
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert (
        response.json()["results"][0]["name"] == "Example Action"
    ), names_from_results(response)


def test_card_filters_order_desc(client: TestClient, session: db.Session):
    """Must allow ordering in descending order"""
    # Sort in descending order
    response = client.get("/v2/cards", params={"order": "desc"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert (
        response.json()["results"][0]["name"] == "Summon Example Conjuration"
    ), names_from_results(response)


def test_card_filters_sort_type(client: TestClient, session: db.Session):
    """Must allow sorting by type"""
    # Sort by type (uses the front-end ordering logic, so Phoenixborn => Ready Spells => others)
    response = client.get("/v2/cards", params={"sort": "type"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert (
        response.json()["results"][0]["name"] == "Example Phoenixborn"
    ), names_from_results(response)


def test_card_filters_sort_cost(client: TestClient, session: db.Session):
    """Must allow sorting by cost"""
    # Sort by cost (excluding things without a cost)
    response = client.get("/v2/cards", params={"sort": "cost", "mode": "deckbuilder"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert (
        response.json()["results"][0]["name"] == "Example Ready Spell"
    ), names_from_results(response)


def test_card_filters_sort_dice(client: TestClient, session: db.Session):
    """Must allow sorting by dice"""
    # Sort by dice (for action and reaction); should have basic, then ceremonial, etc.
    response = client.get(
        "/v2/cards",
        params={"sort": "dice", "types": ["action_spell", "reaction_spell"]},
    )
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert (
        response.json()["results"][0]["name"] == "Example Reaction"
    ), names_from_results(response)

    # Sorts by release, then type weight, then name; since we're doing a descending sort the first
    #  item should be the reaction spell from the expansion release
    response = client.get("/v2/cards", params={"sort": "release", "order": "desc"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert (
        response.json()["results"][0]["name"] == "Example Reaction"
    ), names_from_results(response)


def test_pagination_none(client: TestClient, session: db.Session):
    """Returning all results works as expected."""
    # Verify that we have ten items and they all come back by default
    response = client.get("/v2/cards")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 10
    assert len(data["results"]) == 10
    assert data["previous"] is None
    assert data["next"] is None


def test_pagination_paging(client: TestClient, session: db.Session):
    """Paging through results works as expected"""
    # Verify that we can page through things properly
    response = client.get("/v2/cards", params={"offset": 3, "limit": 3})
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 10
    assert len(data["results"]) == 3
    assert data["previous"] is not None
    assert data["next"] is not None


def test_pagination_negative_offsets(client: TestClient, session: db.Session):
    """A number that would result in a negative offset must result in no offset"""
    # Verify that previous links work properly with arbitrary offsets that would make them negative
    response = client.get("/v2/cards", params={"offset": 2, "limit": 3})
    assert response.status_code == 200
    data = response.json()
    assert "offset=" not in data["previous"]


def test_release_filtration(client: TestClient, session: db.Session):
    """Filtering cards by owned releases works properly."""
    # Create our user, and setup their collection
    user, token = create_user_token(session)
    master_set = session.execute(
        select(Release).where(Release.stub == "master-set").limit(1)
    ).scalar()
    user_release = UserRelease(user_id=user.id, release_id=master_set.id)
    session.add(user_release)
    session.commit()

    # Verify that the filter works
    response = client.get(
        "/v2/cards",
        params={"releases": "mine"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200, response.json()
    assert len(response.json()["results"]) == 7, response.json()


def test_release_filtration_specific_release(client: TestClient, session: db.Session):
    """Filtering by a specific release works properly"""
    response = client.get("/v2/cards", params={"r": ["first-expansion"]})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()["results"]) == 3, response.json()


def test_phg_release_filtration(client: TestClient, session: db.Session):
    """Must be able to filter for only PHG release when looking at legacy cards."""
    release = Release(name="PHG")
    release.is_public = True
    release.is_legacy = True
    release.is_phg = True
    session.add(release)
    fan_release = Release(name="Fan")
    fan_release.is_public = True
    fan_release.is_legacy = True
    session.add(fan_release)
    session.commit()
    phg_card = create_card(
        session,
        name="A",
        card_type="Action Spell",
        placement="Discard",
        release=release,
        text="Text.",
    )
    fan_card = create_card(
        session,
        name="B",
        card_type="Action Spell",
        placement="Discard",
        release=fan_release,
        text="Text.",
    )
    phg_card.is_legacy = True
    fan_card.is_legacy = True
    session.commit()

    response = client.get("/v2/cards", params={"show_legacy": True, "releases": "phg"})
    assert response.status_code == 200
    assert len(response.json()["results"]) == 1, response.json()

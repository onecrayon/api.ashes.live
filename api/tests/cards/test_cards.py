from functools import partial

from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models.release import Release, UserRelease
from api.services.card import create_card
from ..utils import create_card_database, create_user_token


def names_from_results(response):
    """Returns card names from results as a list"""
    return [x["name"] for x in response.json()["results"]]


def test_card_filters(client: TestClient, session: db.Session):
    """Filters properly filter out cards."""
    # I'm generally not a fan of really big methods that test a bunch of different stuff, but in
    #  this instance, creating the card database contents is a query-heavy operation that really
    #  slows things down, so we're testing every filter for card listings in the same method.
    create_card_database(session, is_legacy=True)
    create_card_database(session)

    # Setup our common request pattern
    request = partial(client.get, url="/v2/cards")

    # Listing endpoint only includes legacy cards when requesting legacy cards
    response = request(params={"show_legacy": True})
    assert response.status_code == status.HTTP_200_OK, response.json()
    # There are 9 different types of cards in our fake card database
    assert len(response.json()["results"]) == 9, names_from_results(response)
    # And request non-legacy cards
    response = request()
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 9, names_from_results(response)

    # Filtering by query works; there are two cards with the word "stuff" in their text
    response = request(params={"q": "stuff"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 2, names_from_results(response)
    # And two with the word "alteration" in their title, and one with "alteration" in its text
    response = request(params={"q": "alteration"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 3, names_from_results(response)

    # Filtering by card type works
    response = request(params={"types": ["alteration_spell", "ready_spell"]})
    assert response.status_code == status.HTTP_200_OK, response.json()
    # There are three cards: two ready spells, and one alteration spell
    assert len(response.json()["results"]) == 3, names_from_results(response)
    # Filtering by "conjurations" shortcut works
    response = request(params={"types": "conjurations"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 2, names_from_results(response)

    # Exclude Phoenixborn, their uniques, and conjurations in "deckbuilder" mode
    response = request(params={"mode": "deckbuilder"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 5, names_from_results(response)

    # Show only "summon" cards if requested
    response = request(params={"show_summons": True})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 1, names_from_results(response)

    # Show only cards with basic costs
    response = request(params={"dice": "basic"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    # There are four cards that require basic or no costs: ready spell, alteration, and both conjurations
    assert len(response.json()["results"]) == 4, names_from_results(response)

    # Show only cards with ceremonial or charm costs
    response = request(params={"dice": ["ceremonial", "charm"]})
    assert response.status_code == status.HTTP_200_OK, response.json()
    # There are two cards that require ceremonial or charm: summon spell and reaction
    assert len(response.json()["results"]) == 2, names_from_results(response)

    # Show only cards that require natural AND illusion
    response = request(params={"dice": ["natural", "illusion"], "dice_logic": "all"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    # Only the Ally requires both these colors
    assert len(response.json()["results"]) == 1, names_from_results(response)

    # Include Phoenixborn uniques in deckbuilder mode
    response = request(
        params={"mode": "deckbuilder", "include_uniques_for": "Example Phoenixborn"}
    )
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert len(response.json()["results"]) == 6, names_from_results(response)

    # Sort by name (default)
    response = request()
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert (
        response.json()["results"][0]["name"] == "Example Action"
    ), names_from_results(response)
    # Sort in descending order
    response = request(params={"order": "desc"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert (
        response.json()["results"][0]["name"] == "Summon Example Conjuration"
    ), names_from_results(response)

    # Sort by type (alphabetical)
    response = request(params={"sort": "type"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert (
        response.json()["results"][0]["name"] == "Example Action"
    ), names_from_results(response)

    # Sort by cost (excluding things without a cost)
    response = request(params={"sort": "cost", "mode": "deckbuilder"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert (
        response.json()["results"][0]["name"] == "Example Ready Spell"
    ), names_from_results(response)

    # Sort by dice (for action and reaction); should have basic, then ceremonial, etc.
    response = request(
        params={"sort": "dice", "types": ["action_spell", "reaction_spell"]}
    )
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert (
        response.json()["results"][0]["name"] == "Example Reaction"
    ), names_from_results(response)


def test_pagination(client: TestClient, session: db.Session):
    """Pagination logic works as expected."""
    # We don't need real cards to test, we just need a known quantity that sorts predictably
    release = Release(name="Example")
    release.is_public = True
    session.add(release)
    session.commit()
    for letter in "ABCDEFGHIJ":
        create_card(
            session,
            **{
                "name": letter,
                "card_type": "Action Spell",
                "placement": "Discard",
                "release": release,
                "text": "Text.",
            },
        )
    # Verify that we have ten items and they all come back by default
    response = client.get("/v2/cards")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 10
    assert len(data["results"]) == 10
    assert data["previous"] is None
    assert data["next"] is None

    # Verify that we can page through things properly
    response = client.get("/v2/cards", params={"offset": 3, "limit": 3})
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 10
    assert len(data["results"]) == 3
    assert data["previous"] is not None
    assert data["next"] is not None

    # Verify that previous links work properly with arbitrary offsets that would make them negative
    response = client.get("/v2/cards", params={"offset": 2, "limit": 3})
    assert response.status_code == 200
    data = response.json()
    assert "offset=" not in data["previous"]


def test_release_filtration(client: TestClient, session: db.Session):
    """Filtering cards by owned releases works properly."""
    # Create a pair of releases with an associated card each
    release_1 = Release(name="First")
    release_1.is_public = True
    session.add(release_1)
    release_2 = Release(name="Second")
    release_2.is_public = True
    session.add(release_2)
    session.commit()
    create_card(
        session,
        name="A",
        card_type="Action Spell",
        placement="Discard",
        release=release_1,
        text="Text.",
    )
    create_card(
        session,
        name="B",
        card_type="Action Spell",
        placement="Discard",
        release=release_2,
        text="Text.",
    )

    # Create our user, and setup their collection
    user, token = create_user_token(session)
    user_release = UserRelease(user_id=user.id, release_id=release_1.id)
    session.add(user_release)
    session.commit()

    # Verify that the filter works
    response = client.get(
        "/v2/cards",
        params={"releases": "mine"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200, response.json()
    assert len(response.json()["results"]) == 1, response.json()


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

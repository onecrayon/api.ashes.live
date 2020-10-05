from functools import partial

from fastapi import status
from fastapi.testclient import TestClient

from api import db
from ..utils import create_card_database, create_admin_token


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


# TODO: test filtering by owned collection for logged-in user
# TODO: test filtering for "phg" releases for legacy cards only
# TODO: test pagination handling

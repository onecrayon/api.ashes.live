from functools import partial

from fastapi import status
from fastapi.testclient import TestClient

from api import db, models
from api.models.release import Release, UserRelease
from api.services.card import create_card

from ..utils import create_user_token


def names_from_results(response):
    """Returns card names from results as a list"""
    return [x["name"] for x in response.json()["results"]]


def _create_cards_for_filtration(session: db.Session, is_legacy=False):
    """Populates database with a minimum viable list of one of each card type"""
    # First create our two releases
    master_set = models.Release("Master Set")
    master_set.is_legacy = is_legacy
    master_set.is_public = True
    expansion = models.Release("First Expansion")
    expansion.is_legacy = is_legacy
    expansion.is_public = True
    session.add(master_set)
    session.add(expansion)
    session.commit()
    # Then create one of every type of card, with a mixture of all the different things that can be
    #  included to ensure that the automatic dice sorting and so forth works properly
    card_dicts = [
        {
            "name": "Example Conjuration",
            "card_type": "Conjuration",
            "placement": "Battlefield",
            "release": master_set,
            "attack": 0,
            "life": 2,
            "recover": 0,
            "copies": 3,
        },
        {
            "name": "Example Conjured Alteration",
            "card_type": "Conjured Alteration Spell",
            "placement": "Unit",
            "phoenixborn": "Example Phoenixborn",
            "release": master_set,
            "text": "Whoops: 1 [[basic]] - 1 [[discard]]: Discard this spell.",
            "effect_magic_cost": "1 [[basic]]",
            "attack": "-2",
            "copies": 2,
        },
        {
            "name": "Example Phoenixborn",
            "card_type": "Phoenixborn",
            "release": master_set,
            "text": "Mess With Them: [[main]] - 1 [[illusion:class]]: Place a [[Example Conjured Alteration]] conjured alteration spell on opponent's unit.",
            "effect_magic_cost": "1 [[illusion:class]]",
            "battlefield": 5,
            "life": 16,
            "spellboard": 4,
            "can_effect_repeat": True,
        },
        {
            "name": "Summon Example Conjuration",
            "card_type": "Ready Spell",
            "placement": "Spellboard",
            "release": master_set,
            "cost": "[[main]] - 1 [[basic]] - [[side]] / 1 [[discard]]",
            "text": "1 [[charm:class]]: Place a [[Example Conjuration]] conjuration on your battlefield.",
            "effect_magic_cost": ["1 [[charm:class]]"],
        },
        {
            "name": "Example Ally",
            "card_type": "Ally",
            "placement": "Battlefield",
            "phoenixborn": "Example Phoenixborn",
            "release": master_set,
            "cost": ["[[main]]", ["1 [[natural:power", "1 [[illusion:power]]"]],
            "text": "Stuffiness: [[main]] - [[exhaust]] - 1 [[natural:class]] / 1 [[illusion:class]]: Do stuff.",
            "effect_magic_cost": "1 [[natural:class]] / 1 [[illusion:class]]",
            "attack": 2,
            "life": 1,
            "recover": 1,
        },
        {
            "name": "Example Alteration",
            "card_type": "Alteration Spell",
            "placement": "Unit",
            "release": master_set,
            "cost": "[[side]] - 1 [[basic]] - 1 [[discard]]",
            "attack": "+2",
            "recover": "-1",
        },
        {
            "name": "Example Ready Spell",
            "card_type": "Ready Spell",
            "placement": "Spellboard",
            "release": expansion,
            "cost": "[[side]]",
            "text": "[[main]] - [[exhaust]]: Do more things.",
        },
        {
            "name": "Example Action",
            "card_type": "Action Spell",
            "placement": "Discard",
            "release": expansion,
            "cost": "[[main]] - 1 [[time:power]] - 1 [[basic]]",
            "text": "If you spent a [[sympathy:power]] to pay for this card, do more stuff.",
            "alt_dice": ["sympathy"],
        },
        {
            "name": "Example Reaction",
            "card_type": "Reaction Spell",
            "placement": "Discard",
            "release": expansion,
            "cost": "1 [[divine:class]] / 1 [[ceremonial:class]]",
            "text": "Do a happy dance.",
        },
    ]
    cards = []
    # Create our cards
    for card_dict in card_dicts:
        cards.append(create_card(session, **card_dict))
    if is_legacy:
        for card in cards:
            card.is_legacy = True
        session.commit()


def test_card_filters(client: TestClient, session: db.Session):
    """Filters properly filter out cards."""
    # I'm generally not a fan of really big methods that test a bunch of different stuff, but in
    #  this instance, creating the card database contents is a query-heavy operation that really
    #  slows things down, so we're testing every filter for card listings in the same method.
    _create_cards_for_filtration(session, is_legacy=True)
    _create_cards_for_filtration(session)

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

    # Sort by type (uses the front-end ordering logic, so Phoenixborn => Ready Spells => others)
    response = request(params={"sort": "type"})
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert (
        response.json()["results"][0]["name"] == "Example Phoenixborn"
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

    # Sorts by release, then type weight, then name; since we're doing a descending sort the first
    #  item should be the reaction spell from the expansion release
    response = request(params={"sort": "release", "order": "desc"})
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
    assert response.status_code == status.HTTP_200_OK, response.json()
    data = response.json()
    assert len(data["results"]) == 1, response.json()
    assert data["results"][0]["name"] == "A"

    # Verify that the `r` release filter works
    response = client.get("/v2/cards", params={"r": ["second"]})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data["results"]) == 1, response.json()
    assert data["results"][0]["name"] == "B"


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

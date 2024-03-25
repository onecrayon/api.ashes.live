import pytest

from api import db, models
from api.db import Session
from api.services.card import create_card


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
            "name": "Example Ally Conjuration",
            "card_type": "Conjuration",
            "placement": "Battlefield",
            "phoenixborn": "Example Phoenixborn",
            "release": master_set,
            "attack": 2,
            "life": 1,
            "recover": 0,
            "copies": 2,
        },
        {
            "name": "Example Ally",
            "card_type": "Ally",
            "placement": "Battlefield",
            "phoenixborn": "Example Phoenixborn",
            "release": master_set,
            "cost": ["[[main]]", ["1 [[natural:power", "1 [[illusion:power]]"]],
            "text": "Stuffiness: [[main]] - [[exhaust]] - 1 [[natural:class]] / 1 [[illusion:class]]: Place a [[Example Ally Conjuration]] conjuration on your battlefield.",
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
            # This is normally handled by a migration, since legacy cards can't be added
            card.json["release"]["is_legacy"] = True
            card.json["is_legacy"] = True
            db.flag_modified(card, "json")
        session.commit()


@pytest.fixture(scope="package")
def cards_session(session_local: Session, monkeypatch_package) -> Session:
    """Populate our database with the cards needed for listing tests.

    This causes our session to be reused between all tests in this package.
    """
    # Creates a nested transaction that includes standard card data
    session = session_local()
    session.begin_nested()
    # Overwrite commits with flushes so that we can query stuff, but it's in the same transaction
    monkeypatch_package.setattr(session, "commit", session.flush)
    _create_cards_for_filtration(session, is_legacy=True)
    _create_cards_for_filtration(session)
    try:
        yield session
    finally:
        session.rollback()
        session.close()


@pytest.fixture(scope="function")
def session(cards_session):
    """Return a nested transaction on the outer session, to prevent rolling back card data"""
    cards_session.begin_nested()
    try:
        yield cards_session
    finally:
        cards_session.rollback()

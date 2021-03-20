from api import db, models
from api.services.card import create_card


def populate_cards_for_decks(session: db.Session):
    """This utility function populates a set of cards appropriate for testing deck building"""
    # First create our two releases
    master_set = models.Release("Master Set")
    master_set.is_public = True
    expansion = models.Release("First Expansion")
    expansion.is_public = True
    session.add(master_set)
    session.add(expansion)
    session.commit()
    # Then create two Phoenixborns (with uniques), and 18 other cards spanning all card types
    #  (to ensure that we can filter by release, preconstructed decks, etc.)
    card_dicts = [
        {
            "name": "One Phoenixborn",
            "card_type": "Phoenixborn",
            "release": master_set,
            "text": "Command Strike: [[side]] - 2 [[basic]]: Do stuff.",
            "effect_magic_cost": "2 [[basic]]",
            "battlefield": 4,
            "life": 20,
            "spellboard": 5,
        },
        {
            "name": "One Conjuration A",
            "card_type": "Conjuration",
            "release": master_set,
            "placement": "Battlefield",
            "text": "* Consume: Do stuff.",
            "life": 4,
            "attack": "X",
            "copies": 1,
            "recover": 3,
            "phoenixborn": "One Phoenixborn",
        },
        {
            "name": "Summon One Conjuration A",
            "card_type": "Ready Spell",
            "release": master_set,
            "placement": "Spellboard",
            "cost": ["[[main]]"],
            "text": "[[main]] - [[exhaust]] - 1 [[charm:power]] - 1 [[natural:power]]: Place a [[One Conjuration A]] conjuration onto your battlefield.",
            "phoenixborn": "One Phoenixborn",
        },
        {
            "name": "One Conjuration B",
            "card_type": "Conjuration",
            "release": master_set,
            "placement": "Battlefield",
            "text": "Unit Guard: Do stuff.",
            "attack": 0,
            "life": 2,
            "recover": 0,
            "copies": 2,
        },
        {
            "name": "Summon One Conjuration B",
            "card_type": "Ready Spell",
            "release": master_set,
            "placement": "Spellboard",
            "cost": ["[[main]]", "1 [[charm:class]]"],
            "text": "[[main]] - [[exhaust]] - 1 [[natural:class]]: Place a [[One Conjuration B]] conjuration onto your battlefield.",
        },
        # TODO: LEFT OFF converting Maeoni and I think maybe Rin's decks to JSON
    ]
    # Create our cards
    for card_dict in card_dicts:
        create_card(session, **card_dict)

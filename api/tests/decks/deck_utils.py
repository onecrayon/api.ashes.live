from typing import List

from sqlalchemy import func

from api import db
from api.models import Card, Deck, Release, User
from api.services.card import create_card
from api.services.deck import create_or_update_deck
from api.tests.utils import generate_random_chars


def create_cards_for_decks(session: db.Session):
    """This utility function populates a set of cards appropriate for testing deck building"""
    # First create our two releases
    master_set = Release("Master Set")
    master_set.is_public = True
    expansion = Release("Expansion")
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
        {
            "name": "One Ready Spell A",
            "card_type": "Ready Spell",
            "release": master_set,
            "placement": "Spellboard",
            "cost": ["[[main]]"],
            "text": "[[side]] - [[exhaust]] - 2 [[charm:class]]: Do stuff.",
        },
        {
            "name": "One Ready Spell B",
            "card_type": "Ready Spell",
            "release": master_set,
            "placement": "Spellboard",
            "cost": ["[[side]]", "1 [[basic]]"],
            "text": "[[main]] - [[exhaust]] - 1 [[natural:class]] or 1 [[sympathy:class]]: Do stuff.",
        },
        {
            "name": "One Action Spell A",
            "card_type": "Action Spell",
            "release": master_set,
            "placement": "Discard",
            "cost": ["[[main]]", "2 [[natural:power]]"],
            "text": "Do stuff.",
        },
        {
            "name": "One Action Spell B",
            "card_type": "Action Spell",
            "release": master_set,
            "placement": "Discard",
            "cost": ["[[main]]", "1 [[charm:class]]", "1 [[basic]]"],
            "text": "Do stuff.",
        },
        {
            "name": "One Action Spell C",
            "card_type": "Action Spell",
            "release": master_set,
            "placement": "Discard",
            "cost": ["[[main]]", "1 [[charm:class]]", "1 [[basic]]"],
            "text": "Do stuff.",
        },
        {
            "name": "One Reaction Spell",
            "card_type": "Reaction Spell",
            "release": master_set,
            "placement": "Discard",
            "cost": ["1 [[charm:power]]"],
            "text": "You may play this spell after an opponent targets a unit you control with a spell, ability, or dice power. Do stuff.",
        },
        {
            "name": "One Alteration Spell",
            "card_type": "Alteration Spell",
            "release": master_set,
            "placement": "Unit",
            "cost": ["[[side]]", "1 [[natural:class]]"],
            "text": "This unit now has the following ability:\n\n* Armored 1: Do stuff.",
            "life": "+1",
        },
        {
            "name": "One Ally",
            "card_type": "Ally",
            "release": master_set,
            "placement": "Battlefield",
            "cost": ["[[main]]", "1 [[charm:class]]"],
            "text": "Song of Sorrow: [[side]] - [[exhaust]]: Do stuff.",
            "attack": 1,
            "life": 1,
            "recover": 1,
        },
        # And define cards for a single expansion
        {
            "name": "Two Conjured Alteration Spell",
            "card_type": "Conjured Alteration Spell",
            "release": expansion,
            "placement": "Unit",
            "life": "+1",
            "copies": 5,
            "phoenixborn": "Two Phoenixborn",
        },
        {
            "name": "Two Phoenixborn",
            "text": "Ice Buff: [[side]] - [[exhaust]]: Attach an [[Two Conjured Alteration Spell]] conjured alteration spell to a target unit you control.",
            "card_type": "Phoenixborn",
            "release": expansion,
            "battlefield": 6,
            "life": 17,
            "spellboard": 4,
        },
        {
            "name": "Two's Reaction Spell",
            "card_type": "Reaction Spell",
            "release": expansion,
            "placement": "Discard",
            "cost": ["2 [[basic]]"],
            "text": "You may play this spell after a unit you control is dealt damage by a unit's attack. Prevent that damage from being received. Destroy that target attacking unit.",
            "phoenixborn": "Two Phoenixborn",
        },
        {
            "name": "Two Conjuration A",
            "card_type": "Conjuration",
            "release": expansion,
            "placement": "Battlefield",
            "text": "* Skin Morph 2: Do stuff.",
            "attack": 3,
            "life": 2,
            "recover": 0,
            "copies": 3,
        },
        {
            "name": "Summon Two Conjuration A",
            "card_type": "Ready Spell",
            "release": expansion,
            "placement": "Spellboard",
            "cost": ["[[main]]"],
            "text": "[[main]] - [[exhaust]] - 2 [[natural:class]] - 1 [[basic]]: Place an [[Two Conjuration A]] conjuration onto your battlefield.\n\nFocus 2: Do stuff.",
        },
        {
            "name": "Two Conjuration D",
            "card_type": "Conjuration",
            "release": expansion,
            "placement": "Battlefield",
            "text": "* Inheritance 1: Do stuff.",
            "attack": 3,
            "life": 2,
            "recover": 0,
            "copies": 6,
        },
        {
            "name": "Two Conjuration C",
            "card_type": "Conjuration",
            "release": expansion,
            "placement": "Battlefield",
            "text": "Blossom: [[main]]: Place up to 2 [[Two Conjuration D]] conjurations onto your battlefield.",
            "attack": 0,
            "life": 2,
            "recover": 0,
            "copies": 3,
        },
        {
            "name": "Two Conjuration B",
            "card_type": "Conjuration",
            "release": expansion,
            "placement": "Battlefield",
            "text": "* Germinate: When this unit is destroyed, place a [[Two Conjuration C]] conjuration onto your battlefield.",
            "attack": 2,
            "life": 1,
            "recover": 0,
            "copies": 3,
        },
        {
            "name": "Summon Two Conjuration B",
            "card_type": "Ready Spell",
            "release": expansion,
            "placement": "Spellboard",
            "cost": ["[[main]]"],
            "text": "[[main]] - [[exhaust]] - 1 [[natural:class]] - 1 [[sympathy:class]]: Place an [[Two Conjuration B]] conjuration onto your battlefield.\n\nFocus 1: Do stuff.",
        },
        {
            "name": "Two Ready Spell",
            "card_type": "Ready Spell",
            "release": expansion,
            "placement": "Spellboard",
            "cost": ["[[main]]"],
            "text": "[[main]] - [[exhaust]] - 1 [[natural:class]]: Do stuff.",
        },
        {
            "name": "Two Reaction Spell",
            "card_type": "Reaction Spell",
            "release": expansion,
            "placement": "Discard",
            "cost": ["1 [[natural:class]]"],
            "text": "You may play this spell after a unit with a life value of 2 or less comes into play. Destroy that target unit.",
        },
        {
            "name": "Two Alteration Spell",
            "card_type": "Alteration Spell",
            "release": expansion,
            "placement": "Unit",
            "cost": ["[[main]]", "1 [[natural:class]]"],
            "text": "* When attaching this spell, place 3 status tokens on this spell. Discard this spell when it no longer has any status tokens on it. As long as this spell is attached to this unit, this unit is considered to be exhausted. This unit now has the following ability:\n\n* Thaw: [[side]]: Remove 1 status token from a Deep Freeze alteration spell attached to this unit.",
        },
        {
            "name": "Two Action Spell",
            "card_type": "Action Spell",
            "release": expansion,
            "placement": "Discard",
            "cost": ["[[main]]", "2 [[natural:class]]"],
            "text": "Deal 2 damage to a target unit. Remove 2 status tokens from that unit.",
        },
        {
            "name": "Two Ally A",
            "card_type": "Ally",
            "release": expansion,
            "placement": "Battlefield",
            "cost": ["[[main]]", "2 [[natural:class]]"],
            "text": "* Armored 1: After this unit is dealt damage, prevent 1 damage from being received.",
            "attack": 3,
            "life": 1,
            "recover": 1,
        },
        {
            "name": "Two Ally B",
            "card_type": "Ally",
            "release": expansion,
            "placement": "Battlefield",
            "cost": ["[[main]]", "1 [[sympathy:class]]", "1 [[basic]]"],
            "text": "* Last Orders 1: When this unit is destroyed, you may spend 1 [[basic]] to do stuff.\n\n* Inheritance 1: Do stuff.",
            "attack": 2,
            "life": 2,
            "recover": 1,
        },
        {
            "name": "Two Ally C",
            "card_type": "Ally",
            "release": expansion,
            "placement": "Battlefield",
            "cost": ["[[main]]", "2 [[natural:class]]"],
            "text": "Slumbering 1: Do stuff.",
            "attack": 4,
            "life": 4,
            "recover": 2,
        },
    ]
    # Create our cards
    for card_dict in card_dicts:
        create_card(session, **card_dict)


def create_deck_for_user(
    session: db.Session, user: User, release_stub: str = None
) -> Deck:
    """Creates a deck by collecting a random Phoenixborn, their unique, and 9 random cards.

    Relies on the cards from `create_cards_for_decks()` above being in the database.

    If a release stub is included, then only cards from that release will be in the deck.

    Returns the deck object.
    """
    release: Release = (
        session.query(Release).filter(Release.stub == release_stub).first()
        if release_stub
        else None
    )
    phoenixborn_query = session.query(Card).filter(Card.card_type == "Phoenixborn")
    if release:
        phoenixborn_query = phoenixborn_query.filter(Card.release_id == release.id)
    else:
        phoenixborn_query = phoenixborn_query.order_by(func.random())
    phoenixborn: Card = phoenixborn_query.first()
    if not phoenixborn:
        raise ValueError("No such test Phoenixborn!")
    unique_card: Card = (
        session.query(Card)
        .filter(
            Card.phoenixborn == phoenixborn.name,
            Card.card_type.notin_(("Conjuration", "Conjured Alteration Spell")),
        )
        .first()
    )
    cards_query = session.query(Card).filter(
        Card.card_type.notin_(
            ("Conjuration", "Conjured Alteration Spell", "Phoenixborn")
        ),
        Card.phoenixborn.is_(None),
    )
    if release:
        cards_query = cards_query.filter(Card.release_id == release.id)
    else:
        cards_query = cards_query.order_by(func.random())
    deck_cards: List[Card] = cards_query.limit(9).all()
    card_dicts = [{"stub": x.stub, "count": 3} for x in deck_cards]
    card_dicts.append({"stub": unique_card.stub, "count": 3})
    return create_or_update_deck(
        session,
        user,
        phoenixborn=phoenixborn,
        title=generate_random_chars(),
        dice=[
            {"name": "natural", "count": 5},
            {"name": "sympathy", "count": 3},
            {"name": "charm", "count": 2},
        ],
        cards=card_dicts,
    )

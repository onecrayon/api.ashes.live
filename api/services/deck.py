from typing import List, Dict, Union

from api import db
from api.models import Deck, User, DeckDie, Release, DeckCard
from api.models.card import DiceFlags, Card
from api.schemas.cards import CardType
from api.services.stream import create_entity


class NoSuchDeck(Exception):
    """Raised when the specified deck cannot be found."""

    pass


class PhoenixbornInDeck(Exception):
    """Raised when a Phoenixborn is included in the deck card list."""

    pass


def create_or_update_deck(
    session: db.Session,
    current_user: "User",
    phoenixborn_id: int,
    deck_id: int = None,
    title: str = None,
    description: str = None,
    dice: List[Dict[str, Union[str, int]]] = None,
    cards: List[Dict[str, Union[str, int]]] = None,
) -> "Deck":
    """Creates or updates a deck in place."""
    if deck_id:
        deck = (
            session.query(Deck)
            .options(
                db.joinedload("cards"),
                db.joinedload("dice"),
                db.joinedload("selected_cards"),
            )
            .get(deck_id)
        )
        if not deck:
            raise NoSuchDeck()
        deck.title = title
        deck.description = description
        deck.phoenixborn_id = phoenixborn_id
    else:
        deck = Deck(
            entity_id=create_entity(session),
            title=title,
            description=description,
            user_id=current_user.id,
            phoenixborn_id=phoenixborn_id,
            is_snapshot=False,
            is_public=False,
        )

    # Update the dice listing
    deck_dice: List[DeckDie] = []
    total_dice = 0
    for die_dict in dice:
        die = die_dict.get("name")
        count = die_dict.get("count")
        if count:
            if total_dice + count > 10:
                count = 10 - total_dice
            if count == 0:
                break
            total_dice = total_dice + count
            deck_dice.append(DeckDie(die_flag=DiceFlags[die].value, count=count))
    deck.dice = deck_dice

    # And then the card listing
    deck_cards: List[DeckCard] = []
    card_stub_counts = {x["stub"]: x["count"] for x in cards}
    minimal_cards = (
        session.query(Card.id, Card.stub, Card.card_type)
        .join(Card.release)
        .filter(
            Card.stub.in_(card_stub_counts.keys()),
            Card.is_legacy.is_(False),
            Release.is_public == True,
        )
        .all()
    )
    for card in minimal_cards:
        count = card_stub_counts[card.stub]
        # Make sure our count can't exceed 3
        count = count if count <= 3 else 3
        # If they passed a 0 or negative count for some reason, just skip it
        if count <= 0:
            continue
        if card.card_type == CardType.phoenixborn.value:
            raise PhoenixbornInDeck()
        deck_cards.append(DeckCard(card_id=card.id, count=count))
    deck.cards = deck_cards

    # Save everything up!
    deck.selected_cards = []
    session.add(deck)
    session.commit()

    # TODO: port first five and paid effect updating logic
    return deck

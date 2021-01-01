from typing import List, Dict, Union

from api import db
from api.models import Deck, User, DeckDie, Release, DeckCard, DeckSelectedCard
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
    first_five: List[str] = None,
    effect_costs: List[str] = None,
    tutor_map: Dict[str, str] = None,
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
    card_stubs = set(card_stub_counts.keys())
    if first_five:
        card_stubs.update(first_five)
    if effect_costs:
        card_stubs.update(effect_costs)
    if tutor_map:
        card_stubs.update(tutor_map.keys())
        card_stubs.update(tutor_map.values())
    minimal_cards = (
        session.query(Card.id, Card.stub, Card.card_type)
        .join(Card.release)
        .filter(
            Card.stub.in_(card_stubs),
            Card.is_legacy.is_(False),
            Release.is_public == True,
        )
        .all()
    )
    for card in minimal_cards:
        # Minimal cards could include bogus cards thanks to first_five list and similar, so fall
        #  back to zero to ensure this is something with a count
        count = card_stub_counts.get(card.stub, 0)
        # Make sure our count can't exceed 3
        count = count if count <= 3 else 3
        # Skip it if it's not part of the deck
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

    # And finally set selected cards (first five, paid effects, and tutored cards; used for stats)
    #  This happens after clearing them out above because SQLAlchemy cannot handle the three way
    #  composite index (tries to insert duplicates instead of updating intelligently based on
    #  tutor_card_id)
    stub_to_card = {x.stub: x for x in minimal_cards}
    selected_cards: List[DeckSelectedCard] = []
    for card_stub in effect_costs:
        card = stub_to_card.get(card_stub)
        if not card:
            continue
        if card_stub not in first_five:
            selected_cards.append(
                DeckSelectedCard(card_id=card.id, is_paid_effect=True)
            )
    for card_stub in first_five:
        card = stub_to_card.get(card_stub)
        if not card:
            continue
        selected_cards.append(
            DeckSelectedCard(
                card_id=card.id,
                is_first_five=True,
                is_paid_effect=card.stub in effect_costs,
            )
        )
    for tutor_stub, card_stub in tutor_map.items():
        tutor_card = stub_to_card.get(tutor_stub)
        card = stub_to_card.get(card_stub)
        if not tutor_card or not card:
            continue
        selected_cards.append(
            DeckSelectedCard(card_id=card.id, tutor_card_id=tutor_card.id)
        )
    deck.selected_cards = selected_cards
    session.commit()

    return deck

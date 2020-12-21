from typing import List, Dict, Union

from api import db
from api.models import Deck, User
from api.services.stream import create_entity


class NoSuchDeck(Exception):
    """Raised when the specified deck cannot be found."""

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
    # TODO: Finish porting over the logic for creating and updating a deck
    return deck

from collections import defaultdict
from operator import itemgetter
from typing import Optional, List, Set, Dict

from starlette.requests import Request

from api import db
from api.models import Deck, Card, DeckCard, User, DeckDie
from api.models.card import CardConjuration
from api.schemas.pagination import PaginationOrderOptions, PaginationOptions
from api.utils.helpers import to_prefixed_tsquery
from api.utils.pagination import paginated_results_for_query


def get_decks_query(
    session: db.Session,
    show_legacy=False,
    is_public=False,
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    # Filtering options
    q: Optional[str] = None,
    phoenixborn: Optional[List[str]] = None,
    cards: Optional[List[str]] = None,
    players: Optional[List[str]] = None,
) -> db.Query:
    query = session.query(Deck).filter(Deck.is_legacy.is_(show_legacy))
    if is_public:
        deck_comp = db.aliased(Deck)
        query = query.outerjoin(
            deck_comp,
            db.and_(
                Deck.source_id == deck_comp.source_id,
                deck_comp.is_snapshot.is_(True),
                deck_comp.is_public.is_(True),
                db.or_(
                    Deck.created < deck_comp.created,
                    db.and_(Deck.created == deck_comp.created, Deck.id < deck_comp.id),
                ),
            ),
        ).filter(
            deck_comp.id.is_(None), Deck.is_snapshot.is_(True), Deck.is_public.is_(True)
        )
    if q and q.strip():
        query = query.filter(
            db.func.to_tsvector("english", db.cast(Deck.title, db.Text)).match(
                to_prefixed_tsquery(q)
            )
        )
    # Filter by Phoenixborn stubs (this is always an OR comparison between Phoenixborn)
    if phoenixborn:
        query = query.join(Card, Card.id == Deck.phoenixborn_id).filter(
            Card.stub.in_(phoenixborn)
        )
    # Filter by cards (this is always an OR comparison between cards)
    if cards:
        card_table = db.aliased(Card)
        query = (
            query.join(DeckCard, DeckCard.deck_id == Deck.id)
            .join(card_table, card_table.id == DeckCard.card_id)
            .filter(card_table.stub.in_(cards))
        )
    # Filter by player badge, and always ensure that we eagerly load the user object
    if players:
        query = (
            query.join(User, User.id == Deck.user_id)
            .filter(User.badge.in_(players))
            .options(db.contains_eager(Deck.user))
        )
    else:
        query = query.options(db.joinedload(Deck.user))
    return query.order_by(getattr(Deck.created, order)())


def add_conjurations(card_id_to_conjuration_mapping, root_card_id, conjuration_set):
    """Grabs out all necessary conjurations, updating the mapping and set by in place"""
    conjurations = card_id_to_conjuration_mapping.get(root_card_id)
    if not conjurations:
        return
    for conjuration in conjurations:
        conjuration_set.add(conjuration)
        # In the rare instance that we have a conjuration chain, we'll do a further lookup
        #  then cache the results
        if conjuration.json.get("conjurations"):
            # Trigger our implicit SQL lookup if we haven't cached it before
            if not card_id_to_conjuration_mapping.get(conjuration.id):
                card_id_to_conjuration_mapping[
                    conjuration.id
                ] = conjuration.conjurations
            add_conjurations(
                card_id_to_conjuration_mapping, conjuration.id, conjuration_set
            )


def get_conjuration_mapping(session: db.Session, card_ids: Set[int]) -> dict:
    """Gathers top-level conjurations into a mapping keyed off the root card ID"""
    conjuration_results = (
        session.query(Card, CardConjuration.card_id.label("root_card"))
        .join(CardConjuration, Card.id == CardConjuration.conjuration_id)
        .filter(CardConjuration.card_id.in_(card_ids))
        .all()
    )
    card_id_to_conjurations = defaultdict(list)
    for result in conjuration_results:
        card_id_to_conjurations[result.root_card].append(result.Card)
    return card_id_to_conjurations


def generate_deck_dict(
    deck: Deck,
    card_id_to_card: Dict[int, Card],
    card_id_to_conjurations: Dict[int, List[Card]],
    deck_cards: List[DeckCard] = None,
    deck_dice: List[DeckDie] = None,
) -> dict:
    """Formats a deck into the standard deck output dict after looking up card data beforehand.

    Requires all cards used by the deck to be looked up ahead of time and passed as the
    `card_id_to_card` mapping (ensures that we limit the number of SQL queries by preventing
    implicit lookups through SQLAlchemy).

    Similarly, requires all top-level conjurations for cards in `card_id_to_card` to be included in
    the `card_id_to_conjurations` mapping (which will be modified in place as conjuration chains are
    discovered).

    Also, all DeckCards and DeckDice must be looked up ahead of time and passed through as
    `deck_cards` and `deck_dice`, respectively.
    """
    card_output = []
    conjuration_set = set()
    if deck_cards:
        for deck_card in deck_cards:
            card = card_id_to_card[deck_card.card_id]
            card_output.append(
                {
                    "count": deck_card.count,
                    "name": card.name,
                    "stub": card.stub,
                    "type": card.card_type,
                    "phoenixborn": card.phoenixborn,
                    "is_legacy": card.is_legacy,
                }
            )
            add_conjurations(card_id_to_conjurations, card.id, conjuration_set)

    phoenixborn = card_id_to_card[deck.phoenixborn_id]
    add_conjurations(card_id_to_conjurations, phoenixborn.id, conjuration_set)
    conjuration_output = [
        {
            "count": x.copies,
            "name": x.name,
            "stub": x.stub,
            "type": x.card_type,
            "phoenixborn": x.phoenixborn,
            "is_legacy": x.is_legacy,
        }
        for x in conjuration_set
    ]

    # Compose our basic deck output dictionary
    deck_dice_dict = None
    if deck_dice:
        deck_dice_dict = [
            {
                "count": deck_die.count,
                "name": DiceFlags(deck_die.die_flag).name,
            }
            for deck_die in deck_dice
        ]
    deck_dict = {
        "id": deck.id,
        "entity_id": deck.entity_id,
        "source_id": deck.source_id,
        "title": deck.title,
        "created": deck.created,
        "modified": deck.modified,
        "user": deck.user,
        "dice": deck_dice_dict,
        "phoenixborn": {
            "name": phoenixborn.name,
            "stub": phoenixborn.stub,
            "battlefield": phoenixborn.json["battlefield"],
            "life": phoenixborn.json["life"],
            "spellboard": phoenixborn.json["spellboard"],
            "is_legacy": phoenixborn.is_legacy,
        },
        "cards": sorted(card_output, key=itemgetter("name")),
        "conjurations": sorted(conjuration_output, key=itemgetter("name")),
    }
    # Legacy-only data
    if deck.is_legacy:
        deck_dict["is_legacy"] = True
        deck_dict["ashes_500_score"] = deck.ashes_500_score
        deck_dict["ashes_500_revision_id"] = deck.ashes_500_revision_id
    return deck_dict


def paginate_deck_listing(
    query: db.Query, session: db.Session, request: Request, paging: PaginationOptions
) -> dict:
    """Generates a paginated deck listing using as few queries as possible."""
    # Gather our paginated results
    output = paginated_results_for_query(
        query=query, paging=paging, url=str(request.url)
    )
    # Parse through the decks so that we can load their cards en masse with a single query
    deck_ids = set()
    needed_cards = set()
    for deck_row in output["results"]:
        deck_ids.add(deck_row.id)
        # Ensure we lookup our Phoenixborn cards
        needed_cards.add(deck_row.phoenixborn_id)
    # Fetch and collate our dice information for all decks
    deck_dice = session.query(DeckDie).filter(DeckDie.deck_id.in_(deck_ids)).all()
    deck_id_to_dice = defaultdict(list)
    for deck_die in deck_dice:
        deck_id_to_dice[deck_die.deck_id].append(deck_die)
    # Now that we have all our basic deck information, look up the cards and quantities they include
    deck_cards = session.query(DeckCard).filter(DeckCard.deck_id.in_(deck_ids)).all()
    deck_id_to_deck_cards = defaultdict(list)
    for deck_card in deck_cards:
        needed_cards.add(deck_card.card_id)
        deck_id_to_deck_cards[deck_card.deck_id].append(deck_card)
    # And finally we need to fetch all top-level conjurations
    card_id_to_conjurations = get_conjuration_mapping(
        session=session, card_ids=needed_cards
    )
    # Now that we have root-level conjurations, we can gather all our cards and setup our decks
    cards = session.query(Card).filter(Card.id.in_(needed_cards)).all()
    card_id_to_card = {x.id: x for x in cards}
    deck_output = []
    for deck in output["results"]:
        deck_output.append(
            generate_deck_dict(
                deck=deck,
                card_id_to_card=card_id_to_card,
                card_id_to_conjurations=card_id_to_conjurations,
                deck_cards=deck_id_to_deck_cards[deck.id],
                deck_dice=deck_id_to_dice.get(deck.id),
            )
        )
    output["results"] = deck_output
    return output


def deck_to_dict(session: db.Session, deck: Deck) -> dict:
    """Converts a Deck object into an output dict using as few queries as possible."""
    needed_cards = set()
    needed_cards.add(deck.phoenixborn_id)
    deck_cards = session.query(DeckCard).filter(DeckCard.deck_id == deck.id).all()
    for deck_card in deck_cards:
        needed_cards.add(deck_card.card_id)
    deck_dice = session.query(DeckDie).filter(DeckDie.deck_id == deck.id).all()
    # And finally we need to fetch all top-level conjurations
    card_id_to_conjurations = get_conjuration_mapping(
        session=session, card_ids=needed_cards
    )
    # Now that we have root-level conjurations, we can gather all our cards and generate deck output
    cards = session.query(Card).filter(Card.id.in_(needed_cards)).all()
    card_id_to_card = {x.id: x for x in cards}
    return generate_deck_dict(
        deck=deck,
        card_id_to_card=card_id_to_card,
        card_id_to_conjurations=card_id_to_conjurations,
        deck_cards=deck_cards,
        deck_dice=deck_dice,
    )

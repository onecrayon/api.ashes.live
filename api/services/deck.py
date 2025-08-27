from collections import defaultdict
from operator import itemgetter

from sqlalchemy import select
from starlette.requests import Request

from api import db
from api.environment import settings
from api.models import Deck, DeckCard, DeckDie, DeckSelectedCard, Release, User
from api.models.card import Card, CardConjuration, DiceFlags
from api.schemas.cards import CardType
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.services.stream import (
    create_entity,
    refresh_stream_for_entity,
    update_subscription_for_user,
)
from api.utils.dates import utcnow
from api.utils.helpers import to_prefixed_tsquery
from api.utils.pagination import paginated_results_for_query


class PhoenixbornInDeck(Exception):
    """Raised when a Phoenixborn is included in the deck card list."""

    pass


class ConjurationInDeck(Exception):
    """Raised when a Conjuration is included in the deck card list."""

    card_name: str

    def __init__(self, card):
        self.card_name = card.name
        super().__init__()


class BadPhoenixbornUnique(Exception):
    """Raised when a Phoenixborn unique card is included in the deck card list, but doesn't match
    the deck's Phoenixborn.
    """

    card_name: str
    required_phoenixborn: str

    def __init__(self, card):
        self.card_name = card.name
        self.required_phoenixborn = card.phoenixborn
        super().__init__()


class RedRainsConversionFailed(Exception):
    """Raised when trying to change the Red Rains status of a deck that has a published snapshot."""

    pass


def create_or_update_deck(
    session: db.Session,
    current_user: "User",
    phoenixborn: Card,
    deck_id: int = None,
    title: str = None,
    description: str = None,
    dice: list[dict[str, str | int]] = None,
    cards: list[dict[str, str | int]] = None,
    first_five: list[str] = None,
    effect_costs: list[str] = None,
    tutor_map: dict[str, str] = None,
    is_red_rains: bool = False,
) -> "Deck":
    """Creates or updates a deck in place."""
    now = utcnow()
    # Tracks if dice or cards changed, as this necessitates resetting the export flag
    needs_new_export = False
    if deck_id:
        stmt = (
            select(Deck)
            .options(
                db.joinedload(Deck.cards),
                db.joinedload(Deck.dice),
                db.joinedload(Deck.selected_cards),
            )
            .where(Deck.id == deck_id)
        )
        deck = session.execute(stmt).unique().scalar_one()
        deck.title = title
        deck.description = description
        deck.phoenixborn_id = phoenixborn.id
        deck.modified = now
        if deck.is_red_rains != is_red_rains:
            if (
                session.query(Deck)
                .filter(
                    Deck.source_id == deck_id,
                    Deck.is_snapshot.is_(True),
                    Deck.is_public.is_(True),
                    Deck.is_deleted.is_(False),
                )
                .count()
            ):
                raise RedRainsConversionFailed()
            deck.is_red_rains = is_red_rains
    else:
        deck = Deck(
            entity_id=create_entity(session),
            title=title,
            description=description,
            user_id=current_user.id,
            phoenixborn_id=phoenixborn.id,
            is_snapshot=False,
            is_public=False,
            is_red_rains=is_red_rains,
        )

    # Update the dice listing
    deck_dice: list[DeckDie] = []
    total_dice = 0
    if dice:
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
    if deck.dice != deck_dice:
        needs_new_export = True
    deck.dice = deck_dice

    # And then the card listing
    deck_cards: list[DeckCard] = []
    card_stub_counts = {x["stub"]: x["count"] for x in (cards or [])}
    card_stubs = set(card_stub_counts.keys())
    if first_five:
        card_stubs.update(first_five)
    if effect_costs:
        card_stubs.update(effect_costs)
    if tutor_map:
        card_stubs.update(tutor_map.keys())
        card_stubs.update(tutor_map.values())
    minimal_cards = (
        session.query(Card.id, Card.stub, Card.name, Card.card_type, Card.phoenixborn)
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
        if card.phoenixborn and card.phoenixborn != phoenixborn.name:
            raise BadPhoenixbornUnique(card)
        if card.card_type in (
            CardType.conjuration.value,
            CardType.conjured_alteration_spell.value,
        ):
            raise ConjurationInDeck(card)
        deck_cards.append(DeckCard(card_id=card.id, count=count))
    if deck.cards != deck_cards:
        needs_new_export = True
    deck.cards = deck_cards

    # If dice or cards changed, reset the export flag
    if needs_new_export and settings.allow_exports:
        deck.is_exported = False

    # Save everything up!
    deck.selected_cards = []
    session.add(deck)
    session.commit()

    # And finally set selected cards (first five, paid effects, and tutored cards; used for stats)
    #  This happens after clearing them out above because SQLAlchemy cannot handle the three way
    #  composite index (tries to insert duplicates instead of updating intelligently based on
    #  tutor_card_id)
    stub_to_card = {x.stub: x for x in minimal_cards}
    selected_cards: list[DeckSelectedCard] = []
    if effect_costs:
        for card_stub in effect_costs:
            card = stub_to_card.get(card_stub)
            # pytest-cov simply can't handle catching this usage, so we have to skip it
            if not card:  # pragma: no cover
                continue
            if first_five and card_stub not in first_five:
                selected_cards.append(
                    DeckSelectedCard(card_id=card.id, is_paid_effect=True)
                )
    if first_five:
        for card_stub in first_five:
            card = stub_to_card.get(card_stub)
            if not card:  # pragma: no cover
                continue
            selected_cards.append(
                DeckSelectedCard(
                    card_id=card.id,
                    is_first_five=True,
                    is_paid_effect=card.stub in effect_costs if effect_costs else False,
                )
            )
    if tutor_map:
        for tutor_stub, card_stub in tutor_map.items():
            tutor_card = stub_to_card.get(tutor_stub)
            card = stub_to_card.get(card_stub)
            if not tutor_card or not card:  # pragma: no cover
                continue
            selected_cards.append(
                DeckSelectedCard(card_id=card.id, tutor_card_id=tutor_card.id)
            )
    deck.selected_cards = selected_cards
    session.commit()

    return deck


def create_snapshot_for_deck(
    session: db.Session,
    user: "User",
    deck: "Deck",
    title: str = None,
    description: str = None,
    is_public=False,
    preconstructed_release_id: int = None,
    include_first_five=False,
) -> "Deck":
    """Creates a snapshot for the given deck"""
    entity_id = create_entity(session)
    snapshot = Deck(
        entity_id=entity_id,
        title=title,
        description=description,
        # In the interim while we are saving the cards and dice and so forth, we mark this as private so that it doesn't
        #  show up in any listings and break stuff in weird ways
        is_public=False,
        is_snapshot=True,
        is_red_rains=deck.is_red_rains,
        is_preconstructed=bool(preconstructed_release_id),
        preconstructed_release=preconstructed_release_id,
        source_id=deck.id,
        user_id=user.id,
        phoenixborn_id=deck.phoenixborn_id,
    )
    # Save our snapshot so that we have an ID
    session.add(snapshot)
    session.commit()
    # Now duplicate the cards, dice, and selected cards for the given deck
    if deck.cards:
        for deck_card in deck.cards:
            session.add(
                DeckCard(
                    deck_id=snapshot.id,
                    card_id=deck_card.card_id,
                    count=deck_card.count,
                )
            )
    if deck.dice:
        for deck_die in deck.dice:
            session.add(
                DeckDie(
                    deck_id=snapshot.id,
                    die_flag=deck_die.die_flag,
                    count=deck_die.count,
                )
            )
    if deck.selected_cards and (include_first_five or not is_public):
        for deck_selected_card in deck.selected_cards:
            session.add(
                DeckSelectedCard(
                    deck_id=snapshot.id,
                    card_id=deck_selected_card.card_id,
                    tutor_card_id=deck_selected_card.tutor_card_id,
                    is_first_five=deck_selected_card.is_first_five,
                    is_paid_effect=deck_selected_card.is_paid_effect,
                )
            )
    # Flip our public flag now that we've populated the deck details, if necessary
    if is_public:
        snapshot.is_public = True
        # We also need to publish to the Stream for public snapshots
        refresh_stream_for_entity(
            session,
            entity_id=snapshot.entity_id,
            entity_type="deck",
            source_entity_id=deck.entity_id,
        )
        # And finally we need to update the user's subscription to mark the last_seen_entity_id
        update_subscription_for_user(
            session,
            user=user,
            source_entity_id=deck.entity_id,
            last_seen_entity_id=snapshot.entity_id,
        )
    session.commit()
    return snapshot


def get_decks_query(
    session: db.Session,
    show_legacy=False,
    show_red_rains=False,
    is_public=False,
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    # Filtering options
    q: str | None = None,
    phoenixborn: list[str] | None = None,
    cards: list[str] | None = None,
    players: list[str] | None = None,
    show_preconstructed=False,
) -> db.Query:
    query = session.query(Deck).filter(
        Deck.is_legacy.is_(show_legacy),
        Deck.is_deleted.is_(False),
        Deck.is_red_rains.is_(show_red_rains),
    )
    if show_preconstructed:
        query = query.filter(Deck.is_preconstructed.is_(True))
    if is_public:
        deck_comp = db.aliased(Deck)
        query = query.outerjoin(
            deck_comp,
            db.and_(
                Deck.source_id == deck_comp.source_id,
                deck_comp.is_snapshot.is_(True),
                deck_comp.is_public.is_(True),
                deck_comp.is_deleted.is_(False),
                db.or_(
                    Deck.created < deck_comp.created,
                    db.and_(Deck.created == deck_comp.created, Deck.id < deck_comp.id),
                ),
            ),
        ).filter(
            deck_comp.id.is_(None), Deck.is_snapshot.is_(True), Deck.is_public.is_(True)
        )
    else:
        query = query.filter(Deck.is_snapshot.is_(False))
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
                card_id_to_conjuration_mapping[conjuration.id] = (
                    conjuration.conjurations
                )
            add_conjurations(
                card_id_to_conjuration_mapping, conjuration.id, conjuration_set
            )


def get_conjuration_mapping(session: db.Session, card_ids: set[int]) -> dict:
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
    card_id_to_card: dict[int, Card],
    card_id_to_conjurations: dict[int, list[Card]],
    deck_cards: list[DeckCard] = None,
    deck_dice: list[DeckDie] = None,
    include_share_uuid: bool = False,
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
    deck_dice_dict = []
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
        "is_public": deck.is_public,
        "is_snapshot": deck.is_snapshot,
        "is_red_rains": deck.is_red_rains,
    }
    if include_share_uuid:
        deck_dict["direct_share_uuid"] = deck.direct_share_uuid
    # Legacy-only data
    if deck.is_legacy:
        deck_dict["is_legacy"] = True
        deck_dict["ashes_500_score"] = deck.ashes_500_score
        deck_dict["ashes_500_revision_id"] = deck.ashes_500_revision_id
    return deck_dict


def paginate_deck_listing(
    query: db.Query,
    session: db.Session,
    request: Request,
    paging: PaginationOptions,
    include_share_uuids: bool = False,
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
                include_share_uuid=include_share_uuids,
            )
        )
    output["results"] = deck_output
    return output


def deck_to_dict(
    session: db.Session,
    deck: Deck,
    include_comment_entity_id=False,
    include_share_uuid=False,
) -> dict:
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
    deck_dict = generate_deck_dict(
        deck=deck,
        card_id_to_card=card_id_to_card,
        card_id_to_conjurations=card_id_to_conjurations,
        deck_cards=deck_cards,
        deck_dice=deck_dice,
        include_share_uuid=include_share_uuid,
    )
    deck_dict["description"] = deck.description
    if include_comment_entity_id:
        # This is an implicit SQL lookup, but it's going to require a lookup either way, so meh
        deck_dict["comments_entity_id"] = (
            deck.source.entity_id if deck.source_id else deck.entity_id
        )
    # If we are including first five information, grab that now
    first_five = []
    effect_costs = []
    tutor_map = {}
    # This is another implicit SQL lookup, but again it requires a lookup either way
    for selected_card in deck.selected_cards:
        card = card_id_to_card.get(selected_card.card_id)
        # This situation should theoretically never happen, but just in case...
        if not card:
            continue
        if selected_card.is_first_five:
            first_five.append(card.stub)
        if selected_card.is_paid_effect:
            effect_costs.append(card.stub)
        if selected_card.tutor_card_id:
            tutor_card = card_id_to_card.get(selected_card.tutor_card_id)
            if tutor_card:
                tutor_map[tutor_card.stub] = card.stub
    deck_dict["first_five"] = first_five
    deck_dict["effect_costs"] = effect_costs
    deck_dict["tutor_map"] = tutor_map
    return deck_dict

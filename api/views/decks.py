from collections import defaultdict, OrderedDict
from operator import itemgetter
from typing import Optional, List

from fastapi import APIRouter, Depends, Request

from api import db
from api.depends import (
    paging_options,
    get_current_user,
    get_session,
    login_required,
    AUTH_RESPONSES,
)
from api.exceptions import NoUserAccessException, APIException, NotFoundException
from api.models import User, Deck, Card, DeckCard, DeckDie
from api.models.card import CardConjuration, DiceFlags
from api.schemas import DetailResponse
from api.schemas.decks import DeckFilters, DeckListingOut, DeckOut, DeckIn
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.services.deck import create_or_update_deck, NoSuchDeck
from api.utils.helpers import to_prefixed_tsquery
from api.utils.pagination import paginated_results_for_query

router = APIRouter()


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


def paginate_deck_listing(
    query: db.Query, session: db.Session, request: Request, paging: PaginationOptions
) -> dict:
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
        deck_id_to_dice[deck_die.deck_id].append(
            {
                "count": deck_die.count,
                "name": DiceFlags(deck_die.die_flag).name,
            }
        )
    # Now that we have all our basic deck information, look up the cards and quantities they include
    deck_cards = session.query(DeckCard).filter(DeckCard.deck_id.in_(deck_ids)).all()
    deck_id_to_deck_cards = defaultdict(list)
    for deck_card in deck_cards:
        needed_cards.add(deck_card.card_id)
        deck_id_to_deck_cards[deck_card.deck_id].append(
            {
                "count": deck_card.count,
                "card_id": deck_card.card_id,
            }
        )
    # And finally we need to fetch all top-level conjurations
    conjuration_results = (
        session.query(Card, CardConjuration.card_id.label("root_card"))
        .join(CardConjuration, Card.id == CardConjuration.conjuration_id)
        .filter(CardConjuration.card_id.in_(needed_cards))
        .all()
    )
    card_id_to_conjurations = defaultdict(list)
    for result in conjuration_results:
        card_id_to_conjurations[result.root_card].append(result.Card)
    # Now that we have root-level conjurations, we can gather all our cards and setup our decks
    cards = session.query(Card).filter(Card.id.in_(needed_cards)).all()
    card_id_to_card = {x.id: x for x in cards}
    deck_output = []
    for deck in output["results"]:
        card_output = []
        conjuration_set = set()
        for deck_card in deck_id_to_deck_cards.get(deck.id, []):
            card = card_id_to_card[deck_card["card_id"]]
            card_output.append(
                {
                    "count": deck_card["count"],
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
        deck_dict = {
            "id": deck.id,
            "entity_id": deck.entity_id,
            "source_id": deck.source_id,
            "title": deck.title,
            "created": deck.created,
            "modified": deck.modified,
            "user": deck.user,
            "dice": deck_id_to_dice.get(deck.id),
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
        deck_output.append(deck_dict)
    output["results"] = deck_output
    return output


@router.get(
    "/decks",
    response_model=DeckListingOut,
    response_model_exclude_unset=True,
)
def list_decks(
    request: Request,
    filters: DeckFilters = Depends(),
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    # Standard dependencies
    paging: PaginationOptions = Depends(paging_options),
    session: db.Session = Depends(get_session),
):
    """Get a paginated listing of decks with optional filters.

    ## Available filters

    * `q`: deck title search
    * `phoenixborn`: list of Phoenixborn slugs
    * `player`: list of player badges
    * `show_legacy` (default: false): if true, legacy 1.0 decks will be returned
    """
    query = get_decks_query(
        session,
        show_legacy=filters.show_legacy,
        is_public=True,
        order=order,
        q=filters.q,
        phoenixborn=filters.phoenixborn,
        cards=filters.card,
        players=filters.player,
    )
    return paginate_deck_listing(query, session, request, paging)


@router.put(
    "/decks",
    response_model=DeckOut,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Deck creation failed.",
        },
        **AUTH_RESPONSES,
    },
)
def save_deck(
    data: DeckIn,
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Create or update a deck in place.

    **This is not a patch!** You must pass the entire deck object in the body every time, and it
    will only be treated as an update if there is an ID included.
    """
    # Verify that the user has access to this deck, if we're saving over an existing deck
    if data.id:
        deck_check = session.query(Deck.user_id).get(data.id)
        if not deck_check or deck_check.user_id != current_user.id:
            raise NoUserAccessException(detail="You cannot save a deck you do not own.")
    # Ensure we have a Phoenixborn stub
    phoenixborn_stub = (
        data.phoenixborn
        if isinstance(data.phoenixborn, str)
        else data.phoenixborn.get("stub")
    )
    phoenixborn = (
        session.query(Card.id)
        .filter(Card.stub == phoenixborn_stub, Card.is_legacy.is_(False))
        .first()
    )
    if not phoenixborn:
        raise APIException(detail="Valid Phoenixborn is required.")
    try:
        deck = create_or_update_deck(
            session,
            phoenixborn_id=phoenixborn_id,
            deck_id=data.id,
            title=data.title,
            description=data.description,
            dice=[x.dict() for x in data.dice] if data.dice else None,
            cards=[x.dict() for x in data.cards] if data.cards else None,
        )
    except NoSuchDeck:
        raise NotFoundException()
    except:
        # TODO: handle specific exceptions raised by the service
        pass
    # TODO: format the deck into standard DeckOut output dict and return
    return {"detail": "Worked!"}

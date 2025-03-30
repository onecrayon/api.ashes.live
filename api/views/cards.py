from fastapi import APIRouter, Depends, Query, Request, status
from sqlalchemy.exc import IntegrityError

from api import db
from api.depends import (
    AUTH_RESPONSES,
    admin_required,
    get_current_user,
    get_session,
    paging_options,
)
from api.exceptions import APIException, NotFoundException
from api.models import Deck, DeckCard, Subscription
from api.models.card import Card, DiceFlags
from api.models.release import Release, UserRelease
from api.models.user import UserType
from api.schemas import DetailResponse
from api.schemas.cards import (
    CardDetails,
    CardDiceCosts,
    CardIn,
    CardListingOut,
    CardOut,
    CardsFilterDiceLogic,
    CardsFilterListingMode,
    CardsFilterRelease,
    CardsFilterType,
    CardsSortingMode,
)
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.services.card import MissingConjurations
from api.services.card import create_card as create_card_service
from api.services.card import gather_conjurations, gather_root_summons
from api.utils.helpers import powerset, stubify, to_prefixed_tsquery
from api.utils.pagination import paginated_results_for_query

router = APIRouter()


@router.get(
    "/cards",
    response_model=CardListingOut,
    response_model_exclude_unset=True,
)
def list_cards(
    request: Request,
    # Filtration query string options
    q: str = None,
    show_legacy: bool = False,
    types: list[CardsFilterType] = Query(None),
    mode: CardsFilterListingMode = CardsFilterListingMode.listing,
    show_summons: bool = False,
    releases: CardsFilterRelease = CardsFilterRelease.all_,
    r: list[str] = Query(None),
    dice: list[CardDiceCosts] = Query(None),
    dice_logic: CardsFilterDiceLogic = CardsFilterDiceLogic.only_,
    include_uniques_for: str = None,
    sort: CardsSortingMode = CardsSortingMode.name,
    order: PaginationOrderOptions = PaginationOrderOptions.asc,
    # Standard dependencies
    paging: PaginationOptions = Depends(paging_options),
    current_user: "UserType" = Depends(get_current_user),
    session: db.Session = Depends(get_session),
):
    """Get a paginated listing of cards with optional filters.

    ## Available filters

    * `q`: text search
    * `show_legacy` (default: false): if true, legacy 1.0 card data will be returned
    * `mode` (default: `listing`): if `deckbuilder`, Phoenixborn, uniques, and conjurations will not be included
    * `types`: list of types to include in filtered cards
    * `show_summons` (default: false): if true, will only show cards whose name starts with "Summon "
    * `releases` (default: `all`): if `mine` will show only releases owned by the current user
    * `r`: list of release stubs; will only show cards belonging to releases in this list (**Note:** does nothing if `releases` is not `all`!)
    * `dice`: list of dice costs that cards in the listing must use
    * `dice_logic` (default: `only`): `only` mean the cards will only use one or more of the selected colors; `any` is
      deprecated, but is a synonym for `only`; `includes` mean the cards will use at least one of the selected colors
      (but could require colors that are not selected); and `all` is deprecated but will only show cards that require
      all of the chosen colors
    * `include_uniques_for`: if set to a Phoenixborn name, listing will also include uniques belonging to the given Phoenixborn
      (only applicable to deckbuilder mode)
    """
    # First build our base query
    query = (
        session.query(Card.json).join(Card.release).filter(Release.is_public.is_(True))
    )
    # Only include legacy cards, if we're in legacy mode
    if show_legacy:
        query = query.filter(Card.is_legacy.is_(True))
    else:
        query = query.filter(Card.is_legacy.is_(False))
    # Add a search term, if we're using one
    if q and q.strip():
        query = query.filter(
            db.func.to_tsvector("english", Card.search_text).match(
                to_prefixed_tsquery(q)
            )
        )
    # Filter by particular card types
    if types:
        card_types = set()
        for card_type in types:
            if card_type is CardsFilterType.conjurations:
                card_types.add("Conjuration")
                card_types.add("Conjured Alteration Spell")
            else:
                card_types.add(card_type.replace("_", " ").title())
        query = query.filter(Card.card_type.in_(card_types))
    # Exclude some types if we're in deckbuilder mode
    if mode is CardsFilterListingMode.deckbuilder:
        query = query.filter(
            Card.card_type.notin_(
                ("Phoenixborn", "Conjuration", "Conjured Alteration Spell")
            )
        )
    # Check if we're filtering by "Summon" cards
    if show_summons:
        query = query.filter(Card.is_summon_spell.is_(True))
    # Filter by releases, if requested
    if releases or r:
        if show_legacy and releases is CardsFilterRelease.phg:
            query = query.filter(Release.is_phg.is_(True))
        elif releases is CardsFilterRelease.mine and not current_user.is_anonymous():
            my_release_subquery = (
                session.query(UserRelease.release_id)
                .filter(UserRelease.user_id == current_user.id)
                .subquery()
            )
            query = query.filter(Card.release_id.in_(my_release_subquery))
        elif r:
            query = query.filter(Release.stub.in_(r))
    # Filter against required dice costs
    if dice:
        dice_set = set(dice)
        dice_filters = []
        if dice_logic in (CardsFilterDiceLogic.any_, CardsFilterDiceLogic.only_):
            if "basic" in dice_set:
                dice_filters.append(
                    db.and_(
                        Card.dice_flags == 0,
                        Card.alt_dice_flags == 0,
                        Card.card_type.notin_(
                            ["Conjuration", "Conjured Alteration Spell"]
                        ),
                    )
                )
                dice_set.remove("basic")
            # Only add additional filters if we requested more than basic cards
            if dice_set:
                # We want to match on any combination of the passed dice, so pre-calculate those values
                dice_values = [DiceFlags[die].value for die in dice_set]
                dice_sums = [sum(x) for x in powerset(dice_values) if x]
                # First scenario: the dice flags must match one of the available permutations of the selected dice
                #  AND the alt flags must be empty or contain at least one of the available dice
                dice_filters.append(
                    db.and_(
                        Card.dice_flags.in_(dice_sums),
                        # Dice are stored in the database as bitwise flags, so we can check for the existence of a dice
                        #  type in the alt dice by doing an & bitwise operation and comparing with the flag value
                        #  (because & only includes 1 for bits that match in both numbers, so you end up with just the
                        #  flag value for that given flag, if it exists).
                        db.or_(
                            Card.alt_dice_flags == 0,
                            *[
                                Card.alt_dice_flags.op("&")(die_value) == die_value
                                for die_value in dice_values
                            ],
                        ),
                    )
                )
                # Second scenario: the dice flags must be empty AND the alt flags must match one of the dice
                dice_filters.append(
                    db.and_(
                        Card.dice_flags == 0,
                        db.or_(
                            *[
                                Card.alt_dice_flags.op("&")(die_value) == die_value
                                for die_value in dice_values
                            ],
                        ),
                    )
                )
        elif dice_logic == CardsFilterDiceLogic.all_:
            # Since every passed dice type must be included for ALL searches, we go through all
            #  powersets and look for cards that match the powerset for the dice flags, and
            #  whatever dice types were missed in the alt flags. So if you pass ceremonial and
            #  charm, you get cards that require both but have no alt costs, cards that require
            #  ceremonial with a charm alt cost, etc.
            dice_values = set(DiceFlags[die].value for die in dice_set)
            dice_powersets = [set(x) for x in powerset(dice_values)]
            for subset in dice_powersets:
                missing_values = sum(dice_values.difference(subset))
                dice_filters.append(
                    db.and_(
                        Card.dice_flags == sum(subset),
                        (
                            Card.alt_dice_flags.op("&")(missing_values)
                            == missing_values
                            if missing_values
                            else Card.alt_dice_flags == missing_values
                        ),
                    )
                )
        elif dice_set != {"basic"}:
            # The only remaining logic is the `includes` logic, which is a lot simpler because we
            #  can just use bitwise AND `&` to verify that at least one dice flag is set for a
            #  given combo. However, we must ignore this logic if they are trying to search for only
            #  basic dice, because those are canonically value `0`.
            possible_dice = sum(DiceFlags[die].value for die in dice_set)
            dice_filters.append(Card.dice_flags.op("&")(possible_dice) > 0)
            dice_filters.append(Card.alt_dice_flags.op("&")(possible_dice) > 0)

        # It's possible, though unlikely, to not have filters here if they passed a bad dice listing
        #  (e.g. passed "basic" for the dice color and "includes" for the logic)
        if dice_filters:
            query = query.filter(db.or_(*dice_filters))
    # Only Include Phoenixborn uniques for the given Phoenixborn (or no Phoenixborn, in deckbuilder)
    if include_uniques_for:
        query = query.filter(
            db.or_(
                Card.phoenixborn.is_(None),
                Card.phoenixborn == include_uniques_for,
            )
        )
    elif mode is CardsFilterListingMode.deckbuilder:
        query = query.filter(
            Card.phoenixborn.is_(None),
        )
    if sort == CardsSortingMode.type_:
        # This uses a similar ordering to how the front-end organizes cards in deck listings
        query = query.order_by(
            getattr(Card.type_weight, order)(), getattr(Card.name, order)()
        )
    elif sort == CardsSortingMode.cost:
        query = query.order_by(
            getattr(Card.cost_weight, order)(), getattr(Card.name, order)()
        )
    elif sort == CardsSortingMode.dice:
        # This one is trickier: when sorting by dice, we want cards to show up grouped first by
        #  required dice types (ceremonial, charm, illusion, natural, divine, sympathy, time)
        #  then by their relative cost, and finally falling back on name. The latter two are simple,
        #  but to order by dice types we need to first bitwise OR dice and alt_dice (so we get a
        #  number representing all possible dice types you could spend), then order by that
        query = query.order_by(
            getattr(Card.dice_weight, order)(),
            getattr(Card.cost_weight, order)(),
            getattr(Card.name, order)(),
        )
    elif sort == CardsSortingMode.release:
        # This one is mainly there for people who organize their sets by preconstructed deck, though
        #  it groups all Master Set decks into a single group (not really sure how I would separate
        #  those cards out by preconstructed deck, because there's not an easy join strategy to
        #  fetch that data; I'd have to denormalize it into the cards. Will consider if people
        #  request it)
        query = query.order_by(
            getattr(Release.id, order)(),
            getattr(Card.type_weight, order)(),
            getattr(Card.name, order)(),
        )
    else:
        # Defaults to ordering by name
        query = query.order_by(getattr(Card.name, order)())
    return paginated_results_for_query(
        query=query,
        paging=paging,
        url=str(request.url),
    )


@router.get(
    "/cards/fuzzy-lookup",
    response_model=CardOut,
    response_model_exclude_unset=True,
    responses={404: {"model": DetailResponse}},
)
def get_card_fuzzy_lookup(
    q: str, show_legacy: bool = False, session: db.Session = Depends(get_session)
):
    """Returns a single card using fuzzy lookup logic

    This is similar to querying `/cards` limited to a single result, except that it applies the
    following heuristics when searching for cards:

    * Preference the card with the search term in its stub
    * Preference the card without "summon" in its stub if "summon" is not in the query
    * Preference the card with "summon" in its stub if "summon" is in the query
    """
    # Make sure we have a search term
    if not q or not q.strip():
        raise APIException(detail="Query string is required.")
    query = session.query(Card).join(Card.release).filter(Release.is_public.is_(True))
    if show_legacy:
        query = query.filter(Card.is_legacy.is_(True))
    else:
        query = query.filter(Card.is_legacy.is_(False))
    stub_search = stubify(q)
    search_vector = db.func.to_tsvector("english", Card.search_text)
    prefixed_query = to_prefixed_tsquery(q)
    query = query.filter(
        db.or_(
            search_vector.match(prefixed_query),
            Card.stub.like(f"%{stub_search}%"),
        )
    )
    # Order by search ranking
    possible_cards = query.order_by(Card.name.asc()).all()
    if not possible_cards:
        raise NotFoundException(detail="No matching cards found.")
    ranks_with_matches = []
    # We use this to calculate boost offsets for our three conditions (exact stub match,
    #  partial stub match, "summon")
    base_upper_rank = len(possible_cards)
    # We use this to track the original Postgres alphabetical ordering (our fallback). I originally
    #  tested this using the full text ranking, and it was incredibly opaque, so tossed that.
    db_rank = base_upper_rank
    for card in possible_cards:
        rank = db_rank
        # First check for exact stub matches, and give those greatest preference
        if (
            card.stub == stub_search
            or card.stub.startswith(f"{stub_search}-")
            or card.stub.endswith(f"-{stub_search}")
            or f"-{stub_search}-" in card.stub
        ):
            rank += base_upper_rank * 3
        elif stub_search in card.stub:
            # We have some level of partial stub match, so give that a big preference boost
            rank += base_upper_rank * 2
        # And then boost things based on whether "summon" exists (or does not) in both terms
        if ("summon" in stub_search and "summon" in card.stub) or (
            "summon" not in stub_search and "summon" not in card.stub
        ):
            rank += base_upper_rank + 1
        ranks_with_matches.append((rank, card))
        db_rank -= 1
    # Sort our cards in descending rank order, then return the JSON from the first result
    ranks_with_matches.sort(key=lambda x: x[0], reverse=True)
    return ranks_with_matches[0][1].json


@router.get(
    "/cards/{stub}",
    response_model=CardOut,
    response_model_exclude_unset=True,
    responses={404: {"model": DetailResponse}},
)
def get_card(
    stub: str, show_legacy: bool = False, session: db.Session = Depends(get_session)
):
    """Returns the most basic information about this card."""
    query = session.query(Card.json).filter(Card.stub == stub)
    if show_legacy:
        query = query.filter(Card.is_legacy.is_(True))
    else:
        query = query.filter(Card.is_legacy.is_(False))
    card_json = query.join(Card.release).filter(Release.is_public == True).scalar()
    if not card_json:
        raise NotFoundException(detail="Card not found.")
    return card_json


def _card_to_minimal_card(card: Card) -> dict:
    return {"name": card.name, "stub": card.stub}


@router.get(
    "/cards/{stub}/details",
    response_model=CardDetails,
    response_model_exclude_unset=True,
    responses={404: {"model": DetailResponse}},
)
def get_card_details(
    stub: str,
    show_legacy: bool = False,
    session: db.Session = Depends(get_session),
    current_user: "UserType" = Depends(get_current_user),
):
    """Returns the full details about the card for use on the card details page"""
    card = (
        session.query(Card)
        .join(Card.release)
        .options(db.contains_eager(Card.release))
        .filter(
            Card.stub == stub,
            Card.is_legacy.is_(show_legacy),
            Release.is_public == True,
        )
        .scalar()
    )
    if not card:
        raise NotFoundException(detail="Card not found.")

    # Gather up all related cards; there are two scenarios here: not a Phoenixborn card, in which
    #  case we just look up for the cards that can summon and down for the conjurations that can
    #  be summoned by one or more of those cards. Or we look up the Phoenixborn, unique, and all
    #  related conjurations
    related_cards = {}
    phoenixborn = None
    summons: list | None = None
    if card.phoenixborn or card.card_type == "Phoenixborn":
        # Grab all cards related to this Phoenixborn
        if card.phoenixborn:
            phoenixborn = (
                session.query(Card)
                .filter(
                    Card.name == card.phoenixborn,
                    Card.card_type == "Phoenixborn",
                    Card.is_legacy.is_(show_legacy),
                )
                .first()
            )
        else:
            phoenixborn = card
        phoenixborn_conjurations = gather_conjurations(phoenixborn)
        phoenixborn_unique = (
            session.query(Card)
            .filter(
                Card.phoenixborn == phoenixborn.name,
                Card.card_type.notin_(("Conjuration", "Conjured Alteration Spell")),
                Card.is_legacy.is_(show_legacy),
            )
            .first()
        )
        phoenixborn_unique_conjurations = gather_conjurations(phoenixborn_unique)
        related_cards["phoenixborn"] = _card_to_minimal_card(phoenixborn)
        if phoenixborn_conjurations:
            related_cards["phoenixborn_conjurations"] = [
                _card_to_minimal_card(x) for x in phoenixborn_conjurations
            ]
            if card.id in [x.id for x in phoenixborn_conjurations]:
                summons = [phoenixborn]
        if phoenixborn_unique:
            related_cards["phoenixborn_unique"] = _card_to_minimal_card(
                phoenixborn_unique
            )
        if phoenixborn_unique_conjurations:
            related_cards["phoenixborn_unique_conjurations"] = [
                _card_to_minimal_card(x) for x in phoenixborn_unique_conjurations
            ]
            if card.id in [x.id for x in phoenixborn_unique_conjurations]:
                summons = [phoenixborn_unique]
    else:
        # Check to see if we have any conjurations that we need to map to this card
        # We want to look up things in a different order depending on whether we're looking at
        #  conjuration or not (because if we always start with root summons, we'll lose alternate
        #  summoning cards when looking at a root summon)
        if card.card_type.startswith("Conjur"):
            summons = gather_root_summons(card)
            all_conjurations = []
            for root_card in summons:
                all_conjurations = all_conjurations + gather_conjurations(root_card)
            ids = set()
            conjurations = []
            for conjuration in all_conjurations:
                if conjuration.id not in ids:
                    ids.add(conjuration.id)
                    conjurations.append(conjuration)
        else:
            conjurations = gather_conjurations(card)
            all_summoning_cards = []
            for conjuration in conjurations:
                all_summoning_cards = all_summoning_cards + gather_root_summons(
                    conjuration
                )
            ids = set()
            summons = []
            for summon in all_summoning_cards:
                if summon.id not in ids:
                    ids.add(summon.id)
                    summons.append(summon)
        # Only return anything if this card has conjurations related to it
        if conjurations:
            related_cards["summoning_cards"] = [
                _card_to_minimal_card(x) for x in summons
            ]
            related_cards["conjurations"] = [
                _card_to_minimal_card(x) for x in conjurations
            ]

    # Gather stats
    # If we're looking at a conjuration, then make sure that we gather stats for everything that can
    #  summon that conjuration
    if card.card_type.startswith("Conjur"):
        root_card_ids = [x.id for x in summons] if summons else []
    else:
        root_card_ids = [card.id]
    # We only look up the Phoenixborn if it's in our root summons array (otherwise we might be
    #  looking at a Phoenixborn unique, and we'll get accurate counts for it in the next query)
    phoenixborn_counts = (
        session.query(
            db.func.count(Deck.id).label("decks"),
            db.func.count(db.func.distinct(Deck.user_id)).label("users"),
        )
        .filter(Deck.phoenixborn_id == phoenixborn.id, Deck.is_snapshot.is_(False))
        .first()
        if phoenixborn and phoenixborn.id in root_card_ids
        else None
    )
    card_counts = (
        session.query(
            db.func.count(DeckCard.deck_id).label("decks"),
            db.func.count(db.func.distinct(Deck.user_id)).label("users"),
        )
        .join(Deck, Deck.id == DeckCard.deck_id)
        .filter(
            DeckCard.card_id.in_(root_card_ids),
            Deck.is_snapshot.is_(False),
        )
        .first()
        if root_card_ids
        else None
    )
    counts = {"decks": 0, "users": 0}
    if phoenixborn_counts:
        counts["decks"] += phoenixborn_counts.decks
        counts["users"] += phoenixborn_counts.users
    if card_counts:
        counts["decks"] += card_counts.decks
        counts["users"] += card_counts.users

    # Grab preconstructed deck, if available
    preconstructed = (
        session.query(Deck.source_id, Deck.title)
        .join(DeckCard, DeckCard.deck_id == Deck.id)
        .filter(
            Deck.is_snapshot.is_(True),
            Deck.is_public.is_(True),
            Deck.is_preconstructed.is_(True),
            Deck.is_legacy.is_(show_legacy),
            DeckCard.card_id.in_(root_card_ids),
        )
        .first()
    )

    # Grab the last seen entity ID, if the user is logged in and has a subscription
    last_seen_entity_id = None
    if not current_user.is_anonymous():
        last_seen_entity_id = (
            session.query(Subscription.last_seen_entity_id)
            .filter(
                Subscription.user_id == current_user.id,
                Subscription.source_entity_id == card.entity_id,
            )
            .scalar()
        )

    return {
        "card": card.json,
        "usage": counts,
        "preconstructed_deck": (
            {
                "id": preconstructed.source_id,
                "title": preconstructed.title,
            }
            if preconstructed
            else None
        ),
        "related_cards": related_cards,
        "entity_id": card.entity_id,
        "last_seen_entity_id": last_seen_entity_id,
    }


@router.post(
    "/cards",
    response_model=DetailResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Card creation failed (likely due to missing conjurations).",
        },
        **AUTH_RESPONSES,
    },
)
def create_card(
    data: CardIn, session: db.Session = Depends(get_session), _=Depends(admin_required)
):
    """Admin-only. Adds a new card to the database.

    Releases will be implicitly created (and marked as private), if they do not already exist.
    There is no need to create the release ahead, as a result, which means you can populate a
    release entirely with this endpoint, and then just publish it when ready.

    Note that you must create conjurations *before* the cards that reference them.
    """
    # Implicitly create the release, if necessary
    release_stub = stubify(data.release)
    if not (
        release := (
            session.query(Release)
            .filter(Release.stub == release_stub, Release.is_legacy.is_(False))
            .one_or_none()
        )
    ):
        release = Release(name=data.release, stub=release_stub)
        session.add(release)
        session.commit()

    try:
        card = create_card_service(
            session,
            name=data.name,
            card_type=data.card_type,
            placement=data.placement,
            release=release,
            text=data.text,
            cost=data.cost,
            effect_magic_cost=data.effect_magic_cost,
            can_effect_repeat=data.can_effect_repeat,
            dice=data.dice,
            alt_dice=data.alt_dice,
            phoenixborn=data.phoenixborn,
            attack=data.attack,
            battlefield=data.battlefield,
            life=data.life,
            recover=data.recover,
            spellboard=data.spellboard,
            copies=data.copies,
        )
    except MissingConjurations as e:
        raise APIException(detail=str(e))
    except IntegrityError as e:
        raise APIException(detail="Card already exists!")
    return {"detail": "Card successfully created!"}

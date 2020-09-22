from enum import Enum
from typing import List

from fastapi import APIRouter, Depends, status, Request, Query
from pydantic import BaseModel

from api import db
from api.depends import get_current_user, get_session, paging_options
from api.models.card import Card
from api.models.release import Release
from api.models.user import User
from api.schemas.pagination import PaginationOptions, PaginatedResultsBase
from api.utils.pagination import paginated_results_for_query

router = APIRouter()


# Constants or use with listing filters
class CardsFilterListingMode(str, Enum):
    """Configures which cards to include.

    * `listing` (default): no restrictions
    * `deckbuilder`: filters out conjurations, Phoenixborn, and Phoenixborn uniques
    """

    listing = "listing"
    deckbuilder = "deckbuilder"


class CardsFilterType(str, Enum):
    """Card types for listing filters.

    * All normal card types are supported using snake_case
    * `conjurations`: Shorthand for `conjuration` and `conjured_alteration_spell`
    """

    conjurations = "conjurations"
    phoenixborn = "phoenixborn"
    ally = "ally"
    action_spell = "action_spell"
    reaction_spell = "reaction_spell"
    alteration_spell = "alteration_spell"
    ready_spell = "ready_spell"
    conjuration = "conjuration"
    conjured_alteration_spell = "conjured_alteration_spell"


class CardsFilterRelease(str, Enum):
    """Card releases for listing filters.

    * `all`: do not filter releases
    * `mine`: only show releases the current user owns
    * `phg`: only show Plaid Hat releases (legacy only)
    """

    all_ = "all"
    mine = "mine"
    phg = "phg"


class CardsFilterDice(str, Enum):
    """Card dice costs for listing filters."""

    ceremonial = "ceremonial"
    charm = "charm"
    divine = "divine"
    illusion = "illusion"
    natural = "natural"
    sympathy = "sympathy"
    time = "time"


class CardsFilterDiceLogic(str, Enum):
    """Dice logic for card listing filters."""

    all_ = "all"
    any_ = "any"


class CardListingOut(PaginatedResultsBase):
    """Filtered listing of cards"""

    # TODO: define the output schema for cards
    pass


@router.get("/cards", response_model=CardListingOut)
def list_cards(
    request: Request,
    # Filtration query string options
    q: str = None,
    show_legacy: bool = False,
    types: List[CardsFilterType] = Query(None),
    mode: CardsFilterListingMode = CardsFilterListingMode.listing,
    show_summons: bool = False,
    releases: CardsFilterRelease = CardsFilterRelease.all_,
    dice: List[CardsFilterDice] = Query(None),
    dice_logic: CardsFilterDiceLogic = CardsFilterDiceLogic.any_,
    include_uniques_for: str = None,
    # Standard dependencies
    paging: PaginationOptions = Depends(paging_options),
    current_user: "User" = Depends(get_current_user),
    session: db.Session = Depends(get_session),
):
    """Get a paginated listing of cards with optional filters.

    ## Available filters

    * `q`: text search
    * `show_legacy` (default: false): if true, legacy 1.0 card data will be returned
    * `mode` (default: `listing`): if `deckbuilder`, Phoenixborn, uniques, and conjurations will not be included
    * `type`: list of types to include in filtered cards
    * `show_summons` (default: false): if true, will only show cards whose name starts with "Summon "
    * `releases` (default: `all`): if `mine` will show only releases owned by the current user
    * `dice`: list of dice costs that cards in the listing must use
    * `dice_logic` (default: `any`): if `all` the cards returned must include all costs in `dice`
    * `include_uniques_for`: if set to a Phoenixborn name, listing will also include uniques belonging to the given Phoenixborn
    """
    # First build our query
    query = session.query(Card.json)
    # TODO: implement full text search using q (need to look up how Postgres handles this)
    # Only include legacy cards, if we're in legacy mode
    if show_legacy:
        query = query.filter(Card.is_legacy.is_(True))
    # Filter by particular card types
    if types:
        types = set()
        for card_type in types:
            if card_type is CardsFilterType.conjurations:
                types.add("Conjuration")
                types.add("Conjured Alteration Spell")
            else:
                types.add(card_type.replace("_", " ").title())
        query = query.filter(Card.card_type.in_(types))
    # Exclude some types if we're in deckbuilder mode
    if mode is CardsFilterListingMode.deckbuilder:
        query = query.filter(
            Card.card_type.notin_(
                ("Phoenixborn", "Conjuration", "Conjured Alteration Spell")
            )
        )
    # Check if we're filtering by "Summon" cards
    if show_summons:
        query = query.filter(Card.name.like("Summon %"))
    # Filter by releases, if requested
    if releases:
        if show_legacy and releases is CardsFilterRelease.phg:
            query = query.join(Release, Release.id == Card.release_id).filter(
                Release.is_phg.is_(True)
            )
        elif releases is CardsFilterRelease.mine and not current_user.is_anonymous():
            my_release_subquery = (
                session.query(UserRelease.release_id)
                .filter(UserRelease.user_id == current_user.id)
                .subquery()
            )
            query = query.filter(Card.release_id.in_(my_release_subquery))
    # Filter against required dice costs
    if dice:
        # TODO: embed this logic here instead of in the model
        if dice_logic is CardsFilterDiceLogic.any_:
            query = query.filter(Card.has_any_dice_filter(dice))
        else:
            query = query.filter(Card.has_all_dice_filter(dice))
    # Only Include Phoenixborn uniques for the given Phoenixborn
    if include_uniques_for:
        query = query.filter(
            db.or_(
                Card.phoenixborn.is_(None),
                Card.phoenixborn == include_uniques_for,
            )
        )
    return paginated_results_for_query(
        query=query,
        paging=paging,
        url=str(request.url),
    )

from enum import Enum

from pydantic import BaseModel, Field, validator

from api.utils.helpers import str_or_int

from .pagination import PaginatedResultsBase


class CardDiceCosts(str, Enum):
    """Card dice types."""

    basic = "basic"
    ceremonial = "ceremonial"
    charm = "charm"
    divine = "divine"
    illusion = "illusion"
    natural = "natural"
    sympathy = "sympathy"
    time = "time"


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


class CardsFilterDiceLogic(str, Enum):
    """Dice logic for card listing filters."""

    # These are the legacy terms for dice filtration; "any" is the default and shows any card that includes one or more
    #  of the chosen colors. "All" shows any card that includes all of the chosen colors. The two show identical result
    #  sets when filtering by a single color.
    all_ = "all"
    any_ = "any"
    # These are the new terms for dice filtration. "Only" is identical fo the prior "any" logic (shows cards that only
    #  use one or more of the chosen colors). "Includes" shows any card that includes at least one of the chosen colors
    #  (even if it uses colors that have not been chosen).
    only_ = "only"
    includes_ = "includes"


class CardsSortingMode(str, Enum):
    """Sorting modes for card listings"""

    name = "name"
    type_ = "type"
    cost = "cost"
    dice = "dice"
    release = "release"
    # TODO: should I enable these sorting strategies on the server?
    # # Stats
    # attack = 'attack'
    # battlefield = 'battlefield'
    # life = 'life'
    # spellboard = 'spellboard'
    # recover = 'recover'


class CardReleaseEmbeddedOut(BaseModel):
    """The release information embedded in card listings"""

    # These are included with all types of cards
    name: str
    stub: str
    # These are only include on legacy cards
    is_phg: bool = None
    is_promo: bool = None
    is_retiring: bool = None


class CardMinimalOut(BaseModel):
    """Minimal card information; e.g. for conjurations embedded in card listings"""

    name: str
    stub: str


class CardOut(BaseModel):
    """The standard JSON output for a card.

    Optional properties may not exist!
    """

    name: str
    stub: str
    type: str
    release: CardReleaseEmbeddedOut
    placement: str = None
    cost: list[list[str] | str] = None
    dice: list[str] = None
    altDice: list[str] = None
    magicCost: dict[str, int] = None
    effectMagicCost: dict[str, int] = None
    text: str = None
    conjurations: list[CardMinimalOut] = None
    phoenixborn: str = None
    attack: str | int = None
    battlefield: int = None
    life: str | int = None
    recover: str | int = None
    spellboard: int = None
    copies: int = None
    effectRepeats: bool = None
    is_legacy: bool = None

    # Custom parsing to ensure proper stats output
    _parse_attack = validator("attack", allow_reuse=True)(str_or_int)
    _parse_life = validator("life", allow_reuse=True)(str_or_int)
    _parse_recover = validator("recover", allow_reuse=True)(str_or_int)


class CardUsageCounts(BaseModel):
    """The counts in which this card appears in unique decks vs. users"""

    decks: int
    users: int


class RelatedCardLists(BaseModel):
    """Full listing of all cards that can summon or be summoned by this card.

    If it includes anything it will *either* contain all the Phoenixborn-related properties,
    *or* `summoning_cards` and `conjurations`, but not both sets.
    """

    summoning_cards: list[CardMinimalOut] = None
    conjurations: list[CardMinimalOut] = None
    phoenixborn: CardMinimalOut = None
    phoenixborn_conjurations: list[CardMinimalOut] = None
    phoenixborn_unique: CardMinimalOut = None
    phoenixborn_unique_conjurations: list[CardMinimalOut] = None


class PreconstructedDeck(BaseModel):
    """Minimal information about the preconstructed deck that contains this card."""

    id: int
    title: str


class CardDetails(BaseModel):
    """The full details object for a specific card.

    Optional properties may not exist!
    """

    card: CardOut
    usage: CardUsageCounts
    preconstructed_deck: PreconstructedDeck = None
    phoenixborn_card: CardMinimalOut = None
    phoenixborn_conjurations: list[CardMinimalOut] = None
    related_cards: RelatedCardLists
    entity_id: int = Field(
        ..., description="The card's entity ID (for fetching/posting comments)."
    )
    last_seen_entity_id: int = Field(
        None,
        description=(
            "If the user is subscribed to this card, this will be the highest entity ID for comments that they have "
            "viewed. **Please note:** this only works if comments are displayed in chronological order. Otherwise, the "
            "last seen entity ID will be meaningless (because it relies on the fact that entity IDs are always "
            "increasing)."
        ),
    )


class CardListingOut(PaginatedResultsBase):
    """Filtered listing of cards"""

    results: list[CardOut] = []


class CardType(str, Enum):
    """The various card types in Ashes"""

    ally = "Ally"
    alteration_spell = "Alteration Spell"
    action_spell = "Action Spell"
    reaction_spell = "Reaction Spell"
    ready_spell = "Ready Spell"
    phoenixborn = "Phoenixborn"
    conjuration = "Conjuration"
    conjured_alteration_spell = "Conjured Alteration Spell"


class CardPlacement(str, Enum):
    """The various card placements in Ashes"""

    battlefield = "Battlefield"
    unit = "Unit"
    discard = "Discard"
    spellboard = "Spellboard"
    phoenixborn = "Phoenixborn"


class CardIn(BaseModel):
    name: str = Field(..., min_length=3, max_length=30)
    card_type: CardType
    placement: CardPlacement = None
    release: str = Field(
        ...,
        max_length=60,
        description="The full name of the release this card belongs to.",
    )
    text: str = Field(
        None,
        description="The card effect text, formatting using standard Ashes.live card codes.",
    )
    cost: list[str] | str | None = Field(
        None,
        description=(
            "The cost to play the card formatted with Ashes.live card codes as either a string with costs "
            "separated by ' - ' or a list of strings. Parallel costs should be separated by ' / ' or "
            "the word ' or '.\n\nFor instance, the following cost could be formatted as: `\"[[main]] - "
            '1 [[ceremonial:class]] - 1 [[charm:class]] / 1 [[sympathy:class]]"` or as `["[[main]]", '
            '"1 [[ceremonial:class]]", "1 [[charm:class]] or 1 [[sympathy:class]]"]`'
        ),
    )
    effect_magic_cost: list[str] | str | None = Field(
        None,
        description=(
            "The *magic* cost(s) to activate all card effects as either a string with costs separated by "
            "' - ' or a list of strings. Parallel costs are formatted exactly the same as in the play cost. "
            "\n\nFor instance, a card with two effects, one which costs `[[main]] - 1 [[ceremonial:class]]` "
            'and one that costs `[[main]] - 1 [[sympathy:class]]` would have `"effect_magic_cost": '
            '"1 [[ceremonial:class]] - 1 [[sympathy:class]]"`.\n\n'
            "(This is used in order to calculate the dice necessary to fully activate a card for First "
            "Five calculations and similar.)"
        ),
    )
    can_effect_repeat: bool = Field(
        None,
        description="If an effect can be repeated (i.e. only costs dice and does not exhaust the card), then this should be true (very rare).",
    )
    dice: list[CardDiceCosts] = Field(
        None,
        description="Dice types that are required to play the card or activate its effects. If `null`, will be calculated based on `cost` and `effect_magic_cost`.",
    )
    alt_dice: list[CardDiceCosts] = Field(
        None,
        description="Dice types that are only required by parallel costs, optional effect costs, etc. If `null` will be calculated based on `cost` and `effect_magic_cost`.",
    )
    phoenixborn: str = Field(
        None,
        min_length=3,
        max_length=30,
        description="The full name of the Phoenixborn for whom this card is unique.",
    )
    attack: str = None
    battlefield: str = None
    life: str = None
    recover: str = None
    spellboard: str = None
    copies: int = None

    # TODO[pydantic]: We couldn't refactor the `validator`, please replace it by `field_validator` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-validators for more information.
    @validator("placement", always=True)
    def placement_required_without_phoenixborn(cls, val, values):
        """Placement is required if this isn't a Phoenixborn"""
        if (
            not val
            and "card_type" in values
            and values["card_type"] != CardType.phoenixborn
        ):
            raise ValueError("required for non-Phoenixborn cards")
        return val

    # TODO[pydantic]: We couldn't refactor the `validator`, please replace it by `field_validator` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-validators for more information.
    @validator("copies", always=True)
    def copies_required_for_conjurations(cls, val, values):
        """Copies is required for all conjured cards"""
        if (
            not val
            and "card_type" in values
            and values["card_type"]
            in (CardType.conjuration, CardType.conjured_alteration_spell)
        ):
            raise ValueError("required for conjurations and conjured alteration spells")
        return val

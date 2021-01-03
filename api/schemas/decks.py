from datetime import datetime
from typing import List, Optional, Union, Dict

from fastapi import Query
from pydantic import BaseModel, Field, validator

from api.schemas.pagination import PaginatedResultsBase
from api.schemas.user import UserBasicOut


class DeckFilters:
    """Query string parameters to filter a deck listing"""

    def __init__(
        self,
        q: str = None,
        phoenixborn: Optional[List[str]] = Query(None),
        card: Optional[List[str]] = Query(None),
        player: Optional[List[str]] = Query(None),
        show_legacy: bool = False,
    ):
        self.q = q
        self.phoenixborn = phoenixborn
        self.card = card
        self.player = player
        self.show_legacy = show_legacy


class PhoenixbornCardOut(BaseModel):
    """Minimal card output information"""

    name: str
    stub: str
    battlefield: int
    life: int
    spellboard: int
    is_legacy: bool = None


class DeckCardOut(BaseModel):
    """Output for cards that are included in a deck"""

    count: int
    name: str
    stub: str
    type: str
    phoenixborn: str = None
    is_legacy: bool = None


class DeckDice(BaseModel):
    """Dice associated with the deck"""

    count: int = Field(
        ...,
        ge=1,
        le=10,
    )
    name: str

    @validator("name")
    def name_is_valid_dice_type(cls, value):
        value = value.lower()
        # This is a common mistake, so we'll just handle it (on the off chance people are using the
        #  API by hand)
        if value == "nature":
            value = "natural"
        if value not in (
            "ceremonial",
            "charm",
            "illusion",
            "natural",
            "divine",
            "sympathy",
            "time",
        ):
            raise ValueError("invalid dice type.")
        return value


class DeckOut(BaseModel):
    """The standard JSON output for a deck."""

    id: int
    entity_id: int
    source_id: int = None
    title: str
    created: datetime
    modified: datetime
    user: UserBasicOut
    dice: List[DeckDice]
    phoenixborn: PhoenixbornCardOut
    cards: List[DeckCardOut]
    conjurations: List[DeckCardOut]
    is_legacy: bool = None
    ashes_500_score: int = None
    ashes_500_revision_id: int = None

    class Config:
        orm_mode = True


class DeckFullOut(DeckOut):
    """Full deck information."""

    description: str = None
    is_public: bool
    is_saved: bool = None


class DeckRelease(BaseModel):
    """Information about a release required to build a deck."""

    name: str
    stub: str
    is_legacy: bool = None
    preconstructed_deck_id: int = None


class DeckDetails(BaseModel):
    """JSON output for a deck's details, including required releases and card listing."""

    deck: DeckFullOut
    releases: List[DeckRelease]


class DeckListingOut(PaginatedResultsBase):
    """Filtered listing of decks"""

    results: List[DeckOut] = []


class DeckCardIn(BaseModel):
    """The minimal information necessary to populate a deck with cards."""

    count: int = Field(
        ...,
        description="The quantity of this card to include in the deck.",
        ge=1,
        le=3,
    )
    stub: str


class DeckIn(BaseModel):
    id: int = Field(
        None, description="If no `id` is provided, a new deck will be created."
    )
    title: str = Field(
        None,
        max_length=255,
    )
    description: str = None
    dice: List[DeckDice] = None
    phoenixborn: Union[str, Dict[str, Union[str, int]]] = Field(
        ...,
        description="The stub or an object containing at minimum a `stub` property representing the Phoenixborn for this deck.",
    )
    cards: List[DeckCardIn]
    first_five: List[str] = Field(
        None,
        description="A list of up to five card stubs intended as the typical First Five.",
    )
    effect_costs: List[str] = Field(
        None,
        description="A list of card stubs in the First Five (or the Phoenixborn) whose effects are expected to be paid in the first round.",
    )
    tutor_map: Dict[str, str] = Field(
        None,
        description="An object with tutor card stubs in the First Five as keys, and the tutored card stubs as values.",
    )

from datetime import datetime
from typing import Dict, List, Optional, Union

from fastapi import Query
from pydantic import BaseModel, Field, validator

from api.schemas.pagination import PaginatedResultsBase
from api.schemas.user import UserBasicOut


class DeckFiltersMine:
    """Query string parameters to filter an individual user's deck listing"""

    def __init__(
        self,
        q: str = None,
        phoenixborn: Optional[List[str]] = Query(None),
        card: Optional[List[str]] = Query(None),
        show_legacy: bool = False,
    ):
        self.q = q
        self.phoenixborn = phoenixborn
        self.card = card
        self.show_legacy = show_legacy


class DeckFilters:
    """Query string parameters to filter a deck listing"""

    def __init__(
        self,
        q: str = None,
        phoenixborn: Optional[List[str]] = Query(None),
        card: Optional[List[str]] = Query(None),
        show_legacy: bool = False,
        player: Optional[List[str]] = Query(None),
    ):
        self.q = q
        self.phoenixborn = phoenixborn
        self.card = card
        self.show_legacy = show_legacy
        self.player = player


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


class DeckSaveOut(DeckOut):
    """Full deck information returned from saving endpoint"""

    description: str = None


class DeckFullOut(DeckOut):
    """Full deck information."""

    description: str = None
    is_public: bool
    # These are generated properties; not innate parts of the Deck model
    is_saved: bool = None
    comments_entity_id: int


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
    has_published_snapshot: bool = Field(
        None,
        description="Set to true for private decks and snapshots if they have a public snapshot available.",
    )


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


class SnapshotIn(BaseModel):
    """Optional information when creating a snapshot"""

    title: str = Field(
        None,
        max_length=255,
        description="The title to use specifically for this snapshot; defaults to the current save deck title.",
    )
    description: str = Field(
        None,
        description="The description to use specifically for this snapshot; defaults to the current saved deck description. Pass an empty string to force a blank description.",
    )
    is_public: bool = Field(
        False, description="Whether this snapshot should be published publicly."
    )
    preconstructed_release: str = Field(
        None,
        description="The stub for the release for which this snapshot is the preconstructed deck. Can only be set by site admins.",
    )

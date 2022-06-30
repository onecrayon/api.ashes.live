from datetime import datetime
from typing import Dict, List, Optional, Union

from fastapi import Query
from pydantic import UUID4, BaseModel, Field, validator

from api.schemas import DetailResponse
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
        show_preconstructed: bool = False,
        player: Optional[List[str]] = Query(None),
    ):
        self.q = q
        self.phoenixborn = phoenixborn
        self.card = card
        self.show_legacy = show_legacy
        self.show_preconstructed = show_preconstructed
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
    direct_share_uuid: UUID4 = Field(
        None,
        description="Only included for public snapshots, or decks/snapshots owned by the requesting user. This UUID is used to directly access deck details without requiring authentication (e.g. for private sharing).",
    )
    title: str = None
    created: datetime
    modified: datetime
    user: UserBasicOut
    dice: List[DeckDice]
    phoenixborn: PhoenixbornCardOut
    cards: List[DeckCardOut]
    conjurations: List[DeckCardOut]
    is_public: bool = None
    is_snapshot: bool = None
    is_legacy: bool = None
    ashes_500_score: int = None
    ashes_500_revision_id: int = None

    class Config:
        orm_mode = True


class DeckSaveOut(DeckOut):
    """Full deck information returned from saving endpoint"""

    description: str = None
    first_five: List[str] = Field(
        None,
        description="A list of up to five card stubs intended as the typical First Five. May not be included for public snapshots (owners can opt out of displaying it).",
    )
    effect_costs: List[str] = Field(
        None,
        description="A list of card stubs in the First Five (or the Phoenixborn) whose effects are expected to be paid in the first round. Only included for public snapshots if the First Five is populated.",
    )
    tutor_map: Dict[str, str] = Field(
        None,
        description="An object with tutor card stubs in the First Five as keys, and the tutored card stubs as values. Only included for public snapshots if the First Five is populated.",
    )


class DeckFullOut(DeckSaveOut):
    """Full deck information."""

    # These are generated properties; not innate parts of the Deck model
    is_saved: bool = Field(
        None,
        description="Only included when directly accessing the most recently saved copy of a deck by the owner.",
    )
    comments_entity_id: int = None


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
    include_first_five = Field(
        False,
        description="For public snapshots, whether this snapshot should include your selected First Five cards.",
    )
    preconstructed_release: str = Field(
        None,
        description="The stub for the release for which this snapshot is the preconstructed deck. Can only be set by site admins.",
    )


class SnapshotEditIn(BaseModel):
    """Editable information for snapshots"""

    title: str = Field(
        None, max_length=255, description="The new title to use for this snapshot."
    )
    description: str = Field(
        None, description="The new description to use for this snapshot."
    )
    moderation_notes: str = Field(
        None,
        description="The reason this snapshot was moderated. Can only be set by site admins.",
    )


class SnapshotCreateOut(DetailResponse):
    """Basic information about a just-created snapshot

    The full snapshot data isn't returned because it's identical to the current deck state, which is presumably already
    in the front-end client's memory.
    """

    snapshot_id: int = Field(
        ..., description="The deck ID that links directly to the new snapshot."
    )

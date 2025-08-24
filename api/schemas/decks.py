from datetime import datetime

from fastapi import Query
from pydantic import UUID4, BaseModel, ConfigDict, Field, field_validator

from api.schemas import DetailResponse
from api.schemas.pagination import PaginatedResultsBase
from api.schemas.user import UserBasicOut


class DeckFiltersMine:
    """Query string parameters to filter an individual user's deck listing"""

    def __init__(
        self,
        q: str | None = None,
        phoenixborn: list[str] | None = Query(None),
        card: list[str] | None = Query(None),
        show_legacy: bool = False,
        show_red_rains: bool = False,
    ):
        self.q = q
        self.phoenixborn = phoenixborn
        self.card = card
        self.show_legacy = show_legacy
        self.show_red_rains = show_red_rains


class DeckFilters:
    """Query string parameters to filter a deck listing"""

    def __init__(
        self,
        q: str | None = None,
        phoenixborn: list[str] | None = Query(None),
        card: list[str] | None = Query(None),
        show_legacy: bool = False,
        show_preconstructed: bool = False,
        show_red_rains: bool = False,
        player: list[str] | None = Query(None),
    ):
        self.q = q
        self.phoenixborn = phoenixborn
        self.card = card
        self.show_legacy = show_legacy
        self.show_red_rains = show_red_rains
        self.show_preconstructed = show_preconstructed
        self.player = player


class PhoenixbornCardOut(BaseModel):
    """Minimal card output information"""

    name: str
    stub: str
    battlefield: int
    life: int
    spellboard: int
    is_legacy: bool | None = None


class DeckCardOut(BaseModel):
    """Output for cards that are included in a deck"""

    count: int
    name: str
    stub: str
    type: str
    phoenixborn: str | None = None
    is_legacy: bool | None = None


class DeckDice(BaseModel):
    """Dice associated with the deck"""

    count: int = Field(
        ...,
        ge=1,
        le=10,
    )
    name: str

    @field_validator("name")
    @classmethod
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
    source_id: int | None = None
    direct_share_uuid: UUID4 | None = Field(
        None,
        description="Only included for public snapshots, or decks/snapshots owned by the requesting user. This UUID is used to directly access deck details without requiring authentication (e.g. for private sharing).",
    )
    title: str | None = None
    created: datetime
    modified: datetime
    user: UserBasicOut
    dice: list[DeckDice]
    phoenixborn: PhoenixbornCardOut
    cards: list[DeckCardOut]
    conjurations: list[DeckCardOut]
    is_public: bool | None = None
    is_snapshot: bool | None = None
    is_legacy: bool | None = None
    is_red_rains: bool | None = None
    ashes_500_score: int | None = None
    ashes_500_revision_id: int | None = None

    model_config = ConfigDict(from_attributes=True)


class DeckSaveOut(DeckOut):
    """Full deck information returned from saving endpoint"""

    description: str | None = None
    first_five: list[str] = Field(
        None,
        description="A list of up to five card stubs intended as the typical First Five. May not be included for public snapshots (owners can opt out of displaying it).",
    )
    effect_costs: list[str] = Field(
        None,
        description="A list of card stubs in the First Five (or the Phoenixborn) whose effects are expected to be paid in the first round. Only included for public snapshots if the First Five is populated.",
    )
    tutor_map: dict[str, str] = Field(
        None,
        description="An object with tutor card stubs in the First Five as keys, and the tutored card stubs as values. Only included for public snapshots if the First Five is populated.",
    )


class DeckFullOut(DeckSaveOut):
    """Full deck information."""

    # These are generated properties; not innate parts of the Deck model
    is_saved: bool | None = Field(
        None,
        description="Only included when directly accessing the most recently saved copy of a deck by the owner.",
    )
    comments_entity_id: int | None = None


class DeckExportOut(BaseModel):
    """Representation of a deck for export purposes.

    Because IDs are nonsensical across site instances, the `created` date is treated as the unique identifier for decks
    when exporting them (on the assumption that it is impossible--or at least vanishingly unlikely--for a single user
    to have two decks with identical created dates).
    """

    title: str | None = None
    description: str | None = None
    created: datetime
    modified: datetime
    dice: list[DeckDice]
    phoenixborn: PhoenixbornCardOut
    cards: list[DeckCardOut]
    conjurations: list[DeckCardOut]
    is_public: bool | None = None
    is_snapshot: bool | None = None
    is_red_rains: bool | None = None
    first_five: list[str] | None = None
    effect_costs: list[str] | None = None
    tutor_map: dict[str, str] | None = None

    # This is a generated property, because the root object only knows the source ID
    source_created: datetime | None = None


class DeckExportResults(BaseModel):
    """Listing results for exporting decks"""

    next_page_from_date: datetime | None = Field(
        None, description="The from_date to use to export the next set of decks."
    )
    total: int
    decks: list[DeckExportOut]


class DeckImportOut(BaseModel):
    """Result reporting for deck import requests"""

    next_page_from_date: datetime | None = Field(
        None, description="The from_date to use to export the next set of decks."
    )
    total_count: int = Field(
        0,
        description="The total decks to import (including the successes in this request).",
    )
    success_count: int = Field(
        0, description="The total decks successfully imported in this request."
    )
    errors: list = Field(
        ...,
        description="An array of errors describing which decks failed to import and why.",
    )


class DeckRelease(BaseModel):
    """Information about a release required to build a deck."""

    name: str
    stub: str
    is_legacy: bool | None = None
    preconstructed_deck_id: int | None = None


class DeckDetails(BaseModel):
    """JSON output for a deck's details, including required releases and card listing."""

    deck: DeckFullOut
    releases: list[DeckRelease]
    has_published_snapshot: bool | None = Field(
        None,
        description="Set to true for private decks and snapshots if they have a public snapshot available.",
    )
    last_seen_entity_id: int | None = Field(
        None,
        description=(
            "If the user is subscribed to this deck, this will be the highest entity ID for comments or deck snapshots "
            "that they have viewed. **Please note:** this only works if comments are displayed in chronological order. "
            "Otherwise, the last seen entity ID will be meaningless (because it relies on the fact that entity IDs are "
            "always increasing)."
        ),
    )


class DeckListingOut(PaginatedResultsBase):
    """Filtered listing of decks"""

    results: list[DeckOut] = []


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
    id: int | None = Field(
        None, description="If no `id` is provided, a new deck will be created."
    )
    title: str | None = Field(
        None,
        max_length=255,
    )
    description: str | None = None
    dice: list[DeckDice] = None
    phoenixborn: str | dict[str, str | int] = Field(
        ...,
        description="The stub or an object containing at minimum a `stub` property representing the Phoenixborn for this deck.",
    )
    cards: list[DeckCardIn]
    first_five: list[str] = Field(
        None,
        description="A list of up to five card stubs intended as the typical First Five.",
    )
    effect_costs: list[str] = Field(
        None,
        description="A list of card stubs in the First Five (or the Phoenixborn) whose effects are expected to be paid in the first round.",
    )
    tutor_map: dict[str, str] = Field(
        None,
        description="An object with tutor card stubs in the First Five as keys, and the tutored card stubs as values.",
    )
    is_red_rains: bool = Field(
        False,
        description="May only be changed when creating a new deck or for a deck that has no public snapshots.",
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
    include_first_five: bool = Field(
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

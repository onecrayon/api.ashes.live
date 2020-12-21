from datetime import datetime
from typing import List, Optional

from fastapi import Query
from pydantic import BaseModel

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


class DeckCardOut(BaseModel):
    """Output for cards that are included in a deck"""

    count: int
    name: str
    stub: str
    type: str
    phoenixborn: str = None


class DeckDice(BaseModel):
    """Dice associated with the deck"""

    count: int
    name: str


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


class DeckListingOut(PaginatedResultsBase):
    """Filtered listing of decks"""

    results: List[DeckOut] = []

from datetime import datetime
from typing import List, Optional

from fastapi import Query
from pydantic import BaseModel

from api.schemas.pagination import PaginatedResultsBase


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


class DeckOut(BaseModel):
    """The standard JSON output for a deck."""

    title: str
    created: datetime
    description: str = None
    is_legacy: bool = None

    class Config:
        orm_mode = True


class DeckListingOut(PaginatedResultsBase):
    """Filtered listing of decks"""

    results: List[DeckOut] = []

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

from api.environment import settings


class PaginationOrderOptions(str, Enum):
    """Options for ordering"""

    asc = "asc"
    desc = "desc"


class PaginationOptions(BaseModel):
    """Query string options to adjust pagination"""

    limit: int = Field(
        settings.pagination_default_limit, gt=0, le=settings.pagination_max_limit
    )
    offset: int = 0


class PaginatedResultsBase(BaseModel):
    """Base class for paginated results.

    For proper documentation generation, you must sub-class and override `results`.
    """

    count: int = 0
    next: str | None = None
    previous: str | None = None
    results: list[Any] = []

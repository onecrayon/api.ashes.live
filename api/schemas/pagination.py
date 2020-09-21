from typing import Any, List

from pydantic import BaseModel, Field

from api.environment import settings


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
    next: str = None
    previous: str = None
    results: List[Any] = []

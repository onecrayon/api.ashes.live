from enum import Enum
from typing import Annotated, Any

from pydantic import BaseModel, BeforeValidator, Field

from api.environment import settings


class PaginationOrderOptions(str, Enum):
    """Options for ordering"""

    asc = "asc"
    desc = "desc"


def limit_to_max_pagination_value(value: Any) -> int:
    """Ensures that users cannot exceed the maximum pagination limit

    Needs to be run prior to normal validation to prevent a validation error from getting thrown
    by the framework.
    """
    value = int(value)
    if value > settings.pagination_max_limit:
        value = settings.pagination_max_limit
    return value


class PaginationOptions(BaseModel):
    """Query string options to adjust pagination"""

    limit: Annotated[int, BeforeValidator(limit_to_max_pagination_value)] = Field(
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

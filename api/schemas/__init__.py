"""api.schemas

Pydantic input and output schemas
"""

from pydantic import BaseModel


class DetailResponse(BaseModel):
    """Detail about the reason for success or failure."""

    detail: str

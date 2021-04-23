from pydantic import BaseModel


class ReleaseOut(BaseModel):
    """Basic information about a release.

    `is_mine` is only output when the release is requested by a logged in user with a collection
    set.
    """

    name: str
    stub: str
    is_mine: bool = None
    is_legacy: bool = None

    class Config:
        orm_mode = True

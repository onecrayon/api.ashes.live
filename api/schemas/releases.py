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


class ReleaseOutAdmin(BaseModel):
    """Main information about a release.

    **Admin only.**
    """

    name: str
    stub: str
    is_legacy: bool
    is_public: bool

    class Config:
        orm_mode = True


class ReleaseIn(BaseModel):
    """Information that can be updated about a release; currently only the `is_public` flag."""

    is_public: bool

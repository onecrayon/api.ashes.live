"""api.schemas

Pydantic input and output schemas
"""
from pydantic import BaseModel


class GenericError(BaseModel):
    """Generic error output to allow easy response documentation for endpoints

    Usage:

        from api.schemas import GenericError

        @router.get("/endpoint", responses={401: {"model": GenericError}})
        def my_endpoint():
            raise HTTPException(status_code=401, detail="Some error")
    """

    detail: str

import logging

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.sql.expression import literal_column

from api import db
from api.depends import get_session
from api.schemas.health_check import HealthCheckOut, HealthCheckStatusResponses

logger = logging.getLogger(__name__)

router = APIRouter()

# Construct example error output for OpenAPI spec
_error_out_example = HealthCheckOut()
_error_out_example.services.database = HealthCheckStatusResponses.error
_error_out_example = _error_out_example.has_errors and _error_out_example.model_dump()


@router.get(
    "/health-check",
    tags=["server"],
    response_model=HealthCheckOut,
    responses={
        status.HTTP_503_SERVICE_UNAVAILABLE: {
            "description": "One or more services are down",
            "content": {"application/json": {"example": _error_out_example}},
        }
    },
)
def health_check(response: Response, session: db.Session = Depends(get_session)):
    """Reports on service and overall API status. Please do not hit this endpoint repeatedly;
    it is mainly intended for diagnosing problems internally."""
    # Default okay response
    output = HealthCheckOut()

    # Check for PostgreSQL database health
    try:
        meaning_of_life_the_universe_and_everything = session.query(
            literal_column("42")
        ).scalar()
        assert meaning_of_life_the_universe_and_everything == 42
    except:
        output.services.database = HealthCheckStatusResponses.error
        logger.error("Postgres health-check FAILED", exc_info=True)

    if output.has_errors:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return output

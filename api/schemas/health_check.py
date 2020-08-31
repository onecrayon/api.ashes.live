from enum import Enum

from pydantic import BaseModel


class StatusResponses(str, Enum):
    """Output strings for status responses"""

    okay = "okay"
    error = "error"


class ServicesOut(BaseModel):
    """Nested services status tracking"""

    database: StatusResponses = StatusResponses.okay

    def __iter__(self):
        """Allow iterating over the various services for easy checking for failures"""
        return iter((self.database,))


class HealthCheckOut(BaseModel):
    """Information about API system status"""

    status: StatusResponses = StatusResponses.okay
    services: ServicesOut = ServicesOut()

    @property
    def has_errors(self):
        if any(x == StatusResponses.error for x in self.services):
            self.status = StatusResponses.error
            return True
        return False

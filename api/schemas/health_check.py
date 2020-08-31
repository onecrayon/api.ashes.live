from enum import Enum

from pydantic import BaseModel


class HealthCheckStatusResponses(str, Enum):
    """Output strings for status responses"""

    okay = "okay"
    error = "error"


class HealthCheckServicesOut(BaseModel):
    """Nested services status tracking"""

    database: HealthCheckStatusResponses = HealthCheckStatusResponses.okay

    def __iter__(self):
        """Allow iterating over the various services for easy checking for failures"""
        return iter((self.database,))


class HealthCheckOut(BaseModel):
    """Information about API system status"""

    status: HealthCheckStatusResponses = HealthCheckStatusResponses.okay
    services: HealthCheckServicesOut = HealthCheckServicesOut()

    @property
    def has_errors(self):
        if any(x == HealthCheckStatusResponses.error for x in self.services):
            self.status = HealthCheckStatusResponses.error
            return True
        return False

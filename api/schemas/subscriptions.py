from pydantic import BaseModel


class SubscriptionIn(BaseModel):
    """Used to update a user's subscription to mark what entity IDs they've seen."""

    last_seen_entity_id: int

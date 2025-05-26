from api import db
from api.models.stream import Stream, Streamable, Subscription
from api.utils.dates import utcnow


def create_entity(session: db.Session) -> int:
    """Creates and returns a new entity ID"""
    entity = Streamable()
    session.add(entity)
    session.commit()
    return entity.entity_id


def refresh_stream_for_entity(
    session: db.Session, entity_id: int, entity_type: str, source_entity_id: int
):
    """Creates or updates the Stream entry for the given entity

    **Please note:** this method does not commit the changes! You must flush the session in the
    invoking method.
    """
    if entity_type == "deck":
        entity = (
            session.query(Stream)
            .filter(
                Stream.source_entity_id == source_entity_id,
                Stream.entity_type == "deck",
            )
            .first()
        )
    else:
        entity = session.query(Stream).filter(Stream.entity_id == entity_id).first()
    # Comment edits do not update the stream, hence not handling them here
    if not entity:
        entity = Stream(
            entity_id=entity_id,
            entity_type=entity_type,
            source_entity_id=source_entity_id,
        )
        session.add(entity)
    elif entity_type == "deck":
        # Decks are a special case; we update the Stream entity because the snapshots effectively
        # replace one another as far as most users are concerned
        entity.posted = utcnow()
        entity.entity_id = entity_id
    # TODO: implement emailing logic to update people who are subscribed to this entity?


def update_subscription_for_user(
    session: db.Session,
    user: "User",
    source_entity_id: int,
    last_seen_entity_id: int = None,
):
    """Create or update the user's subscription to the given entity ID.

    **Please note:** this method does not commit the changes! You must flush the session in the
    invoking method.
    """
    subscription = (
        session.query(Subscription)
        .filter(
            Subscription.user_id == user.id,
            Subscription.source_entity_id == source_entity_id,
        )
        .first()
    )
    if not subscription:
        subscription = Subscription(
            user_id=user.id,
            source_entity_id=source_entity_id,
            last_seen_entity_id=last_seen_entity_id,
        )
    else:
        subscription.last_seen_entity_id = last_seen_entity_id
    session.add(subscription)

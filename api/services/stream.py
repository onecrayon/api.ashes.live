from api import db
from api.models.stream import Streamable


def create_entity(session: db.Session) -> int:
    """Creates and returns a new entity ID"""
    entity = Streamable()
    session.add(entity)
    session.commit()
    return entity.entity_id

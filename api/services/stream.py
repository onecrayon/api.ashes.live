from api import db
from api.models.stream import Streamable


def create_entity(session: db.Session) -> int:
    """Creates and returns a new entity ID"""
    entity = Streamable()
    db.session.add(entity)
    db.session.commit()
    return entity.entity_id

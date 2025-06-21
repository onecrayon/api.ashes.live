from datetime import datetime

from api import db

from .user import User


class Streamable(db.AlchemyBase):
    """A Streamable entity is one that can show up in activity streams"""

    __tablename__ = "streamable"
    entity_id = db.Column(db.BigInteger, primary_key=True)


class Stream(db.AlchemyBase):
    """Stream entries are used to construct activity streams"""

    __tablename__ = "stream"
    id = db.Column(db.BigInteger, primary_key=True)
    entity_id = db.Column(db.BigInteger, nullable=False, index=True, unique=True)
    entity_type = db.Column(db.String(16), index=True)
    source_entity_id = db.Column(db.BigInteger, nullable=False, index=True)
    posted = db.Column(db.UTCTimestamp, default=datetime.utcnow, index=True)
    is_legacy = db.Column(db.Boolean, nullable=False, default=False, index=True)


class Subscription(db.AlchemyBase):
    """A Subscription subscribes a user to a Streamable entity's comments"""

    __tablename__ = "subscription"
    user_id = db.Column(
        db.BigInteger, db.ForeignKey(User.id), primary_key=True, nullable=False
    )
    source_entity_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    last_seen_entity_id = db.Column(db.BigInteger, index=True)

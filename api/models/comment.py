from datetime import datetime

from api import db

from .user import User


class Comment(db.AlchemyBase):
    __tablename__ = "comment"
    id = db.Column(db.BigInteger, primary_key=True)
    entity_id = db.Column(db.BigInteger, nullable=False, index=True, unique=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey(User.id), nullable=False)
    # This points to the entity_id being commented on
    source_entity_id = db.Column(db.BigInteger, nullable=False, index=True)
    source_type = db.Column(db.String(16))
    source_version = db.Column(db.BigInteger)
    text = db.Column(db.Text)
    # This is an auto-incrementing integer that is specific to the source_entity_id the comment is associated with. It
    #  is not used by the backend, but it can be used by the front-end to calculate the page that a particular comment
    #  is living on (since the ordering_increment is from oldest to newest and increments by one each time, if you know
    #  the total number of results per page you can determine a comment's page based on its ordering_increment).
    ordering_increment = db.Column(db.BigInteger, index=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False, index=True)
    is_moderated = db.Column(db.Boolean, nullable=False, default=False)
    original_text = db.Column(db.Text)
    moderation_notes = db.Column(db.Text)
    created = db.Column(db.UTCTimestamp, default=datetime.utcnow, index=True)
    modified = db.Column(
        db.UTCTimestamp, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    user = db.relationship(User)

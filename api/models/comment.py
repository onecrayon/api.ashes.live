from datetime import datetime

from api import db
from .user import User


class Comment(db.AlchemyBase):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, nullable=False, index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    # This points to the entity_id being commented on
    source_entity_id = db.Column(db.Integer, nullable=False, index=True)
    source_type = db.Column(db.String(16))
    source_version = db.Column(db.Integer)
    text = db.Column(db.Text)
    order = db.Column(db.Integer, index=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False, index=True)
    is_moderated = db.Column(db.Boolean, nullable=False, default=False)
    original_text = db.Column(db.Text)
    moderation_notes = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship(User)

from datetime import datetime
from random import choice

from api import db
from api.utils.auth import generate_password_hash


class AnonymousUser:
    """Anonymous user base class"""

    def is_anonymous(self) -> bool:
        return True


class User(db.AlchemyBase, AnonymousUser):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True, nullable=False, index=True)
    # Usernames are not unique, but the randomly-generated badge is; e.g. "Skaak#4eh?"
    badge = db.Column(db.String(8), unique=True, nullable=False, index=True)
    username = db.Column(db.String(42), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_banned = db.Column(db.Boolean, nullable=False, default=False)
    moderation_notes = db.Column(db.Text)
    password = db.Column(db.String(255), nullable=False)
    reset_uuid = db.Column(
        db.UUID(as_uuid=True), nullable=True, default=None, index=True, unique=True
    )
    newsletter_opt_in = db.Column(db.Boolean, nullable=False, default=False)
    exclude_subscriptions = db.Column(db.Boolean, nullable=False, default=False)
    email_subscriptions = db.Column(
        db.Boolean, nullable=False, default=False, index=True
    )
    colorize_icons = db.Column(db.Boolean, nullable=False, default=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # `collection` defined via backref in api.models.release.UserRelease

    def is_anonymous(self) -> bool:
        return False

    def set_password(self, password):
        """(Re)set the password after the user has been created"""
        # Hash the password
        self.password = generate_password_hash(password)
        self.reset_uuid = None

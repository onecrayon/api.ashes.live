from datetime import datetime

from api import db


class AnonymousUser:
    """Anonymous user base class"""

    def is_anonymous(self) -> bool:
        return True


class User(db.AlchemyBase, AnonymousUser):
    __tablename__ = "user"
    id = db.Column(db.BigInteger, primary_key=True)
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
    deck_export_uuid = db.Column(
        db.UUID(as_uuid=True), nullable=True, default=None, index=True, unique=True
    )
    newsletter_opt_in = db.Column(db.Boolean, nullable=False, default=False)
    exclude_subscriptions = db.Column(db.Boolean, nullable=False, default=False)
    email_subscriptions = db.Column(
        db.Boolean, nullable=False, default=False, index=True
    )
    colorize_icons = db.Column(db.Boolean, nullable=False, default=False)
    created = db.Column(db.UTCTimestamp, default=datetime.utcnow)
    modified = db.Column(
        db.UTCTimestamp, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # `collection` defined via backref in api.models.release.UserRelease

    def is_anonymous(self) -> bool:
        return False


class UserRevokedToken(db.AlchemyBase):
    """JWT token identifiers that have been explicitly revoked"""

    __tablename__ = "user_revoked_tokens"
    revoked_uuid = db.Column(db.UUID(as_uuid=True), primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey(User.id), nullable=False)
    expires = db.Column(db.UTCTimestamp, nullable=False, index=True)


# Helper for managing user types around the codebase
UserType = AnonymousUser | User

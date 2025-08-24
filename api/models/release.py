from api import db
from api.utils.helpers import stubify

from .user import User


class Release(db.AlchemyBase):
    __tablename__ = "releases"
    __table_args__ = (db.UniqueConstraint("stub", "is_legacy"),)
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    stub = db.Column(db.String(60), nullable=False)
    is_legacy = db.Column(db.Boolean, nullable=False, default=False, index=True)
    is_public = db.Column(db.Boolean, nullable=False, default=False, index=True)
    # These fields are only used by legacy cards
    is_phg = db.Column(db.Boolean, nullable=False, default=False)
    is_promo = db.Column(db.Boolean, nullable=False, default=False)
    is_retiring = db.Column(db.Boolean, nullable=False, default=False)
    # These fields are specifically for Project Phoenix
    designer_name = db.Column(db.String(100), nullable=True)
    designer_url = db.Column(db.String(255), nullable=True)

    def __init__(self, name: str, stub: str = None):
        if not stub:
            stub = stubify(name)
        self.name = name
        self.stub = stub


class UserRelease(db.AlchemyBase):
    __tablename__ = "user_release"
    user_id = db.Column(
        db.BigInteger,
        db.ForeignKey(User.id),
        nullable=False,
        primary_key=True,
        index=True,
    )
    release_id = db.Column(
        db.BigInteger, db.ForeignKey(Release.id), nullable=False, primary_key=True
    )

    user = db.relationship(
        User, backref=db.backref("collection", cascade="all, delete-orphan")
    )

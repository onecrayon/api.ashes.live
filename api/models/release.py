from api import db
from .user import User


class Release(db.AlchemyBase):
    __tablename__ = "releases"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False, unique=True)
    is_phg = db.Column(db.Boolean, nullable=False, default=False)
    is_promo = db.Column(db.Boolean, nullable=False, default=False)
    is_retiring = db.Column(db.Boolean, nullable=False, default=False)
    # These fields are specifically for Project Phoenix
    designer_name = db.Column(db.String(100), nullable=True)
    designer_url = db.Column(db.String(255), nullable=True)


class UserRelease(db.AlchemyBase):
    __tablename__ = "user_release"
    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id), nullable=False, primary_key=True, index=True
    )
    release_id = db.Column(
        db.Integer, db.ForeignKey(Release.id), nullable=False, primary_key=True
    )

    user = db.relationship(
        User, backref=db.backref("collection", cascade="all, delete-orphan")
    )

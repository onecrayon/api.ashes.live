from datetime import datetime

from api import db


class Invite(db.AlchemyBase):
    __tablename__ = "invite"
    uuid = db.Column(db.String(36), primary_key=True)
    email = db.Column(db.String(254), unique=True, nullable=False, index=True)
    requests = db.Column(db.Integer, nullable=False, default=1)
    requested = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

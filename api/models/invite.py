import uuid
from datetime import datetime

from api import db


class Invite(db.AlchemyBase):
    __tablename__ = "invite"
    uuid = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(254), unique=True, nullable=False, index=True)
    requests = db.Column(db.BigInteger, nullable=False, default=1)
    requested = db.Column(
        db.UTCTimestamp, default=datetime.utcnow, onupdate=datetime.utcnow
    )

from datetime import datetime

from api import db


class PhoenixDice(db.AlchemyBase):
    __tablename__ = "phoenix_dice"
    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(254), unique=True, nullable=False, index=True)
    only_official_icons = db.Column(
        db.Boolean, nullable=False, default=False, index=True
    )
    desired_sets = db.Column(db.BigInteger, nullable=False, default=1)
    created = db.Column(db.UTCTimestamp, default=datetime.utcnow)

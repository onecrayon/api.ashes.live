from datetime import datetime

from api import db

from .card import Card


class Ashes500Revision(db.AlchemyBase):
    __tablename__ = "ashes500_revision"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    entity_id = db.Column(db.BigInteger, nullable=False, index=True)
    description = db.Column(db.Text)
    created = db.Column(db.UTCTimestamp, default=datetime.utcnow, index=True)


class Ashes500Value(db.AlchemyBase):
    __tablename__ = "ashes500_value"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    card_id = db.Column(
        db.BigInteger, db.ForeignKey(Card.id), nullable=False, index=True
    )
    revision_id = db.Column(
        db.BigInteger, db.ForeignKey(Ashes500Revision.id), nullable=False, index=True
    )
    combo_card_id = db.Column(
        db.BigInteger, db.ForeignKey(Card.id), nullable=True, default=None
    )
    combo_card_type = db.Column(db.String(25), nullable=True, default=None)
    qty_1 = db.Column(db.SmallInteger, nullable=False)
    qty_2 = db.Column(db.SmallInteger, nullable=True)
    qty_3 = db.Column(db.SmallInteger, nullable=True)

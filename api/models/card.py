from enum import Enum

from sqlalchemy.ext.declarative import declared_attr

from api import db
from .release import Release


class DiceFlags(Enum):
    basic = 0
    ceremonial = 1
    charm = 2
    illusion = 4
    natural = 8
    divine = 16
    sympathy = 32
    time = 64


conjurations_table = db.Table(
    "card_conjuration",
    db.AlchemyBase.metadata,
    db.Column(
        "card_id",
        db.Integer,
        db.ForeignKey("card.id"),
        nullable=False,
        primary_key=True,
    ),
    db.Column(
        "conjuration_id",
        db.Integer,
        db.ForeignKey("card.id"),
        nullable=False,
        primary_key=True,
    ),
)


class Card(db.AlchemyBase):
    __tablename__ = "card"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entity_id = db.Column(db.Integer, nullable=False, index=True, unique=True)
    name = db.Column(db.String(30), nullable=False)
    stub = db.Column(db.String(30), nullable=False)
    phoenixborn = db.Column(db.String(25), nullable=True, index=True)
    release_id = db.Column(
        db.Integer, db.ForeignKey(Release.id), nullable=False, index=True, default=0
    )
    # This gets incremented when a card's text is updated due to errata
    version = db.Column(db.Integer, nullable=False, default=1)
    card_type = db.Column(db.String(25), nullable=False, index=True)
    is_summon_spell = db.Column(db.Boolean, nullable=False, default=False)
    is_legacy = db.Column(db.Boolean, nullable=False, default=False, index=True)
    cost_weight = db.Column(db.Integer, nullable=False, index=True, default=0)
    dice_flags = db.Column(db.Integer, nullable=False, index=True, default=0)
    alt_dice_flags = db.Column(db.Integer, nullable=False, index=True, default=0)
    copies = db.Column(db.SmallInteger, nullable=True, default=None)
    json = db.Column(db.JSONB)
    search_text = db.Column(db.Text)
    # These fields are specifically for Project Phoenix-designed cards
    artist_name = db.Column(db.String(100), nullable=True)
    artist_url = db.Column(db.String(255), nullable=True)

    conjurations = db.relationship(
        "Card",
        secondary=conjurations_table,
        primaryjoin=(id == conjurations_table.c.card_id),
        secondaryjoin=(id == conjurations_table.c.conjuration_id),
        backref="summons",
    )
    release = db.relationship(Release)

    @declared_attr
    def __table_args__(cls):
        return (
            db.UniqueConstraint(cls.name, cls.is_legacy),
            db.UniqueConstraint(cls.stub, cls.is_legacy),
            # Defining this here is technically unnecessary, because alembic can't autogenerate
            #  the index anyway; I like having the database structure fully defined in code, though
            db.Index(
                "ix_card_text_tsv",
                db.func.to_tsvector(cls.search_text),
                postgresql_using="gin",
            ),
        )

    @staticmethod
    def dice_to_flags(dice_list):
        flags = 0
        if not dice_list:
            return flags
        for die in dice_list:
            flags = flags | DiceFlags[die].value
        return flags

    @staticmethod
    def flags_to_dice(flags_int):
        dice = [die.name for die in DiceFlags if die.value & flags_int == die.value]
        return dice if dice else None

    @staticmethod
    def has_any_dice_filter(dice):
        if not dice:
            dice = ["basic"]
        filters = []
        if "basic" in dice:
            filters.append(db.and_(Card.dice_flags == 0, Card.alt_dice_flags == 0))
            dice.remove("basic")
        filters = (
            filters
            + [
                Card.dice_flags.op("&")(DiceFlags[die].value) == DiceFlags[die].value
                for die in dice
            ]
            + [
                Card.alt_dice_flags.op("&")(DiceFlags[die].value)
                == DiceFlags[die].value
                for die in dice
            ]
        )
        return db.or_(*filters)

    @staticmethod
    def has_all_dice_filter(dice):
        flags = Card.dice_to_flags(dice)
        filters = [
            db.or_(
                Card.dice_flags.op("&")(DiceFlags[die].value) == DiceFlags[die].value,
                Card.alt_dice_flags.op("&")(DiceFlags[die].value)
                == DiceFlags[die].value,
            )
            for die in dice
        ]
        return db.and_(*filters)

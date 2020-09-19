from datetime import datetime

from api import db
from .ashes_500 import Ashes500Revision
from .card import Card
from .user import User


class Deck(db.AlchemyBase):
    __tablename__ = "deck"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entity_id = db.Column(db.Integer, nullable=False, index=True, unique=True)
    title = db.Column(db.String(255), index=True)
    description = db.Column(db.Text)
    is_public = db.Column(db.Boolean, nullable=False, default=False, index=True)
    is_snapshot = db.Column(db.Boolean, nullable=False, default=False, index=True)
    is_preconstructed = db.Column(db.Boolean, nullable=False, default=False, index=True)
    is_legacy = db.Column(db.Boolean, nullable=False, default=False, index=True)
    # This is not a ForeignKey because it's usually null
    preconstructed_release = db.Column(db.Integer, index=True)
    created = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    modified = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, index=True
    )
    ashes_500_score = db.Column(db.Integer, nullable=True, default=None)
    ashes_500_revision_id = db.Column(
        db.Integer, db.ForeignKey(Ashes500Revision.id), nullable=True, default=None
    )
    # Snapshots will always have a deck as their source; decks can be sourced from a private
    # snapshot (if the two share a user_id) or any public snapshot
    source_id = db.Column(db.Integer, db.ForeignKey("deck.id"), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False, index=True)
    phoenixborn_id = db.Column(db.Integer, db.ForeignKey(Card.id), index=True)

    user = db.relationship(User)
    phoenixborn = db.relationship(Card)
    source = db.relationship("Deck", uselist=False, remote_side=[id])
    # `cards`, `dice`, and `selected_cards` are defined via backref in the models below


class DeckCard(db.AlchemyBase):
    __tablename__ = "deck_card"
    deck_id = db.Column(
        db.Integer, db.ForeignKey(Deck.id), nullable=False, primary_key=True
    )
    card_id = db.Column(
        db.Integer, db.ForeignKey(Card.id), nullable=False, primary_key=True
    )
    count = db.Column(db.SmallInteger, nullable=False)

    card = db.relationship(Card)
    deck = db.relationship(
        Deck, backref=db.backref("cards", cascade="all, delete-orphan")
    )


class DeckDie(db.AlchemyBase):
    __tablename__ = "deck_die"
    deck_id = db.Column(
        db.Integer, db.ForeignKey(Deck.id), nullable=False, primary_key=True
    )
    die_flag = db.Column(db.Integer, nullable=False, primary_key=True)
    count = db.Column(db.SmallInteger, nullable=False)

    deck = db.relationship(
        Deck, backref=db.backref("dice", cascade="all, delete-orphan")
    )


class DeckSelectedCard(db.AlchemyBase):
    __tablename__ = "deck_selected_card"
    deck_id = db.Column(
        db.Integer, db.ForeignKey(Deck.id), nullable=False, primary_key=True
    )
    card_id = db.Column(
        db.Integer, db.ForeignKey(Card.id), nullable=False, primary_key=True
    )
    tutor_card_id = db.Column(db.Integer, nullable=False, default=0, primary_key=True)
    is_first_five = db.Column(db.Boolean, nullable=False, default=False)
    is_paid_effect = db.Column(db.Boolean, nullable=False, default=False)

    deck = db.relationship(
        Deck, backref=db.backref("selected_cards", cascade="all, delete-orphan")
    )

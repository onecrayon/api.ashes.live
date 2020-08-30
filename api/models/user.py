from datetime import datetime
from random import choice

from api import db


class User(db.AlchemyBase):
    __tablename__ = 'user'
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
    reset_uuid = db.Column(db.String(36), nullable=True, default=None, index=True, unique=True)
    newsletter_opt_in = db.Column(db.Boolean, nullable=False, default=False)
    exclude_subscriptions = db.Column(db.Boolean, nullable=False, default=False)
    email_subscriptions = db.Column(db.Boolean, nullable=False, default=False, index=True)
    colorize_icons = db.Column(db.Boolean, nullable=False, default=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # `collection` defined via backref in api.models.release.UserRelease

    def __init__(self, email, password, badge=None, username=None, description=None,
                 newsletter_opt_in=False):
        self.email = email
        # TODO: hash the password! This approach relies on a Flask module
        # self.password = bcrypt.generate_password_hash(password)
        if badge and re.search(r'^[0-9][a-z0-9*&+=-]+[a-z0-9*!]$', badge):
            self.badge = badge
        else:
            self.badge = User.fetch_badges(True)
        self.username = username if username else choice([
            'Aradel Summergaard', 'Brennen Blackcloud', 'Coal Roarkwin',
            'Dimona Odinstar', 'Jessa Na Ni', 'Leo Sunshadow',
            'Lulu Firststone', 'Maeoni Viper', 'Namine Hymntide',
            'Noah Redmoon', 'Odette Diamondcrest', 'Orrick Gilstream',
            'Rin Northfell', 'Saria Guideman', 'Victoria Glassfire',
            'Echo Greystorm', 'Jericho Kill', 'Astrea', 'Koji Wolfcub',
            'Harold Westraven', 'Sembali Grimtongue', 'Rimea Careworn',
            'Xander Heartsblood', 'Fiona Mercywind', 'James Endersight'
        ])
        self.description = description
        self.newsletter_opt_in = newsletter_opt_in

    def set_password(self, password):
        # TODO: hash the password! This approach relies on a Flask module
        # self.password = bcrypt.generate_password_hash(password)
        self.reset_uuid = None

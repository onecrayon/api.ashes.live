"""Database configuration and convenience access to common SQLAlchemy objects

Typical usage:
    from api import db
    class SomeModel(db.AlchemyBase):
        id = db.Column(db.Integer, primary_key=True)
"""
from sqlalchemy import (
    BigInteger,
    Binary,
    Boolean,
    Column,
    Date,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Index,
    Integer,
    Interval,
    LargeBinary,
    MetaData,
    Numeric,
    PickleType,
    SmallInteger,
    String,
    Table,
    Text,
    Time,
    Unicode,
    UnicodeText,
    alias,
    all_,
    and_,
    any_,
    asc,
    between,
    case,
    cast,
    collate,
    create_engine,
    desc,
    distinct,
    except_,
    except_all,
    exists,
    extract,
    false,
    func,
    funcfilter,
    intersect,
    intersect_all,
    join,
    lateral,
    literal,
    literal_column,
    modifier,
    not_,
    null,
    nullsfirst,
    nullslast,
    or_,
    outerjoin,
    over,
    text,
    true,
    tuple_,
    type_coerce,
    union,
    union_all,
    within_group,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import (
    Session,
    backref,
    relationship,
    sessionmaker,
    Query,
    aliased,
    joinedload,
)
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.engine import RowProxy

from .environment import settings

__all__ = (
    # Local variables and session handling
    "AlchemyBase",
    Session,
    "SessionLocal",
    # SQLAlchemy convenience access
    #  "Holy verbosity, Batman! Why not programmatically include these like in Flask-SQLAlchemy?"
    #  "Well, Robin, I happen to like accurate autocomplete in my editors."
    # Schema shortcuts
    Column,
    ForeignKey,
    # Column type shortcuts
    BigInteger,
    Integer,
    SmallInteger,
    Binary,
    LargeBinary,
    Boolean,
    Date,
    DateTime,
    Time,
    Enum,
    Float,
    Interval,
    Numeric,
    PickleType,
    String,
    Text,
    Unicode,
    UnicodeText,
    UUID,
    JSONB,
    # Relationships
    relationship,
    backref,
    # SQL subset
    alias,
    all_,
    and_,
    any_,
    except_,
    except_all,
    not_,
    or_,
    asc,
    desc,
    between,
    case,
    cast,
    collate,
    distinct,
    exists,
    extract,
    false,
    true,
    null,
    func,
    funcfilter,
    intersect,
    intersect_all,
    join,
    outerjoin,
    lateral,
    literal,
    literal_column,
    modifier,
    nullsfirst,
    nullslast,
    over,
    text,
    tuple_,
    type_coerce,
    union,
    union_all,
    within_group,
    # Schema
    Index,
    Table,
    UniqueConstraint,
    Query,
    RowProxy,
    hybrid_property,
    # ORM
    flag_modified,
    aliased,
    joinedload,
)

# Setup base engine and session class
engine = create_engine(settings.postgres_url, echo=settings.debug)
SessionLocal = sessionmaker(bind=engine)

# Setup our declarative base
meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)
AlchemyBase = declarative_base(metadata=meta)

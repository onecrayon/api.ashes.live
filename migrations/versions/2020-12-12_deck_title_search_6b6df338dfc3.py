"""Deck title search

Revision ID: 6b6df338dfc3
Revises: e3cbe225d553
Create Date: 2020-12-12 04:51:17.527486+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6b6df338dfc3"
down_revision = "e3cbe225d553"
branch_labels = None
depends_on = None


def upgrade():
    # This index was necessary for full text search in MySQL, but PostgreSQL works differently
    op.drop_index("ix_deck_title", table_name="deck")
    # Now we need a GIN index on a tsvector
    op.create_index(
        "ix_deck_title_tsv",
        "deck",
        [sa.text("to_tsvector('english'::regconfig, title)")],
        postgresql_using="gin",
    )


def downgrade():
    op.drop_index("ix_deck_title_tsv", table_name="deck")
    op.create_index("ix_deck_title", "deck", ["title"], unique=False)

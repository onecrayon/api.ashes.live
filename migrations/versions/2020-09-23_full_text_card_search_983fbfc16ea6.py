"""Full text Card search

Revision ID: 983fbfc16ea6
Revises: e037174fcbdc
Create Date: 2020-09-23 03:30:52.556239+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "983fbfc16ea6"
down_revision = "e037174fcbdc"
branch_labels = None
depends_on = None


def upgrade():
    # This index was necessary for full text search in MySQL, but PostgreSQL works differently
    op.drop_index("ix_card_text", table_name="card")
    # These indexes are no longer necessary now that we're unique based on the is_legacy flag
    op.drop_index("ix_card_name", table_name="card")
    op.drop_index("ix_card_stub", table_name="card")
    # And finally switch things up a little so that full text search works properly
    op.alter_column("card", "text", new_column_name="search_text")
    # Concatenate our card names into the text column
    op.execute("UPDATE card SET search_text = trim(name || E'\\n' || search_text)")
    # Now we need a GIN index on a tsvector
    op.create_index(
        "ix_card_text_tsv",
        "card",
        [sa.text("to_tsvector('english'::regconfig, search_text)")],
        postgresql_using="gin",
    )


def downgrade():
    op.drop_index("ix_card_text_tsv", table_name="card")
    op.execute("UPDATE card SET search_text = split_part(search_text, E'\\n', 2)")
    op.alter_column("card", "search_text", new_column_name="text")
    op.create_index("ix_card_stub", "card", ["stub"], unique=False)
    op.create_index("ix_card_name", "card", ["name"], unique=False)
    op.create_index("ix_card_text", "card", ["name", "text"], unique=False)

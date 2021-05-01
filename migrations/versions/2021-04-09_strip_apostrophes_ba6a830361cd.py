"""Strip apostrophes

Revision ID: ba6a830361cd
Revises: d20f98cdadb3
Create Date: 2021-04-09 03:13:46.082822+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ba6a830361cd"
down_revision = "d20f98cdadb3"
branch_labels = None
depends_on = None


def upgrade():
    # We need to strip out apostrophes from all card search_text so that those words will be treated as lexemes
    conn = op.get_bind()
    conn.execute("UPDATE card SET search_text = replace(search_text, '''', '')")


def downgrade():
    pass

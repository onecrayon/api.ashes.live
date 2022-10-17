"""Chinese support

Revision ID: 34119bd8b577
Revises: bea881b08e72
Create Date: 2022-10-17 03:57:34.996730+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "34119bd8b577"
down_revision = "bea881b08e72"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("card", sa.Column("name_zh", sa.String(length=30), nullable=True))
    op.add_column("card", sa.Column("stub_zh", sa.String(length=30), nullable=True))
    op.add_column(
        "card",
        sa.Column("json_zh", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    )
    op.create_index(op.f("ix_card_stub_zh"), "card", ["stub_zh"], unique=False)
    op.add_column(
        "deck",
        sa.Column("lang", sa.String(length=2), server_default="en", nullable=False),
    )
    op.add_column("releases", sa.Column("name_zh", sa.String(length=60), nullable=True))
    op.add_column("releases", sa.Column("stub_zh", sa.String(length=60), nullable=True))
    op.create_index(op.f("ix_releases_stub_zh"), "releases", ["stub_zh"], unique=False)


def downgrade():
    op.drop_column("releases", "stub_zh")
    op.drop_column("releases", "name_zh")
    op.drop_column("deck", "lang")
    op.drop_column("card", "json_zh")
    op.drop_column("card", "stub_zh")
    op.drop_column("card", "name_zh")

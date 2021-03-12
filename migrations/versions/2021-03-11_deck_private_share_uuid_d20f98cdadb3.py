"""Deck private share UUID

Revision ID: d20f98cdadb3
Revises: 74e98d76716e
Create Date: 2021-03-11 14:50:51.449344+00:00

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "d20f98cdadb3"
down_revision = "74e98d76716e"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "deck",
        sa.Column(
            "direct_share_uuid",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
    )
    op.create_index(
        op.f("ix_deck_direct_share_uuid"), "deck", ["direct_share_uuid"], unique=True
    )


def downgrade():
    op.drop_column("deck", "direct_share_uuid")

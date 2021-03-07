"""Deck deletions

Revision ID: 74e98d76716e
Revises: c63e4dc58694
Create Date: 2021-02-21 05:20:11.964522+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "74e98d76716e"
down_revision = "c63e4dc58694"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "deck",
        sa.Column("is_deleted", sa.Boolean(), nullable=False, server_default="0"),
    )
    op.create_index(op.f("ix_deck_is_deleted"), "deck", ["is_deleted"], unique=False)


def downgrade():
    op.drop_column("deck", "is_deleted")

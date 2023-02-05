"""Red Rains for Decks

Revision ID: d8355888887b
Revises: bea881b08e72
Create Date: 2023-02-05 17:58:19.001122+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d8355888887b"
down_revision = "bea881b08e72"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("deck", sa.Column("is_red_rains", sa.Boolean(), nullable=False, server_default='0'))
    op.create_index(
        op.f("ix_deck_is_red_rains"), "deck", ["is_red_rains"], unique=False
    )


def downgrade():
    op.drop_column("deck", "is_red_rains")

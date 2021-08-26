"""Deck moderation

Revision ID: bea881b08e72
Revises: ba6a830361cd
Create Date: 2021-08-26 15:47:27.539989+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bea881b08e72"
down_revision = "ba6a830361cd"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("deck", sa.Column("is_moderated", sa.Boolean(), nullable=False))
    op.add_column("deck", sa.Column("original_description", sa.Text(), nullable=True))
    op.add_column("deck", sa.Column("moderation_notes", sa.Text(), nullable=True))


def downgrade():
    op.drop_column("deck", "moderation_notes")
    op.drop_column("deck", "original_description")
    op.drop_column("deck", "is_moderated")

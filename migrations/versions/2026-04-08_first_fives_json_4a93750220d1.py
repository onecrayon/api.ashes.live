"""First Fives JSON

Revision ID: 4a93750220d1
Revises: 489f5ba99de2
Create Date: 2026-04-08 15:01:30.056287+00:00

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "4a93750220d1"
down_revision = "489f5ba99de2"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "deck",
        sa.Column(
            "first_fives", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
    )


def downgrade():
    op.drop_column("deck", "first_fives")

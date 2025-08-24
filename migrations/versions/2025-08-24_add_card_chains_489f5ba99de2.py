"""Add card chains

Revision ID: 489f5ba99de2
Revises: b5e78986c4b6
Create Date: 2025-08-24 15:46:54.114706+00:00

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "489f5ba99de2"
down_revision = "b5e78986c4b6"
branch_labels = None
depends_on = None


def upgrade():
    # Update all cards with default chain status
    op.execute(
        """
        UPDATE card SET "json" = "json" || '{"chained": false}'::jsonb
        WHERE is_legacy = FALSE
        """
    )
    op.execute(
        """
        UPDATE card SET "json" = "json" || '{"chained": true}'::jsonb
        WHERE is_legacy = FALSE AND stub IN (
            'explosive-growth',
            'golden-veil',
            'hypnotize',
            'psychic-vampire',
            'river-skald',
            'summon-shining-hydra',
            'meteor'
        )
        """
    )


def downgrade():
    op.execute(
        """
        UPDATE card SET "json" = "json" - 'chained'
        WHERE is_legacy = FALSE
        """
    )

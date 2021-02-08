"""Phoenixborn unique card search text

Revision ID: c63e4dc58694
Revises: 00a3f50d70fc
Create Date: 2021-02-08 06:42:12.171358+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c63e4dc58694"
down_revision = "00a3f50d70fc"
branch_labels = None
depends_on = None


def upgrade():
    # We need to upgrade the search text for cards to include the Phoenixborn's name if it's a unique
    conn = op.get_bind()
    unique_cards = conn.execute(
        """
        SELECT id, phoenixborn, search_text
        FROM card
        WHERE phoenixborn IS NOT NULL
        """
    ).fetchall()
    for card in unique_cards:
        exploded_search_text = card["search_text"].split("\n")
        if exploded_search_text[1] == card["phoenixborn"]:
            continue
        exploded_search_text.insert(1, card["phoenixborn"])
        search_text = "\n".join(exploded_search_text)
        conn.execute(
            sa.text("UPDATE card SET search_text = :search_text WHERE id = :id"),
            search_text=search_text,
            id=card["id"],
        )


def downgrade():
    pass

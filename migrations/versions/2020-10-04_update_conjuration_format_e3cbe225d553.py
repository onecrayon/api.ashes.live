"""Update conjuration format

Revision ID: e3cbe225d553
Revises: ea070da9abd9
Create Date: 2020-10-04 03:05:12.861613+00:00

"""
import json
import re

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e3cbe225d553"
down_revision = "ea070da9abd9"
branch_labels = None
depends_on = None


def upgrade():
    # Go through all cards and update their conjurations array to use an object with name and stub
    conn = op.get_bind()
    cards = conn.execute(
        "SELECT DISTINCT ON (id) id, json FROM card INNER JOIN card_conjuration AS conj ON conj.card_id = card.id"
    ).fetchall()
    for card in cards:
        json_data = card["json"]
        conj_data = []
        for name in json_data["conjurations"]:
            conj_data.append(
                {
                    "name": name,
                    "stub": re.sub(
                        r"[^a-z0-9-]",
                        "",
                        name.strip().lower().replace(" ", "-"),
                        flags=re.I,
                    ),
                }
            )
        json_data["conjurations"] = conj_data
        conn.execute(
            sa.text("UPDATE card SET json = :json_data WHERE id = :id"),
            json_data=json.dumps(json_data, separators=(",", ":"), sort_keys=True),
            id=card["id"],
        )


def downgrade():
    # And back to names only
    conn = op.get_bind()
    cards = conn.execute(
        "SELECT DISTINCT ON (id) id, json FROM card INNER JOIN card_conjuration AS conj ON conj.card_id = card.id"
    ).fetchall()
    for card in cards:
        json_data = card["json"]
        conj_names = []
        for conj_data in json_data["conjurations"]:
            conj_names.append(conj_data["name"])
        json_data["conjurations"] = conj_names
        conn.execute(
            sa.text("UPDATE card SET json = :json_data WHERE id = :id"),
            json_data=json.dumps(json_data, separators=(",", ":"), sort_keys=True),
            id=card["id"],
        )

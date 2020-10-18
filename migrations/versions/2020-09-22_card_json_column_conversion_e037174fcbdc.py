"""Card JSON column conversion

Revision ID: e037174fcbdc
Revises: 227bda0f6448
Create Date: 2020-09-22 14:07:04.320398+00:00

"""
import json

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e037174fcbdc"
down_revision = "227bda0f6448"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        "card",
        "json",
        type_=sa.dialects.postgresql.JSONB,
        postgresql_using="json::jsonb",
    )
    # Strip out IDs and images, add `is_legacy` flag, and flatten effect text into a string
    conn = op.get_bind()
    cards = conn.execute('SELECT id, is_legacy, "json" FROM card').fetchall()
    for card in cards:
        data = card["json"]
        if card["is_legacy"]:
            data["is_legacy"] = True
        try:
            del data["id"]
            del data["images"]
        except KeyError:
            pass
        if "text" in data and not isinstance(data["text"], str):
            textList = []
            for entry in data["text"]:
                entryList = []
                if "inexhaustible" in entry and entry["inexhaustible"]:
                    entryList.append("*")
                elif "betweenRealms" in entry and entry["betweenRealms"]:
                    entryList.append("~")
                if "name" in entry:
                    entryList.append(f"{entry['name']}:")
                if "cost" in entry:
                    entryList.append(f"{' - '.join(entry['cost'])}:")
                if "text" in entry:
                    entryList.append(entry["text"])
                textList.append(" ".join(entryList))
            data["text"] = "\n\n".join(textList)
        if "release" in data:
            try:
                del data["release"]["id"]
            except KeyError:
                pass
            if card["is_legacy"]:
                data["release"]["is_legacy"] = True
            data["release"]["stub"] = data["release"]["name"].replace(" ", "-").lower()
        conn.execute(
            sa.text("UPDATE card SET json = CAST(:data AS jsonb) WHERE id = :id"),
            data=json.dumps(data),
            id=card["id"],
        )


def downgrade():
    op.alter_column("card", "json", type_=sa.TEXT, postgresql_using="json::text")

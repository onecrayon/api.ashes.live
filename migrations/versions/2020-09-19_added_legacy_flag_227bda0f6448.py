"""Added legacy flag

Revision ID: 227bda0f6448
Revises: e697db57d287
Create Date: 2020-09-19 18:23:26.608488+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "227bda0f6448"
down_revision = "e697db57d287"
branch_labels = None
depends_on = None


def upgrade():
    # Generate legacy flags and related indexes
    op.add_column(
        "card",
        sa.Column("is_legacy", sa.Boolean(), nullable=False, server_default="0"),
    )
    op.create_index(op.f("ix_card_is_legacy"), "card", ["is_legacy"], unique=False)
    op.create_unique_constraint(op.f("uq_card_name"), "card", ["name", "is_legacy"])
    op.create_unique_constraint(op.f("uq_card_stub"), "card", ["stub", "is_legacy"])
    op.drop_index("ix_card_name", table_name="card")
    op.create_index(op.f("ix_card_name"), "card", ["name"], unique=False)
    op.drop_index("ix_card_stub", table_name="card")
    op.create_index(op.f("ix_card_stub"), "card", ["stub"], unique=False)
    op.add_column(
        "deck",
        sa.Column("is_legacy", sa.Boolean(), nullable=False, server_default="0"),
    )
    op.create_index(op.f("ix_deck_is_legacy"), "deck", ["is_legacy"], unique=False)
    op.add_column(
        "post",
        sa.Column("is_legacy", sa.Boolean(), nullable=False, server_default="0"),
    )
    op.create_index(op.f("ix_post_is_legacy"), "post", ["is_legacy"], unique=False)
    op.add_column(
        "releases",
        sa.Column("is_legacy", sa.Boolean(), nullable=False, server_default="0"),
    )
    op.create_index(
        op.f("ix_releases_is_legacy"), "releases", ["is_legacy"], unique=False
    )
    op.add_column(
        "stream",
        sa.Column("is_legacy", sa.Boolean(), nullable=False, server_default="0"),
    )
    op.create_index(op.f("ix_stream_is_legacy"), "stream", ["is_legacy"], unique=False)

    # Now that we have the legacy flag, mark everything that's currently in the database as legacy
    op.execute("UPDATE card SET is_legacy = TRUE")
    op.execute("UPDATE deck SET is_legacy = TRUE")
    op.execute("UPDATE post SET is_legacy = TRUE")
    op.execute("UPDATE releases SET is_legacy = TRUE")
    op.execute("UPDATE stream SET is_legacy = TRUE")


def downgrade():
    op.drop_index(op.f("ix_stream_is_legacy"), table_name="stream")
    op.drop_column("stream", "is_legacy")
    op.drop_index(op.f("ix_releases_is_legacy"), table_name="releases")
    op.drop_column("releases", "is_legacy")
    op.drop_index(op.f("ix_post_is_legacy"), table_name="post")
    op.drop_column("post", "is_legacy")
    op.drop_index(op.f("ix_deck_is_legacy"), table_name="deck")
    op.drop_column("deck", "is_legacy")
    op.drop_index(op.f("ix_card_stub"), table_name="card")
    op.create_index("ix_card_stub", "card", ["stub"], unique=True)
    op.drop_index(op.f("ix_card_name"), table_name="card")
    op.create_index("ix_card_name", "card", ["name"], unique=True)
    op.drop_constraint(op.f("uq_card_stub"), "card", type_="unique")
    op.drop_constraint(op.f("uq_card_name"), "card", type_="unique")
    op.drop_index(op.f("ix_card_is_legacy"), table_name="card")
    op.drop_column("card", "is_legacy")

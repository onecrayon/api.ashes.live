"""Deck exporting

Revision ID: b5e78986c4b6
Revises: c1d8d8b6925f
Create Date: 2025-05-24 15:31:51.532998+00:00

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "b5e78986c4b6"
down_revision = "c1d8d8b6925f"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "deck",
        sa.Column("is_exported", sa.Boolean(), nullable=False, server_default="0"),
    )
    op.add_column(
        "user",
        sa.Column("deck_export_uuid", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.create_index(
        op.f("ix_user_deck_export_uuid"), "user", ["deck_export_uuid"], unique=True
    )
    op.alter_column(
        "user_revoked_tokens",
        "user_id",
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )
    op.alter_column(
        "user_revoked_tokens",
        "expires",
        existing_type=postgresql.TIMESTAMP(),
        type_=postgresql.TIMESTAMP(timezone=True),
        existing_nullable=False,
    )


def downgrade():
    op.alter_column(
        "user_revoked_tokens",
        "expires",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=False,
    )
    op.alter_column(
        "user_revoked_tokens",
        "user_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.drop_index(op.f("ix_user_deck_export_uuid"), table_name="user")
    op.drop_column("user", "deck_export_uuid")
    op.drop_column("deck", "is_exported")

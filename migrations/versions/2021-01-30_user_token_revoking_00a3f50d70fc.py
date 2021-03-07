"""User token revoking

Revision ID: 00a3f50d70fc
Revises: 6b6df338dfc3
Create Date: 2021-01-30 15:52:32.240423+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "00a3f50d70fc"
down_revision = "6b6df338dfc3"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user_revoked_tokens",
        sa.Column("revoked_uuid", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("expires", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name=op.f("fk_user_revoked_tokens_user_id_user")
        ),
        sa.PrimaryKeyConstraint("revoked_uuid", name=op.f("pk_user_revoked_tokens")),
    )
    op.create_index(
        op.f("ix_user_revoked_tokens_expires"),
        "user_revoked_tokens",
        ["expires"],
        unique=False,
    )


def downgrade():
    op.drop_table("user_revoked_tokens")

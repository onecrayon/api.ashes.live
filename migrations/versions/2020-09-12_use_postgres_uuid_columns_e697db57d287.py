"""Use Postgres UUID columns

Revision ID: e697db57d287
Revises: de48fc5206e4
Create Date: 2020-09-12 16:52:10.525424+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "e697db57d287"
down_revision = "de48fc5206e4"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("invite", "uuid", type_=UUID(), postgresql_using="uuid::uuid")
    op.alter_column(
        "user", "reset_uuid", type_=UUID(), postgresql_using="reset_uuid::uuid"
    )


def downgrade():
    op.alter_column("invite", "uuid", type_=sa.VARCHAR(36))
    op.alter_column("user", "reset_uuid", type_=sa.VARCHAR(36))

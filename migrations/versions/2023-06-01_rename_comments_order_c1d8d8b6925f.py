"""Rename comments order

Revision ID: c1d8d8b6925f
Revises: d8355888887b
Create Date: 2023-06-01 18:39:14.788886+00:00

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c1d8d8b6925f"
down_revision = "d8355888887b"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        "comment", "order", nullable=True, new_column_name="ordering_increment"
    )
    op.drop_index("ix_comment_order", table_name="comment")
    op.create_index(
        op.f("ix_comment_ordering_increment"),
        "comment",
        ["ordering_increment"],
        unique=False,
    )


def downgrade():
    op.alter_column(
        "comment", "ordering_increment", nullable=True, new_column_name="order"
    )
    op.drop_index(op.f("ix_comment_ordering_increment"), table_name="comment")
    op.create_index("ix_comment_order", "comment", ["order"], unique=False)

"""Release updates

Revision ID: ea070da9abd9
Revises: 983fbfc16ea6
Create Date: 2020-10-01 04:20:28.340679+00:00

"""
from alembic import op
import sqlalchemy as sa

from api.utils.helpers import stubify


# revision identifiers, used by Alembic.
revision = "ea070da9abd9"
down_revision = "983fbfc16ea6"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "releases",
        sa.Column("is_public", sa.Boolean(), nullable=False, server_default="0"),
    )
    # Releases default to not public, but all legacy releases need to be marked public by default
    op.execute("UPDATE releases SET is_public = TRUE WHERE is_legacy IS TRUE")
    # We have to add this column as nullable first, so that we can populate it without errors
    op.add_column("releases", sa.Column("stub", sa.String(length=60), nullable=True))
    conn = op.get_bind()
    releases = conn.execute("SELECT id, name FROM releases").fetchall()
    for release in releases:
        conn.execute(
            f"UPDATE releases SET stub = '{stubify(release['name'])}' WHERE id = {release['id']}"
        )
    op.alter_column("releases", "stub", nullable=False)
    op.create_index(
        op.f("ix_releases_is_public"), "releases", ["is_public"], unique=False
    )
    op.create_unique_constraint(
        op.f("uq_releases_stub"), "releases", ["stub", "is_legacy"]
    )
    op.drop_constraint("uq_releases_name", "releases", type_="unique")


def downgrade():
    op.create_unique_constraint("uq_releases_name", "releases", ["name"])
    op.drop_constraint(op.f("uq_releases_stub"), "releases", type_="unique")
    op.drop_index(op.f("ix_releases_is_public"), table_name="releases")
    op.drop_column("releases", "stub")
    op.drop_column("releases", "is_public")

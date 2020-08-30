"""legacy_starting_point

Revision ID: 8995c5200c07
Revises: 
Create Date: 2020-08-30 06:48:48.958520+00:00

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.schema import DropTable
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "c58a815a71a0"
down_revision = None
branch_labels = None
depends_on = None


@compiles(DropTable, "postgresql")
def _compile_drop_table(element, compiler, **kwargs):
    """Adds DROP ... CASCADE to PostgreSQL drop statements

    https://stackoverflow.com/a/38679457
    """
    return compiler.visit_drop_table(element) + " CASCADE"


def upgrade():
    # Creates all tables and indexes to match the legacy database schema (only necessary if
    #  building the API from scratch; the live site will migrate data and schema over from MySQL)
    op.create_table(
        "user",
        sa.Column(
            "id",
            sa.BIGINT(),
            server_default=sa.text("nextval('user_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("email", sa.VARCHAR(length=254), autoincrement=False, nullable=False),
        sa.Column("badge", sa.VARCHAR(length=8), autoincrement=False, nullable=False),
        sa.Column(
            "username", sa.VARCHAR(length=42), autoincrement=False, nullable=False
        ),
        sa.Column(
            "password", sa.VARCHAR(length=255), autoincrement=False, nullable=False
        ),
        sa.Column(
            "created",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "modified",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "reset_uuid", sa.VARCHAR(length=36), autoincrement=False, nullable=True
        ),
        sa.Column(
            "newsletter_opt_in", sa.BOOLEAN(), autoincrement=False, nullable=False
        ),
        sa.Column("description", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "is_admin",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "exclude_subscriptions",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "is_banned",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("moderation_notes", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "email_subscriptions", sa.BOOLEAN(), autoincrement=False, nullable=False
        ),
        sa.Column("colorize_icons", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="idx_17073_primary"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("idx_17073_ix_user_reset_uuid", "user", ["reset_uuid"], unique=True)
    op.create_index(
        "idx_17073_ix_user_email_subscriptions",
        "user",
        ["email_subscriptions"],
        unique=False,
    )
    op.create_index("idx_17073_ix_user_email", "user", ["email"], unique=True)
    op.create_index("idx_17073_ix_user_badge", "user", ["badge"], unique=True)

    op.create_table(
        "releases",
        sa.Column(
            "id",
            sa.BIGINT(),
            server_default=sa.text("nextval('releases_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("name", sa.VARCHAR(length=60), autoincrement=False, nullable=False),
        sa.Column(
            "is_phg",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "is_promo",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "designer_name", sa.VARCHAR(length=100), autoincrement=False, nullable=True
        ),
        sa.Column(
            "designer_url", sa.VARCHAR(length=255), autoincrement=False, nullable=True
        ),
        sa.Column("is_retiring", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="idx_17031_primary"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("idx_17031_name", "releases", ["name"], unique=True)

    op.create_table(
        "card",
        sa.Column(
            "id",
            sa.BIGINT(),
            server_default=sa.text("nextval('card_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("name", sa.VARCHAR(length=30), autoincrement=False, nullable=False),
        sa.Column("stub", sa.VARCHAR(length=30), autoincrement=False, nullable=False),
        sa.Column("json", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "release_id",
            sa.BIGINT(),
            server_default=sa.text("'0'::bigint"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "card_type", sa.VARCHAR(length=25), autoincrement=False, nullable=False
        ),
        sa.Column("cost_weight", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column(
            "dice_flags",
            sa.BIGINT(),
            server_default=sa.text("'0'::bigint"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "phoenixborn", sa.VARCHAR(length=25), autoincrement=False, nullable=True
        ),
        sa.Column("copies", sa.SMALLINT(), autoincrement=False, nullable=True),
        sa.Column(
            "is_summon_spell",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("text", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "alt_dice_flags",
            sa.BIGINT(),
            server_default=sa.text("'0'::bigint"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("entity_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column(
            "version",
            sa.BIGINT(),
            server_default=sa.text("'1'::bigint"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "artist_name", sa.VARCHAR(length=100), autoincrement=False, nullable=True
        ),
        sa.Column(
            "artist_url", sa.VARCHAR(length=255), autoincrement=False, nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["release_id"],
            ["releases.id"],
            name="card_release_ibfk_1",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("id", name="idx_16961_primary"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("idx_16961_ix_card_text", "card", ["name", "text"], unique=False)
    op.create_index("idx_16961_ix_card_stub", "card", ["stub"], unique=True)
    op.create_index(
        "idx_16961_ix_card_release_id", "card", ["release_id"], unique=False
    )
    op.create_index(
        "idx_16961_ix_card_phoenixborn", "card", ["phoenixborn"], unique=False
    )
    op.create_index("idx_16961_ix_card_name", "card", ["name"], unique=True)
    op.create_index("idx_16961_ix_card_entity_id", "card", ["entity_id"], unique=True)
    op.create_index(
        "idx_16961_ix_card_dice_flags", "card", ["dice_flags"], unique=False
    )
    op.create_index(
        "idx_16961_ix_card_cost_weight", "card", ["cost_weight"], unique=False
    )
    op.create_index("idx_16961_ix_card_card_type", "card", ["card_type"], unique=False)
    op.create_index(
        "idx_16961_ix_card_alt_dice_flags", "card", ["alt_dice_flags"], unique=False
    )

    op.create_table(
        "comment",
        sa.Column("id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.Column("entity_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("user_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("source_entity_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column(
            "source_type", sa.VARCHAR(length=16), autoincrement=False, nullable=True
        ),
        sa.Column("source_version", sa.BIGINT(), autoincrement=False, nullable=True),
        sa.Column("text", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("order", sa.BIGINT(), autoincrement=False, nullable=True),
        sa.Column(
            "is_deleted",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "is_moderated",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("original_text", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("moderation_notes", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "created",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "modified",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name="comment_ibfk_1",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("id", name="idx_16978_primary"),
    )
    op.create_index("idx_16978_user_id", "comment", ["user_id"], unique=False)
    op.create_index(
        "idx_16978_ix_comment_source_entity_id",
        "comment",
        ["source_entity_id"],
        unique=False,
    )
    op.create_index("idx_16978_ix_comment_order", "comment", ["order"], unique=False)
    op.create_index(
        "idx_16978_ix_comment_is_deleted", "comment", ["is_deleted"], unique=False
    )
    op.create_index(
        "idx_16978_ix_comment_entity_id", "comment", ["entity_id"], unique=True
    )
    op.create_index(
        "idx_16978_ix_comment_created", "comment", ["created"], unique=False
    )

    op.create_table(
        "section",
        sa.Column(
            "id",
            sa.BIGINT(),
            server_default=sa.text("nextval('section_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("entity_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("title", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column("stub", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column("description", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "is_restricted",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name="idx_17039_primary"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("idx_17039_ix_section_stub", "section", ["stub"], unique=True)
    op.create_index(
        "idx_17039_ix_section_is_restricted", "section", ["is_restricted"], unique=False
    )
    op.create_index(
        "idx_17039_ix_section_entity_id", "section", ["entity_id"], unique=True
    )

    op.create_table(
        "card_conjuration",
        sa.Column("card_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("conjuration_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["card_id"],
            ["card.id"],
            name="card_conjuration_ibfk_1",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["conjuration_id"],
            ["card.id"],
            name="card_conjuration_ibfk_2",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("card_id", "conjuration_id", name="idx_16973_primary"),
    )
    op.create_index(
        "idx_16973_conjuration_id", "card_conjuration", ["conjuration_id"], unique=False
    )

    op.create_table(
        "ashes500_revision",
        sa.Column(
            "id",
            sa.BIGINT(),
            server_default=sa.text("nextval('ashes500_revision_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("entity_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("description", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "created",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="idx_16946_primary"),
        postgresql_ignore_search_path=False,
    )
    op.create_index(
        "idx_16946_ix_ashes500_revision_entity_id",
        "ashes500_revision",
        ["entity_id"],
        unique=False,
    )
    op.create_index(
        "idx_16946_ix_ashes500_revision_created",
        "ashes500_revision",
        ["created"],
        unique=False,
    )

    op.create_table(
        "deck",
        sa.Column("id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.Column("title", sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.Column("description", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "is_public",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "created",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "modified",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("user_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("phoenixborn_id", sa.BIGINT(), autoincrement=False, nullable=True),
        sa.Column("is_snapshot", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column("source_id", sa.BIGINT(), autoincrement=False, nullable=True),
        sa.Column(
            "is_preconstructed",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("entity_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column(
            "ashes_500_revision_id", sa.BIGINT(), autoincrement=False, nullable=True
        ),
        sa.Column("ashes_500_score", sa.BIGINT(), autoincrement=False, nullable=True),
        sa.Column(
            "preconstructed_release", sa.BIGINT(), autoincrement=False, nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["ashes_500_revision_id"],
            ["ashes500_revision.id"],
            name="fk_ashes_500_revision_id",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["phoenixborn_id"],
            ["card.id"],
            name="deck_ibfk_1",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["deck.id"],
            name="deck_ibfk_3",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name="deck_ibfk_2",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("id", name="idx_16989_primary"),
    )
    op.create_index("idx_16989_ix_deck_user_id", "deck", ["user_id"], unique=False)
    op.create_index("idx_16989_ix_deck_title", "deck", ["title"], unique=False)
    op.create_index("idx_16989_ix_deck_source_id", "deck", ["source_id"], unique=False)
    op.create_index(
        "idx_16989_ix_deck_preconstructed_release",
        "deck",
        ["preconstructed_release"],
        unique=False,
    )
    op.create_index(
        "idx_16989_ix_deck_phoenixborn_id", "deck", ["phoenixborn_id"], unique=False
    )
    op.create_index("idx_16989_ix_deck_modified", "deck", ["modified"], unique=False)
    op.create_index(
        "idx_16989_ix_deck_is_snapshot", "deck", ["is_snapshot"], unique=False
    )
    op.create_index("idx_16989_ix_deck_is_public", "deck", ["is_public"], unique=False)
    op.create_index(
        "idx_16989_ix_deck_is_preconstructed",
        "deck",
        ["is_preconstructed"],
        unique=False,
    )
    op.create_index("idx_16989_ix_deck_entity_id", "deck", ["entity_id"], unique=True)
    op.create_index("idx_16989_ix_deck_created", "deck", ["created"], unique=False)
    op.create_index(
        "idx_16989_fk_ashes_500_revision_id",
        "deck",
        ["ashes_500_revision_id"],
        unique=False,
    )

    op.create_table(
        "deck_selected_card",
        sa.Column("deck_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("card_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("is_first_five", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column("is_paid_effect", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column(
            "tutor_card_id",
            sa.BIGINT(),
            server_default=sa.text("'0'::bigint"),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["card_id"],
            ["card.id"],
            name="deck_selected_card_ibfk_1",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["deck_id"],
            ["deck.id"],
            name="deck_selected_card_ibfk_2",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint(
            "deck_id", "card_id", "tutor_card_id", name="idx_17004_primary"
        ),
    )
    op.create_index(
        "idx_17004_deck_selected_card_ibfk_1",
        "deck_selected_card",
        ["card_id"],
        unique=False,
    )

    op.create_table(
        "deck_card",
        sa.Column("deck_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("card_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("count", sa.SMALLINT(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["card_id"],
            ["card.id"],
            name="deck_card_ibfk_1",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["deck_id"],
            ["deck.id"],
            name="deck_card_ibfk_2",
            onupdate="RESTRICT",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("deck_id", "card_id", name="idx_16998_primary"),
    )
    op.create_index("idx_16998_card_id", "deck_card", ["card_id"], unique=False)

    op.create_table(
        "invite",
        sa.Column("uuid", sa.VARCHAR(length=36), autoincrement=False, nullable=False),
        sa.Column("email", sa.VARCHAR(length=254), autoincrement=False, nullable=False),
        sa.Column("requests", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column(
            "requested",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("uuid", name="idx_17008_primary"),
    )
    op.create_index("idx_17008_ix_invite_email", "invite", ["email"], unique=True)

    op.create_table(
        "stream",
        sa.Column("id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.Column("entity_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column(
            "entity_type", sa.VARCHAR(length=16), autoincrement=False, nullable=True
        ),
        sa.Column("source_entity_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column(
            "posted",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="idx_17058_primary"),
    )
    op.create_index(
        "idx_17058_ix_stream_souce_entity_id",
        "stream",
        ["source_entity_id"],
        unique=False,
    )
    op.create_index("idx_17058_ix_stream_posted", "stream", ["posted"], unique=False)
    op.create_index(
        "idx_17058_ix_stream_entity_type", "stream", ["entity_type"], unique=False
    )
    op.create_index(
        "idx_17058_ix_stream_entity_id", "stream", ["entity_id"], unique=True
    )

    op.create_table(
        "user_release",
        sa.Column("user_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("release_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["release_id"],
            ["releases.id"],
            name="user_release_ibfk_1",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name="user_release_ibfk_2",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("user_id", "release_id", name="idx_17083_primary"),
    )
    op.create_index(
        "idx_17083_release_id", "user_release", ["release_id"], unique=False
    )
    op.create_index(
        "idx_17083_ix_user_release_user_id", "user_release", ["user_id"], unique=False
    )

    op.create_table(
        "subscription",
        sa.Column("user_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("source_entity_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column(
            "last_seen_entity_id", sa.BIGINT(), autoincrement=False, nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name="subscription_ibfk_1",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint(
            "user_id", "source_entity_id", name="idx_17068_primary"
        ),
    )
    op.create_index(
        "idx_17068_ix_subscription_last_seen_entity_id",
        "subscription",
        ["last_seen_entity_id"],
        unique=False,
    )

    op.create_table(
        "deck_die",
        sa.Column("deck_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("die_flag", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("count", sa.SMALLINT(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["deck_id"],
            ["deck.id"],
            name="deck_die_ibfk_1",
            onupdate="RESTRICT",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("deck_id", "die_flag", name="idx_17001_primary"),
    )

    op.create_table(
        "streamable",
        sa.Column("entity_id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("entity_id", name="idx_17064_primary"),
    )

    op.create_table(
        "ashes500_value",
        sa.Column("id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.Column("card_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("revision_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("combo_card_id", sa.BIGINT(), autoincrement=False, nullable=True),
        sa.Column("qty_1", sa.SMALLINT(), autoincrement=False, nullable=False),
        sa.Column("qty_2", sa.SMALLINT(), autoincrement=False, nullable=True),
        sa.Column("qty_3", sa.SMALLINT(), autoincrement=False, nullable=True),
        sa.Column(
            "combo_card_type", sa.VARCHAR(length=25), autoincrement=False, nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["card_id"],
            ["card.id"],
            name="ashes500_value_ibfk_1",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["combo_card_id"],
            ["card.id"],
            name="ashes500_value_ibfk_2",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["revision_id"],
            ["ashes500_revision.id"],
            name="ashes500_value_ibfk_3",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("id", name="idx_16955_primary"),
    )
    op.create_index(
        "idx_16955_ix_ashes500_value_revision_id",
        "ashes500_value",
        ["revision_id"],
        unique=False,
    )
    op.create_index(
        "idx_16955_ix_ashes500_value_card_id",
        "ashes500_value",
        ["card_id"],
        unique=False,
    )
    op.create_index(
        "idx_16955_combo_card_id", "ashes500_value", ["combo_card_id"], unique=False
    )

    op.create_table(
        "post",
        sa.Column("id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.Column("entity_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("user_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("section_id", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column("title", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column("text", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("pin_teaser", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "is_pinned",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "is_deleted",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "is_moderated",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "original_title", sa.VARCHAR(length=255), autoincrement=False, nullable=True
        ),
        sa.Column("original_text", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("moderation_notes", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "created",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "modified",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["section_id"],
            ["section.id"],
            name="post_ibfk_1",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name="post_ibfk_2",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("id", name="idx_17019_primary"),
    )
    op.create_index("idx_17019_user_id", "post", ["user_id"], unique=False)
    op.create_index(
        "idx_17019_ix_post_section_id", "post", ["section_id"], unique=False
    )
    op.create_index("idx_17019_ix_post_is_pinned", "post", ["is_pinned"], unique=False)
    op.create_index(
        "idx_17019_ix_post_is_deleted", "post", ["is_deleted"], unique=False
    )
    op.create_index("idx_17019_ix_post_entity_id", "post", ["entity_id"], unique=True)
    op.create_index("idx_17019_ix_post_created", "post", ["created"], unique=False)

    op.create_table(
        "phoenix_dice",
        sa.Column("id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.Column("email", sa.VARCHAR(length=254), autoincrement=False, nullable=False),
        sa.Column(
            "only_official_icons", sa.BOOLEAN(), autoincrement=False, nullable=False
        ),
        sa.Column("desired_sets", sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column(
            "created",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="idx_17013_primary"),
    )
    op.create_index(
        "idx_17013_ix_phoenix_dice_only_official_icons",
        "phoenix_dice",
        ["only_official_icons"],
        unique=False,
    )
    op.create_index(
        "idx_17013_ix_phoenix_dice_email", "phoenix_dice", ["email"], unique=True
    )

    op.create_table(
        "sessions",
        sa.Column("id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.Column(
            "session_id", sa.VARCHAR(length=255), autoincrement=False, nullable=True
        ),
        sa.Column("data", postgresql.BYTEA(), autoincrement=False, nullable=True),
        sa.Column(
            "expiry",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="idx_17049_primary"),
    )
    op.create_index("idx_17049_session_id", "sessions", ["session_id"], unique=True)


def downgrade():
    # Takes the database back to a completely empty state
    op.drop_index("idx_17049_session_id", table_name="sessions")
    op.drop_table("sessions")
    op.drop_index("idx_17013_ix_phoenix_dice_email", table_name="phoenix_dice")
    op.drop_index(
        "idx_17013_ix_phoenix_dice_only_official_icons", table_name="phoenix_dice"
    )
    op.drop_table("phoenix_dice")
    op.drop_index("idx_17019_ix_post_created", table_name="post")
    op.drop_index("idx_17019_ix_post_entity_id", table_name="post")
    op.drop_index("idx_17019_ix_post_is_deleted", table_name="post")
    op.drop_index("idx_17019_ix_post_is_pinned", table_name="post")
    op.drop_index("idx_17019_ix_post_section_id", table_name="post")
    op.drop_index("idx_17019_user_id", table_name="post")
    op.drop_table("post")
    op.drop_index("idx_16955_combo_card_id", table_name="ashes500_value")
    op.drop_index("idx_16955_ix_ashes500_value_card_id", table_name="ashes500_value")
    op.drop_index(
        "idx_16955_ix_ashes500_value_revision_id", table_name="ashes500_value"
    )
    op.drop_table("ashes500_value")
    op.drop_table("streamable")
    op.drop_index("idx_16989_fk_ashes_500_revision_id", table_name="deck")
    op.drop_index("idx_16989_ix_deck_created", table_name="deck")
    op.drop_index("idx_16989_ix_deck_entity_id", table_name="deck")
    op.drop_index("idx_16989_ix_deck_is_preconstructed", table_name="deck")
    op.drop_index("idx_16989_ix_deck_is_public", table_name="deck")
    op.drop_index("idx_16989_ix_deck_is_snapshot", table_name="deck")
    op.drop_index("idx_16989_ix_deck_modified", table_name="deck")
    op.drop_index("idx_16989_ix_deck_phoenixborn_id", table_name="deck")
    op.drop_index("idx_16989_ix_deck_preconstructed_release", table_name="deck")
    op.drop_index("idx_16989_ix_deck_source_id", table_name="deck")
    op.drop_index("idx_16989_ix_deck_title", table_name="deck")
    op.drop_index("idx_16989_ix_deck_user_id", table_name="deck")
    op.drop_table("deck")
    op.drop_index(
        "idx_16946_ix_ashes500_revision_created", table_name="ashes500_revision"
    )
    op.drop_index(
        "idx_16946_ix_ashes500_revision_entity_id", table_name="ashes500_revision"
    )
    op.drop_table("ashes500_revision")
    op.drop_index("idx_17031_name", table_name="releases")
    op.drop_table("releases")
    op.drop_index("idx_17073_ix_user_badge", table_name="user")
    op.drop_index("idx_17073_ix_user_email", table_name="user")
    op.drop_index("idx_17073_ix_user_email_subscriptions", table_name="user")
    op.drop_index("idx_17073_ix_user_reset_uuid", table_name="user")
    op.drop_table("user")
    op.drop_table("deck_die")
    op.drop_index(
        "idx_17068_ix_subscription_last_seen_entity_id", table_name="subscription"
    )
    op.drop_table("subscription")
    op.drop_index("idx_17083_ix_user_release_user_id", table_name="user_release")
    op.drop_index("idx_17083_release_id", table_name="user_release")
    op.drop_table("user_release")
    op.drop_index("idx_17058_ix_stream_entity_id", table_name="stream")
    op.drop_index("idx_17058_ix_stream_entity_type", table_name="stream")
    op.drop_index("idx_17058_ix_stream_posted", table_name="stream")
    op.drop_index("idx_17058_ix_stream_souce_entity_id", table_name="stream")
    op.drop_table("stream")
    op.drop_index("idx_16961_ix_card_alt_dice_flags", table_name="card")
    op.drop_index("idx_16961_ix_card_card_type", table_name="card")
    op.drop_index("idx_16961_ix_card_cost_weight", table_name="card")
    op.drop_index("idx_16961_ix_card_dice_flags", table_name="card")
    op.drop_index("idx_16961_ix_card_entity_id", table_name="card")
    op.drop_index("idx_16961_ix_card_name", table_name="card")
    op.drop_index("idx_16961_ix_card_phoenixborn", table_name="card")
    op.drop_index("idx_16961_ix_card_release_id", table_name="card")
    op.drop_index("idx_16961_ix_card_stub", table_name="card")
    op.drop_index("idx_16961_ix_card_text", table_name="card")
    op.drop_table("card")
    op.drop_index("idx_17008_ix_invite_email", table_name="invite")
    op.drop_table("invite")
    op.drop_index("idx_16998_card_id", table_name="deck_card")
    op.drop_table("deck_card")
    op.drop_index("idx_16973_conjuration_id", table_name="card_conjuration")
    op.drop_table("card_conjuration")
    op.drop_index(
        "idx_17004_deck_selected_card_ibfk_1", table_name="deck_selected_card"
    )
    op.drop_table("deck_selected_card")
    op.drop_index("idx_17039_ix_section_entity_id", table_name="section")
    op.drop_index("idx_17039_ix_section_is_restricted", table_name="section")
    op.drop_index("idx_17039_ix_section_stub", table_name="section")
    op.drop_table("section")
    op.drop_index("idx_16978_ix_comment_created", table_name="comment")
    op.drop_index("idx_16978_ix_comment_entity_id", table_name="comment")
    op.drop_index("idx_16978_ix_comment_is_deleted", table_name="comment")
    op.drop_index("idx_16978_ix_comment_order", table_name="comment")
    op.drop_index("idx_16978_ix_comment_source_entity_id", table_name="comment")
    op.drop_index("idx_16978_user_id", table_name="comment")
    op.drop_table("comment")

"""postgres_indexes

Revision ID: de48fc5206e4
Revises: c58a815a71a0
Create Date: 2020-08-30 17:13:43.204983+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "de48fc5206e4"
down_revision = "c58a815a71a0"
branch_labels = None
depends_on = None


def upgrade():
    # We will no longer be using the session table (Flask-login specific)
    op.drop_table("sessions")
    # We need to recreate a bunch of indexes to ensure automigrations work going forward
    #  (old ones were ported from MySQL, so they have some funky names)
    op.create_index(
        op.f("ix_ashes500_revision_created"),
        "ashes500_revision",
        ["created"],
        unique=False,
    )
    op.create_index(
        op.f("ix_ashes500_revision_entity_id"),
        "ashes500_revision",
        ["entity_id"],
        unique=False,
    )
    op.drop_index(
        "idx_16946_ix_ashes500_revision_created", table_name="ashes500_revision"
    )
    op.drop_index(
        "idx_16946_ix_ashes500_revision_entity_id", table_name="ashes500_revision"
    )
    op.create_index(
        op.f("ix_ashes500_value_card_id"), "ashes500_value", ["card_id"], unique=False
    )
    op.create_index(
        op.f("ix_ashes500_value_revision_id"),
        "ashes500_value",
        ["revision_id"],
        unique=False,
    )
    op.drop_index("idx_16955_combo_card_id", table_name="ashes500_value")
    op.drop_index("idx_16955_ix_ashes500_value_card_id", table_name="ashes500_value")
    op.drop_index(
        "idx_16955_ix_ashes500_value_revision_id", table_name="ashes500_value"
    )
    op.drop_constraint("ashes500_value_ibfk_3", "ashes500_value", type_="foreignkey")
    op.drop_constraint("ashes500_value_ibfk_1", "ashes500_value", type_="foreignkey")
    op.drop_constraint("ashes500_value_ibfk_2", "ashes500_value", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_ashes500_value_revision_id_ashes500_revision"),
        "ashes500_value",
        "ashes500_revision",
        ["revision_id"],
        ["id"],
    )
    op.create_foreign_key(
        op.f("fk_ashes500_value_card_id_card"),
        "ashes500_value",
        "card",
        ["card_id"],
        ["id"],
    )
    op.create_foreign_key(
        op.f("fk_ashes500_value_combo_card_id_card"),
        "ashes500_value",
        "card",
        ["combo_card_id"],
        ["id"],
    )
    op.create_index(
        op.f("ix_card_alt_dice_flags"), "card", ["alt_dice_flags"], unique=False
    )
    op.create_index(op.f("ix_card_card_type"), "card", ["card_type"], unique=False)
    op.create_index(op.f("ix_card_cost_weight"), "card", ["cost_weight"], unique=False)
    op.create_index(op.f("ix_card_dice_flags"), "card", ["dice_flags"], unique=False)
    op.create_index(op.f("ix_card_entity_id"), "card", ["entity_id"], unique=True)
    op.create_index(op.f("ix_card_name"), "card", ["name"], unique=True)
    op.create_index(op.f("ix_card_phoenixborn"), "card", ["phoenixborn"], unique=False)
    op.create_index(op.f("ix_card_release_id"), "card", ["release_id"], unique=False)
    op.create_index(op.f("ix_card_stub"), "card", ["stub"], unique=True)
    op.create_index("ix_card_text", "card", ["name", "text"], unique=False)
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
    op.drop_constraint("card_release_ibfk_1", "card", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_card_release_id_releases"), "card", "releases", ["release_id"], ["id"]
    )
    op.drop_index("idx_16973_conjuration_id", table_name="card_conjuration")
    op.drop_constraint(
        "card_conjuration_ibfk_2", "card_conjuration", type_="foreignkey"
    )
    op.drop_constraint(
        "card_conjuration_ibfk_1", "card_conjuration", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_card_conjuration_conjuration_id_card"),
        "card_conjuration",
        "card",
        ["conjuration_id"],
        ["id"],
    )
    op.create_foreign_key(
        op.f("fk_card_conjuration_card_id_card"),
        "card_conjuration",
        "card",
        ["card_id"],
        ["id"],
    )
    op.create_index(op.f("ix_comment_created"), "comment", ["created"], unique=False)
    op.create_index(op.f("ix_comment_entity_id"), "comment", ["entity_id"], unique=True)
    op.create_index(
        op.f("ix_comment_is_deleted"), "comment", ["is_deleted"], unique=False
    )
    op.create_index(op.f("ix_comment_order"), "comment", ["order"], unique=False)
    op.create_index(
        op.f("ix_comment_source_entity_id"),
        "comment",
        ["source_entity_id"],
        unique=False,
    )
    op.drop_index("idx_16978_ix_comment_created", table_name="comment")
    op.drop_index("idx_16978_ix_comment_entity_id", table_name="comment")
    op.drop_index("idx_16978_ix_comment_is_deleted", table_name="comment")
    op.drop_index("idx_16978_ix_comment_order", table_name="comment")
    op.drop_index("idx_16978_ix_comment_source_entity_id", table_name="comment")
    op.drop_index("idx_16978_user_id", table_name="comment")
    op.drop_constraint("comment_ibfk_1", "comment", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_comment_user_id_user"), "comment", "user", ["user_id"], ["id"]
    )
    op.create_index(op.f("ix_deck_created"), "deck", ["created"], unique=False)
    op.create_index(op.f("ix_deck_entity_id"), "deck", ["entity_id"], unique=True)
    op.create_index(
        op.f("ix_deck_is_preconstructed"), "deck", ["is_preconstructed"], unique=False
    )
    op.create_index(op.f("ix_deck_is_public"), "deck", ["is_public"], unique=False)
    op.create_index(op.f("ix_deck_is_snapshot"), "deck", ["is_snapshot"], unique=False)
    op.create_index(op.f("ix_deck_modified"), "deck", ["modified"], unique=False)
    op.create_index(
        op.f("ix_deck_phoenixborn_id"), "deck", ["phoenixborn_id"], unique=False
    )
    op.create_index(
        op.f("ix_deck_preconstructed_release"),
        "deck",
        ["preconstructed_release"],
        unique=False,
    )
    op.create_index(op.f("ix_deck_source_id"), "deck", ["source_id"], unique=False)
    op.create_index(op.f("ix_deck_title"), "deck", ["title"], unique=False)
    op.create_index(op.f("ix_deck_user_id"), "deck", ["user_id"], unique=False)
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
    op.drop_constraint("fk_ashes_500_revision_id", "deck", type_="foreignkey")
    op.drop_constraint("deck_ibfk_3", "deck", type_="foreignkey")
    op.drop_constraint("deck_ibfk_2", "deck", type_="foreignkey")
    op.drop_constraint("deck_ibfk_1", "deck", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_deck_phoenixborn_id_card"), "deck", "card", ["phoenixborn_id"], ["id"]
    )
    op.create_foreign_key(
        op.f("fk_deck_ashes_500_revision_id_ashes500_revision"),
        "deck",
        "ashes500_revision",
        ["ashes_500_revision_id"],
        ["id"],
    )
    op.create_foreign_key(
        op.f("fk_deck_user_id_user"), "deck", "user", ["user_id"], ["id"]
    )
    op.create_foreign_key(
        op.f("fk_deck_source_id_deck"), "deck", "deck", ["source_id"], ["id"]
    )
    op.drop_index("idx_16998_card_id", table_name="deck_card")
    op.drop_constraint("deck_card_ibfk_1", "deck_card", type_="foreignkey")
    op.drop_constraint("deck_card_ibfk_2", "deck_card", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_deck_card_card_id_card"), "deck_card", "card", ["card_id"], ["id"]
    )
    op.create_foreign_key(
        op.f("fk_deck_card_deck_id_deck"), "deck_card", "deck", ["deck_id"], ["id"]
    )
    op.drop_constraint("deck_die_ibfk_1", "deck_die", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_deck_die_deck_id_deck"), "deck_die", "deck", ["deck_id"], ["id"]
    )
    op.drop_index(
        "idx_17004_deck_selected_card_ibfk_1", table_name="deck_selected_card"
    )
    op.drop_constraint(
        "deck_selected_card_ibfk_1", "deck_selected_card", type_="foreignkey"
    )
    op.drop_constraint(
        "deck_selected_card_ibfk_2", "deck_selected_card", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_deck_selected_card_card_id_card"),
        "deck_selected_card",
        "card",
        ["card_id"],
        ["id"],
    )
    op.create_foreign_key(
        op.f("fk_deck_selected_card_deck_id_deck"),
        "deck_selected_card",
        "deck",
        ["deck_id"],
        ["id"],
    )
    op.create_index(op.f("ix_invite_email"), "invite", ["email"], unique=True)
    op.drop_index("idx_17008_ix_invite_email", table_name="invite")
    op.create_index(
        op.f("ix_phoenix_dice_email"), "phoenix_dice", ["email"], unique=True
    )
    op.create_index(
        op.f("ix_phoenix_dice_only_official_icons"),
        "phoenix_dice",
        ["only_official_icons"],
        unique=False,
    )
    op.drop_index("idx_17013_ix_phoenix_dice_email", table_name="phoenix_dice")
    op.drop_index(
        "idx_17013_ix_phoenix_dice_only_official_icons", table_name="phoenix_dice"
    )
    op.create_index(op.f("ix_post_created"), "post", ["created"], unique=False)
    op.create_index(op.f("ix_post_entity_id"), "post", ["entity_id"], unique=True)
    op.create_index(op.f("ix_post_is_deleted"), "post", ["is_deleted"], unique=False)
    op.create_index(op.f("ix_post_is_pinned"), "post", ["is_pinned"], unique=False)
    op.create_index(op.f("ix_post_section_id"), "post", ["section_id"], unique=False)
    op.drop_index("idx_17019_ix_post_created", table_name="post")
    op.drop_index("idx_17019_ix_post_entity_id", table_name="post")
    op.drop_index("idx_17019_ix_post_is_deleted", table_name="post")
    op.drop_index("idx_17019_ix_post_is_pinned", table_name="post")
    op.drop_index("idx_17019_ix_post_section_id", table_name="post")
    op.drop_index("idx_17019_user_id", table_name="post")
    op.drop_constraint("post_ibfk_2", "post", type_="foreignkey")
    op.drop_constraint("post_ibfk_1", "post", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_post_user_id_user"), "post", "user", ["user_id"], ["id"]
    )
    op.create_foreign_key(
        op.f("fk_post_section_id_section"), "post", "section", ["section_id"], ["id"]
    )
    op.create_unique_constraint(op.f("uq_releases_name"), "releases", ["name"])
    op.drop_index("idx_17031_name", table_name="releases")
    op.create_index(op.f("ix_section_entity_id"), "section", ["entity_id"], unique=True)
    op.create_index(
        op.f("ix_section_is_restricted"), "section", ["is_restricted"], unique=False
    )
    op.create_index(op.f("ix_section_stub"), "section", ["stub"], unique=True)
    op.drop_index("idx_17039_ix_section_entity_id", table_name="section")
    op.drop_index("idx_17039_ix_section_is_restricted", table_name="section")
    op.drop_index("idx_17039_ix_section_stub", table_name="section")
    op.create_index(op.f("ix_stream_entity_id"), "stream", ["entity_id"], unique=True)
    op.create_index(
        op.f("ix_stream_entity_type"), "stream", ["entity_type"], unique=False
    )
    op.create_index(op.f("ix_stream_posted"), "stream", ["posted"], unique=False)
    op.create_index(
        op.f("ix_stream_source_entity_id"), "stream", ["source_entity_id"], unique=False
    )
    op.drop_index("idx_17058_ix_stream_entity_id", table_name="stream")
    op.drop_index("idx_17058_ix_stream_entity_type", table_name="stream")
    op.drop_index("idx_17058_ix_stream_posted", table_name="stream")
    op.drop_index("idx_17058_ix_stream_souce_entity_id", table_name="stream")
    op.create_index(
        op.f("ix_subscription_last_seen_entity_id"),
        "subscription",
        ["last_seen_entity_id"],
        unique=False,
    )
    op.drop_index(
        "idx_17068_ix_subscription_last_seen_entity_id", table_name="subscription"
    )
    op.drop_constraint("subscription_ibfk_1", "subscription", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_subscription_user_id_user"),
        "subscription",
        "user",
        ["user_id"],
        ["id"],
    )
    op.create_index(op.f("ix_user_badge"), "user", ["badge"], unique=True)
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_index(
        op.f("ix_user_email_subscriptions"),
        "user",
        ["email_subscriptions"],
        unique=False,
    )
    op.create_index(op.f("ix_user_reset_uuid"), "user", ["reset_uuid"], unique=True)
    op.drop_index("idx_17073_ix_user_badge", table_name="user")
    op.drop_index("idx_17073_ix_user_email", table_name="user")
    op.drop_index("idx_17073_ix_user_email_subscriptions", table_name="user")
    op.drop_index("idx_17073_ix_user_reset_uuid", table_name="user")
    op.create_index(
        op.f("ix_user_release_user_id"), "user_release", ["user_id"], unique=False
    )
    op.drop_index("idx_17083_ix_user_release_user_id", table_name="user_release")
    op.drop_index("idx_17083_release_id", table_name="user_release")
    op.drop_constraint("user_release_ibfk_1", "user_release", type_="foreignkey")
    op.drop_constraint("user_release_ibfk_2", "user_release", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_user_release_release_id_releases"),
        "user_release",
        "releases",
        ["release_id"],
        ["id"],
    )
    op.create_foreign_key(
        op.f("fk_user_release_user_id_user"),
        "user_release",
        "user",
        ["user_id"],
        ["id"],
    )


def downgrade():
    op.drop_constraint(
        op.f("fk_user_release_user_id_user"), "user_release", type_="foreignkey"
    )
    op.drop_constraint(
        op.f("fk_user_release_release_id_releases"), "user_release", type_="foreignkey"
    )
    op.create_foreign_key(
        "user_release_ibfk_2",
        "user_release",
        "user",
        ["user_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        "user_release_ibfk_1",
        "user_release",
        "releases",
        ["release_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_index(
        "idx_17083_release_id", "user_release", ["release_id"], unique=False
    )
    op.create_index(
        "idx_17083_ix_user_release_user_id", "user_release", ["user_id"], unique=False
    )
    op.drop_index(op.f("ix_user_release_user_id"), table_name="user_release")
    op.create_index("idx_17073_ix_user_reset_uuid", "user", ["reset_uuid"], unique=True)
    op.create_index(
        "idx_17073_ix_user_email_subscriptions",
        "user",
        ["email_subscriptions"],
        unique=False,
    )
    op.create_index("idx_17073_ix_user_email", "user", ["email"], unique=True)
    op.create_index("idx_17073_ix_user_badge", "user", ["badge"], unique=True)
    op.drop_index(op.f("ix_user_reset_uuid"), table_name="user")
    op.drop_index(op.f("ix_user_email_subscriptions"), table_name="user")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_index(op.f("ix_user_badge"), table_name="user")
    op.drop_constraint(
        op.f("fk_subscription_user_id_user"), "subscription", type_="foreignkey"
    )
    op.create_foreign_key(
        "subscription_ibfk_1",
        "subscription",
        "user",
        ["user_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_index(
        "idx_17068_ix_subscription_last_seen_entity_id",
        "subscription",
        ["last_seen_entity_id"],
        unique=False,
    )
    op.drop_index(
        op.f("ix_subscription_last_seen_entity_id"), table_name="subscription"
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
    op.drop_index(op.f("ix_stream_source_entity_id"), table_name="stream")
    op.drop_index(op.f("ix_stream_posted"), table_name="stream")
    op.drop_index(op.f("ix_stream_entity_type"), table_name="stream")
    op.drop_index(op.f("ix_stream_entity_id"), table_name="stream")
    op.create_index("idx_17039_ix_section_stub", "section", ["stub"], unique=True)
    op.create_index(
        "idx_17039_ix_section_is_restricted", "section", ["is_restricted"], unique=False
    )
    op.create_index(
        "idx_17039_ix_section_entity_id", "section", ["entity_id"], unique=True
    )
    op.drop_index(op.f("ix_section_stub"), table_name="section")
    op.drop_index(op.f("ix_section_is_restricted"), table_name="section")
    op.drop_index(op.f("ix_section_entity_id"), table_name="section")
    op.create_index("idx_17031_name", "releases", ["name"], unique=True)
    op.drop_constraint(op.f("uq_releases_name"), "releases", type_="unique")
    op.drop_constraint(op.f("fk_post_section_id_section"), "post", type_="foreignkey")
    op.drop_constraint(op.f("fk_post_user_id_user"), "post", type_="foreignkey")
    op.create_foreign_key(
        "post_ibfk_1",
        "post",
        "section",
        ["section_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        "post_ibfk_2",
        "post",
        "user",
        ["user_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
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
    op.drop_index(op.f("ix_post_section_id"), table_name="post")
    op.drop_index(op.f("ix_post_is_pinned"), table_name="post")
    op.drop_index(op.f("ix_post_is_deleted"), table_name="post")
    op.drop_index(op.f("ix_post_entity_id"), table_name="post")
    op.drop_index(op.f("ix_post_created"), table_name="post")
    op.create_index(
        "idx_17013_ix_phoenix_dice_only_official_icons",
        "phoenix_dice",
        ["only_official_icons"],
        unique=False,
    )
    op.create_index(
        "idx_17013_ix_phoenix_dice_email", "phoenix_dice", ["email"], unique=True
    )
    op.drop_index(
        op.f("ix_phoenix_dice_only_official_icons"), table_name="phoenix_dice"
    )
    op.drop_index(op.f("ix_phoenix_dice_email"), table_name="phoenix_dice")
    op.create_index("idx_17008_ix_invite_email", "invite", ["email"], unique=True)
    op.drop_index(op.f("ix_invite_email"), table_name="invite")
    op.drop_constraint(
        op.f("fk_deck_selected_card_deck_id_deck"),
        "deck_selected_card",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("fk_deck_selected_card_card_id_card"),
        "deck_selected_card",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "deck_selected_card_ibfk_2",
        "deck_selected_card",
        "deck",
        ["deck_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        "deck_selected_card_ibfk_1",
        "deck_selected_card",
        "card",
        ["card_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_index(
        "idx_17004_deck_selected_card_ibfk_1",
        "deck_selected_card",
        ["card_id"],
        unique=False,
    )
    op.drop_constraint(op.f("fk_deck_die_deck_id_deck"), "deck_die", type_="foreignkey")
    op.create_foreign_key(
        "deck_die_ibfk_1",
        "deck_die",
        "deck",
        ["deck_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="CASCADE",
    )
    op.drop_constraint(
        op.f("fk_deck_card_deck_id_deck"), "deck_card", type_="foreignkey"
    )
    op.drop_constraint(
        op.f("fk_deck_card_card_id_card"), "deck_card", type_="foreignkey"
    )
    op.create_foreign_key(
        "deck_card_ibfk_2",
        "deck_card",
        "deck",
        ["deck_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "deck_card_ibfk_1",
        "deck_card",
        "card",
        ["card_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_index("idx_16998_card_id", "deck_card", ["card_id"], unique=False)
    op.drop_constraint(op.f("fk_deck_source_id_deck"), "deck", type_="foreignkey")
    op.drop_constraint(op.f("fk_deck_user_id_user"), "deck", type_="foreignkey")
    op.drop_constraint(
        op.f("fk_deck_ashes_500_revision_id_ashes500_revision"),
        "deck",
        type_="foreignkey",
    )
    op.drop_constraint(op.f("fk_deck_phoenixborn_id_card"), "deck", type_="foreignkey")
    op.create_foreign_key(
        "deck_ibfk_1",
        "deck",
        "card",
        ["phoenixborn_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        "deck_ibfk_2",
        "deck",
        "user",
        ["user_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        "deck_ibfk_3",
        "deck",
        "deck",
        ["source_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        "fk_ashes_500_revision_id",
        "deck",
        "ashes500_revision",
        ["ashes_500_revision_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
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
    op.drop_index(op.f("ix_deck_user_id"), table_name="deck")
    op.drop_index(op.f("ix_deck_title"), table_name="deck")
    op.drop_index(op.f("ix_deck_source_id"), table_name="deck")
    op.drop_index(op.f("ix_deck_preconstructed_release"), table_name="deck")
    op.drop_index(op.f("ix_deck_phoenixborn_id"), table_name="deck")
    op.drop_index(op.f("ix_deck_modified"), table_name="deck")
    op.drop_index(op.f("ix_deck_is_snapshot"), table_name="deck")
    op.drop_index(op.f("ix_deck_is_public"), table_name="deck")
    op.drop_index(op.f("ix_deck_is_preconstructed"), table_name="deck")
    op.drop_index(op.f("ix_deck_entity_id"), table_name="deck")
    op.drop_index(op.f("ix_deck_created"), table_name="deck")
    op.drop_constraint(op.f("fk_comment_user_id_user"), "comment", type_="foreignkey")
    op.create_foreign_key(
        "comment_ibfk_1",
        "comment",
        "user",
        ["user_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
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
    op.drop_index(op.f("ix_comment_source_entity_id"), table_name="comment")
    op.drop_index(op.f("ix_comment_order"), table_name="comment")
    op.drop_index(op.f("ix_comment_is_deleted"), table_name="comment")
    op.drop_index(op.f("ix_comment_entity_id"), table_name="comment")
    op.drop_index(op.f("ix_comment_created"), table_name="comment")
    op.drop_constraint(
        op.f("fk_card_conjuration_card_id_card"), "card_conjuration", type_="foreignkey"
    )
    op.drop_constraint(
        op.f("fk_card_conjuration_conjuration_id_card"),
        "card_conjuration",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "card_conjuration_ibfk_1",
        "card_conjuration",
        "card",
        ["card_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        "card_conjuration_ibfk_2",
        "card_conjuration",
        "card",
        ["conjuration_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_index(
        "idx_16973_conjuration_id", "card_conjuration", ["conjuration_id"], unique=False
    )
    op.drop_constraint(op.f("fk_card_release_id_releases"), "card", type_="foreignkey")
    op.create_foreign_key(
        "card_release_ibfk_1",
        "card",
        "releases",
        ["release_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
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
    op.drop_index("ix_card_text", table_name="card")
    op.drop_index(op.f("ix_card_stub"), table_name="card")
    op.drop_index(op.f("ix_card_release_id"), table_name="card")
    op.drop_index(op.f("ix_card_phoenixborn"), table_name="card")
    op.drop_index(op.f("ix_card_name"), table_name="card")
    op.drop_index(op.f("ix_card_entity_id"), table_name="card")
    op.drop_index(op.f("ix_card_dice_flags"), table_name="card")
    op.drop_index(op.f("ix_card_cost_weight"), table_name="card")
    op.drop_index(op.f("ix_card_card_type"), table_name="card")
    op.drop_index(op.f("ix_card_alt_dice_flags"), table_name="card")
    op.drop_constraint(
        op.f("fk_ashes500_value_combo_card_id_card"),
        "ashes500_value",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("fk_ashes500_value_card_id_card"), "ashes500_value", type_="foreignkey"
    )
    op.drop_constraint(
        op.f("fk_ashes500_value_revision_id_ashes500_revision"),
        "ashes500_value",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "ashes500_value_ibfk_2",
        "ashes500_value",
        "card",
        ["combo_card_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        "ashes500_value_ibfk_1",
        "ashes500_value",
        "card",
        ["card_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        "ashes500_value_ibfk_3",
        "ashes500_value",
        "ashes500_revision",
        ["revision_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
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
    op.drop_index(op.f("ix_ashes500_value_revision_id"), table_name="ashes500_value")
    op.drop_index(op.f("ix_ashes500_value_card_id"), table_name="ashes500_value")
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
    op.drop_index(
        op.f("ix_ashes500_revision_entity_id"), table_name="ashes500_revision"
    )
    op.drop_index(op.f("ix_ashes500_revision_created"), table_name="ashes500_revision")
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

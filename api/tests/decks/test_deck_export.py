"""Tests for deck export functionality

These tests cover the export endpoints that allow one Ashes.live instance
to serve deck data to another instance for migration purposes.
"""

import uuid
from datetime import timedelta

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.services.deck import create_or_update_deck, create_snapshot_for_deck
from api.tests import utils
from api.utils.dates import pydantic_style_datetime_str, utcnow

from .deck_utils import create_deck_for_user, get_phoenixborn_cards_dice

# Shared fixtures


@pytest.fixture(scope="module", autouse=True)
def export_user(decks_session):
    """User with export token for export tests"""
    user, _ = utils.create_user_token(decks_session)
    user.deck_export_uuid = uuid.uuid4()
    decks_session.commit()
    return user


@pytest.fixture(scope="module", autouse=True)
def export_deck1(decks_session, export_user):
    """First deck for export user"""
    return create_deck_for_user(decks_session, export_user, release_stub="master-set")


@pytest.fixture(scope="module", autouse=True)
def export_deck2(decks_session, export_user):
    """Second deck for export user"""
    return create_deck_for_user(decks_session, export_user, release_stub="expansion")


@pytest.fixture(scope="module", autouse=True)
def export_deck3(decks_session, export_user):
    """Third deck for export user (marked as exported)"""
    deck = create_deck_for_user(decks_session, export_user, release_stub="expansion")
    deck.is_exported = True
    decks_session.commit()
    return deck


# Basic Export Functionality Tests


def test_export_decks_requires_valid_token(
    client: TestClient, session: db.Session, monkeypatch
):
    """Test that export endpoint requires a valid export token"""
    # Enable exports for this test
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Test with invalid UUID
    invalid_token = uuid.uuid4()
    response = client.get(f"/v2/decks/export/{invalid_token}")

    data = response.json()
    assert response.status_code == status.HTTP_404_NOT_FOUND, data
    assert "No user matching export token" in data["detail"]


def test_export_decks_fails_when_exports_disabled(
    client: TestClient, session: db.Session, export_user, monkeypatch
):
    """Test that export endpoint fails when ALLOW_EXPORTS=false"""
    # Ensure exports are disabled
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": False})

    response = client.get(f"/v2/decks/export/{export_user.deck_export_uuid}")

    data = response.json()
    assert response.status_code == status.HTTP_400_BAD_REQUEST, data
    assert "not allowed" in data["detail"]


def test_export_decks_returns_paginated_results(
    client: TestClient,
    session: db.Session,
    export_user,
    export_deck1,
    export_deck2,
    monkeypatch,
):
    """Test that export endpoint returns paginated deck results"""
    # Enable exports and set small page size for testing
    utils.monkeypatch_settings(
        monkeypatch, {"allow_exports": True, "exports_per_request": 1}
    )

    response = client.get(f"/v2/decks/export/{export_user.deck_export_uuid}")

    data = response.json()
    assert response.status_code == status.HTTP_200_OK, data
    assert "decks" in data
    assert "total" in data
    assert "next_page_from_date" in data
    assert len(data["decks"]) == 1  # Page size limit
    assert data["total"] == 2  # Two unexported decks available
    assert data["next_page_from_date"] is not None  # Has next page


def test_export_decks_filters_by_export_status(
    client: TestClient,
    session: db.Session,
    export_user,
    export_deck1,
    export_deck3,
    monkeypatch,
):
    """Test that export endpoint only returns decks with is_exported=false"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    response = client.get(f"/v2/decks/export/{export_user.deck_export_uuid}")

    data = response.json()
    assert response.status_code == status.HTTP_200_OK, data
    # Should only return unexported decks (export_deck1 and export_deck2, not export_deck3)
    assert data["total"] == 2  # Two unexported decks
    # Compare by created dates since export data uses created as unique identifier
    exported_deck_created_dates = {deck["created"] for deck in data["decks"]}
    assert export_deck1.created.isoformat() in exported_deck_created_dates
    assert (
        export_deck3.created.isoformat() not in exported_deck_created_dates
    )  # Exported deck excluded


def test_export_decks_filters_by_from_date(
    client: TestClient,
    session: db.Session,
    export_user,
    export_deck1,
    export_deck2,
    monkeypatch,
):
    """Test that export endpoint filters decks by from_date parameter"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Set deck1 to older date and deck2 to newer date
    old_date = utcnow() - timedelta(days=2)
    new_date = utcnow() - timedelta(hours=1)
    export_deck1.created = old_date
    export_deck2.created = new_date
    session.commit()

    # Filter by date between old and new decks
    filter_date = utcnow() - timedelta(days=1)
    response = client.get(
        f"/v2/decks/export/{export_user.deck_export_uuid}?from_date={pydantic_style_datetime_str(filter_date)}"
    )

    data = response.json()
    assert response.status_code == status.HTTP_200_OK, data
    assert data["total"] == 1  # Only newer deck
    assert len(data["decks"]) == 1
    assert data["decks"][0]["created"] == pydantic_style_datetime_str(new_date)


def test_export_decks_single_deck_by_share_uuid(
    client: TestClient,
    session: db.Session,
    export_user,
    export_deck1,
    export_deck2,
    monkeypatch,
):
    """Test that export endpoint can export a single deck by share UUID"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Export only deck1 by its share UUID
    response = client.get(
        f"/v2/decks/export/{export_user.deck_export_uuid}?deck_share_uuid={export_deck1.direct_share_uuid}"
    )

    data = response.json()
    assert response.status_code == status.HTTP_200_OK, data
    assert data["total"] == 1  # Only the specified deck
    assert len(data["decks"]) == 1
    assert data["decks"][0]["created"] == pydantic_style_datetime_str(
        export_deck1.created
    )


def test_export_decks_includes_snapshots_for_single_deck(
    client: TestClient, session: db.Session, export_user, monkeypatch
):
    """Test that single deck export includes all associated snapshots"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Create a deck with snapshots
    source_deck = create_deck_for_user(session, export_user, release_stub="master-set")
    snapshot1 = create_snapshot_for_deck(
        session, export_user, source_deck, title="Test Snapshot 1", is_public=True
    )
    snapshot2 = create_snapshot_for_deck(
        session, export_user, source_deck, title="Test Snapshot 2", is_public=False
    )

    # Export by source deck's share UUID should include all snapshots
    response = client.get(
        f"/v2/decks/export/{export_user.deck_export_uuid}?deck_share_uuid={source_deck.direct_share_uuid}"
    )

    data = response.json()
    assert response.status_code == status.HTTP_200_OK, data
    assert data["total"] == 3  # Source deck + 2 snapshots
    assert len(data["decks"]) == 3

    # Verify all decks are included
    exported_created_dates = {deck["created"] for deck in data["decks"]}
    assert pydantic_style_datetime_str(source_deck.created) in exported_created_dates
    assert pydantic_style_datetime_str(snapshot1.created) in exported_created_dates
    assert pydantic_style_datetime_str(snapshot2.created) in exported_created_dates


def test_export_decks_excludes_deleted_legacy_decks(
    client: TestClient, session: db.Session, export_user, monkeypatch
):
    """Test that export endpoint excludes deleted and legacy decks"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Create normal deck
    normal_deck = create_deck_for_user(session, export_user, release_stub="master-set")

    # Create deleted deck
    deleted_deck = create_deck_for_user(session, export_user, release_stub="expansion")
    deleted_deck.is_deleted = True

    # Create legacy deck
    legacy_deck = create_deck_for_user(session, export_user, release_stub="expansion")
    legacy_deck.is_legacy = True

    session.commit()

    response = client.get(f"/v2/decks/export/{export_user.deck_export_uuid}")

    data = response.json()
    assert response.status_code == status.HTTP_200_OK, data
    # Should only include normal deck (plus existing export_deck1 and export_deck2 from fixtures)
    # But since we're in a fresh function scope, only the normal_deck should appear
    exported_created_dates = {deck["created"] for deck in data["decks"]}
    assert pydantic_style_datetime_str(normal_deck.created) in exported_created_dates
    assert (
        pydantic_style_datetime_str(deleted_deck.created) not in exported_created_dates
    )
    assert (
        pydantic_style_datetime_str(legacy_deck.created) not in exported_created_dates
    )


def test_export_decks_includes_selected_cards_data(
    client: TestClient, session: db.Session, export_user, monkeypatch
):
    """Test that export includes first_five, effect_costs, and tutor_map data"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Create a deck with selected cards data
    phoenixborn, card_dicts, dice_dicts = get_phoenixborn_cards_dice(
        session, "master-set"
    )

    # Extract some card stubs for selected cards
    first_card_stub = card_dicts[0]["stub"]
    second_card_stub = card_dicts[1]["stub"]
    third_card_stub = card_dicts[2]["stub"]

    deck = create_or_update_deck(
        session,
        export_user,
        phoenixborn=phoenixborn,
        title="Deck with Selected Cards",
        cards=card_dicts,
        dice=dice_dicts,
        first_five=[first_card_stub, second_card_stub],
        effect_costs=[second_card_stub, third_card_stub],
        tutor_map={first_card_stub: second_card_stub},
    )

    response = client.get(f"/v2/decks/export/{export_user.deck_export_uuid}")

    data = response.json()
    assert response.status_code == status.HTTP_200_OK, data

    # Find our deck in the results
    target_deck = None
    for exported_deck in data["decks"]:
        if exported_deck["created"] == pydantic_style_datetime_str(deck.created):
            target_deck = exported_deck
            break

    assert target_deck is not None, "Created deck not found in export"
    assert "first_five" in target_deck
    assert "effect_costs" in target_deck
    assert "tutor_map" in target_deck
    assert first_card_stub in target_deck["first_five"]
    assert second_card_stub in target_deck["first_five"]
    assert second_card_stub in target_deck["effect_costs"]
    assert third_card_stub in target_deck["effect_costs"]
    assert target_deck["tutor_map"][first_card_stub] == second_card_stub


# Export Finalization Tests


def test_finalize_exported_decks_marks_as_exported(
    client: TestClient,
    session: db.Session,
    export_user,
    export_deck1,
    export_deck2,
    monkeypatch,
):
    """Test that finalization endpoint marks decks as exported"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Verify decks start as unexported
    assert export_deck1.is_exported == False
    assert export_deck2.is_exported == False

    # Finalize export for both decks
    created_dates = [export_deck1.created.isoformat(), export_deck2.created.isoformat()]
    response = client.post(
        f"/v2/decks/export/{export_user.deck_export_uuid}", json=created_dates
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Verify decks are now marked as exported
    session.refresh(export_deck1)
    session.refresh(export_deck2)
    assert export_deck1.is_exported == True
    assert export_deck2.is_exported == True


def test_finalize_exported_decks_validates_batch_size(
    client: TestClient, session: db.Session, export_user, monkeypatch
):
    """Test that finalization endpoint validates batch size limits"""
    # Enable exports with small batch size
    utils.monkeypatch_settings(
        monkeypatch, {"allow_exports": True, "exports_per_request": 2}
    )

    # Create more dates than allowed batch size
    base_date = utcnow()
    too_many_dates = [
        (base_date - timedelta(days=i)).isoformat() for i in range(3)
    ]  # 3 > 2

    response = client.post(
        f"/v2/decks/export/{export_user.deck_export_uuid}", json=too_many_dates
    )

    data = response.json()
    assert response.status_code == status.HTTP_400_BAD_REQUEST, data
    assert "cannot mark more than 2 decks" in data["detail"]


def test_finalize_exported_decks_requires_valid_token(
    client: TestClient, session: db.Session, monkeypatch
):
    """Test that finalization endpoint requires a valid export token"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Use invalid token
    invalid_token = uuid.uuid4()
    created_dates = [utcnow().isoformat()]

    response = client.post(f"/v2/decks/export/{invalid_token}", json=created_dates)

    data = response.json()
    assert response.status_code == status.HTTP_404_NOT_FOUND, data
    assert "No user matching export token" in data["detail"]


def test_finalize_exported_decks_fails_when_exports_disabled(
    client: TestClient, session: db.Session, export_user, monkeypatch
):
    """Test that finalization endpoint fails when exports are disabled"""
    # Disable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": False})

    created_dates = [utcnow().isoformat()]
    response = client.post(
        f"/v2/decks/export/{export_user.deck_export_uuid}", json=created_dates
    )

    data = response.json()
    assert response.status_code == status.HTTP_400_BAD_REQUEST, data
    assert "not allowed" in data["detail"]


def test_finalize_exported_decks_validates_created_dates(
    client: TestClient, session: db.Session, export_user, monkeypatch
):
    """Test that finalization endpoint validates created dates are provided"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Send empty list of dates
    response = client.post(f"/v2/decks/export/{export_user.deck_export_uuid}", json=[])

    data = response.json()
    assert response.status_code == status.HTTP_400_BAD_REQUEST, data
    assert "must pass one or more created dates" in data["detail"]


def test_finalize_exported_decks_only_updates_user_decks(
    client: TestClient, session: db.Session, export_user, monkeypatch
):
    """Test that finalization only marks decks belonging to the export token user"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Create another user with a deck
    other_user, _ = utils.create_user_token(session)
    other_deck = create_deck_for_user(session, other_user, release_stub="master-set")

    # Create deck for export_user with same created date as other_deck
    export_user_deck = create_deck_for_user(
        session, export_user, release_stub="master-set"
    )
    export_user_deck.created = other_deck.created  # Same date
    session.commit()

    # Verify both start as unexported
    assert export_user_deck.is_exported == False
    assert other_deck.is_exported == False

    # Finalize export using export_user's token
    created_dates = [other_deck.created.isoformat()]  # This date matches both decks
    response = client.post(
        f"/v2/decks/export/{export_user.deck_export_uuid}", json=created_dates
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Only export_user's deck should be marked as exported
    session.refresh(export_user_deck)
    session.refresh(other_deck)
    assert export_user_deck.is_exported == True
    assert other_deck.is_exported == False  # Other user's deck unchanged


# Edge Cases and Error Handling


def test_export_decks_handles_nonexistent_share_uuid(
    client: TestClient, session: db.Session, export_user, monkeypatch
):
    """Test that export endpoint handles requests for non-existent share UUIDs"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Use a non-existent share UUID
    nonexistent_uuid = uuid.uuid4()
    response = client.get(
        f"/v2/decks/export/{export_user.deck_export_uuid}?deck_share_uuid={nonexistent_uuid}"
    )

    data = response.json()
    assert response.status_code == status.HTTP_404_NOT_FOUND, data
    assert "does not have a deck with this share UUID" in data["detail"]


def test_export_decks_handles_snapshot_as_initial_deck(
    client: TestClient, session: db.Session, export_user, monkeypatch
):
    """Test that export endpoint correctly resolves snapshots to their source deck"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Create a source deck and its snapshot
    source_deck = create_deck_for_user(session, export_user, release_stub="master-set")
    snapshot = create_snapshot_for_deck(
        session, export_user, source_deck, title="Test Snapshot", is_public=True
    )

    # Export using the snapshot's share UUID (should resolve to source deck)
    response = client.get(
        f"/v2/decks/export/{export_user.deck_export_uuid}?deck_share_uuid={snapshot.direct_share_uuid}"
    )

    data = response.json()
    assert response.status_code == status.HTTP_200_OK, data
    # Should export both source deck and snapshot
    assert data["total"] == 2

    # Verify both decks are included
    exported_created_dates = {deck["created"] for deck in data["decks"]}
    assert pydantic_style_datetime_str(source_deck.created) in exported_created_dates
    assert pydantic_style_datetime_str(snapshot.created) in exported_created_dates


def test_export_decks_pagination_boundary_conditions(
    client: TestClient, session: db.Session, export_user, monkeypatch
):
    """Test export pagination at boundary conditions (exactly at limit, etc.)"""
    # Set exports per request to exactly match number of decks we'll create
    utils.monkeypatch_settings(
        monkeypatch, {"allow_exports": True, "exports_per_request": 3}
    )

    # Create exactly 1 deck (matching the limit with the 2 from fixtures)
    _deck3 = create_deck_for_user(session, export_user, release_stub="master-set")

    response = client.get(f"/v2/decks/export/{export_user.deck_export_uuid}")

    data = response.json()
    assert response.status_code == status.HTTP_200_OK, data
    assert data["total"] == 3
    assert len(data["decks"]) == 3
    assert data["next_page_from_date"] is None  # No more pages

    # Test with limit + 1 decks (should trigger pagination)
    _deck4 = create_deck_for_user(session, export_user, release_stub="expansion")

    response = client.get(f"/v2/decks/export/{export_user.deck_export_uuid}")
    data = response.json()
    assert data["total"] == 4
    assert len(data["decks"]) == 3  # Still limited by exports_per_request
    assert data["next_page_from_date"] is not None  # Have another page


def test_export_decks_empty_result_set(
    client: TestClient, session: db.Session, export_user, monkeypatch
):
    """Test export endpoint behavior when no decks match the criteria"""
    # Enable exports
    utils.monkeypatch_settings(monkeypatch, {"allow_exports": True})

    # Test with date filter that matches no decks (future date)
    future_date = utcnow() + timedelta(days=1)
    response = client.get(
        f"/v2/decks/export/{export_user.deck_export_uuid}?from_date={pydantic_style_datetime_str(future_date)}"
    )

    data = response.json()
    assert response.status_code == status.HTTP_200_OK, data
    assert data["total"] == 0
    assert data["decks"] == []
    assert data["next_page_from_date"] is None

"""Tests for deck import functionality

These tests cover the import endpoint that allows one Ashes.live instance
to pull deck data from another instance for migration purposes.
"""

import uuid
from datetime import datetime, timedelta
from unittest.mock import Mock

import httpx
import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models import Deck
from api.tests import utils
from api.utils.dates import pydantic_style_datetime_str, utcnow

from .deck_utils import create_deck_for_user

# Shared fixtures


@pytest.fixture(scope="module", autouse=True)
def user_token(decks_session):
    """User and token for import tests"""
    user, token = utils.create_user_token(decks_session)
    return user, token


def _create_mock_export_response(decks_data, total=None, next_page_from_date=None):
    """Helper to create a mock export API response"""
    response = Mock()
    response.status_code = 200
    response.raise_for_status = Mock()
    response.json.return_value = {
        "decks": decks_data,
        "total": total or len(decks_data),
        "next_page_from_date": next_page_from_date,
    }
    return response


def _create_mock_deck_data(
    created_date,
    title="Test Deck",
    phoenixborn_stub="one-phoenixborn",
    is_snapshot=False,
    source_created=None,
):
    """Helper to create mock deck export data"""
    return {
        "title": title,
        "description": "Test description",
        "created": (
            pydantic_style_datetime_str(created_date)
            if isinstance(created_date, datetime)
            else created_date
        ),
        "modified": (
            pydantic_style_datetime_str(created_date)
            if isinstance(created_date, datetime)
            else created_date
        ),
        "dice": [{"name": "natural", "count": 5}, {"name": "sympathy", "count": 3}],
        "phoenixborn": {
            "name": "One Phoenixborn",
            "stub": phoenixborn_stub,
            "type": "Phoenixborn",
            "battlefield": 4,
            "life": 20,
            "spellboard": 5,
        },
        "cards": [
            {
                "name": "One Action Spell A",
                "stub": "one-action-spell-a",
                "count": 3,
                "type": "Action Spell",
            }
        ],
        "conjurations": [],
        "is_public": False,
        "is_snapshot": is_snapshot,
        "is_red_rains": False,
        "first_five": [],
        "effect_costs": [],
        "tutor_map": {},
        "source_created": (
            pydantic_style_datetime_str(source_created) if source_created else None
        ),
    }


# Authentication and Validation


def test_import_decks_requires_authentication(client: TestClient):
    """Test that import endpoint requires user authentication"""
    export_token = uuid.uuid4()
    response = client.get(f"/v2/decks/import/{export_token}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.json()


def test_import_decks_validates_export_token_format(
    client: TestClient, session: db.Session, user_token
):
    """Test that import endpoint validates export token is a valid UUID"""
    user, token = user_token

    # Test with invalid UUID format
    response = client.get(
        "/v2/decks/import/invalid-uuid", headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()


def test_import_decks_handles_invalid_from_api_format(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint handles malformed from_api parameter"""
    user, token = user_token
    export_token = uuid.uuid4()

    # Mock httpx.get to simulate connection error without making real network calls
    def mock_httpx_get(*args, **kwargs):
        raise httpx.RequestError(
            "Connection error", request=httpx.Request("GET", "https://example.com")
        )

    monkeypatch.setattr(httpx, "get", mock_httpx_get)

    # The endpoint should normalize malformed URLs (add https, remove trailing slash)
    # This test verifies the endpoint can handle various URL formats
    response = client.get(
        f"/v2/decks/import/{export_token}?from_api=malformed-url-without-protocol/",
        headers={"Authorization": f"Bearer {token}"},
    )

    # The endpoint will normalize the URL and attempt to connect
    # Since we've mocked the connection to fail, we expect a connection error
    data = response.json()
    assert response.status_code == status.HTTP_400_BAD_REQUEST, data
    assert "Unable to connect to source API" in data["detail"]


def test_import_decks_validates_date_parameters(
    client: TestClient, session: db.Session, user_token
):
    """Test that import endpoint validates from_date parameter format"""
    user, token = user_token
    export_token = uuid.uuid4()

    # Test with invalid date format
    response = client.get(
        f"/v2/decks/import/{export_token}?from_date=invalid-date",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()


def test_import_decks_validates_deck_share_uuid_format(
    client: TestClient, session: db.Session, user_token
):
    """Test that import endpoint validates deck_share_uuid parameter format"""
    user, token = user_token
    export_token = uuid.uuid4()

    # Test with invalid UUID format
    response = client.get(
        f"/v2/decks/import/{export_token}?deck_share_uuid=invalid-uuid",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()


# Success Scenarios


def test_import_decks_creates_new_decks(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint creates new decks from export data"""
    user, token = user_token
    export_token = uuid.uuid4()

    # Create mock export data with two new decks
    deck1_created = utcnow() - timedelta(days=2)
    deck2_created = utcnow() - timedelta(days=1)

    mock_decks = [
        _create_mock_deck_data(deck1_created, "Imported Deck 1"),
        _create_mock_deck_data(deck2_created, "Imported Deck 2"),
    ]

    mock_response = _create_mock_export_response(mock_decks)

    def mock_httpx_get(*args, **kwargs):
        return mock_response

    def mock_httpx_post(*args, **kwargs):
        # Mock successful notification
        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    # Verify no decks exist initially
    assert session.query(Deck).filter(Deck.user_id == user.id).count() == 0

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Verify response structure
    assert data["total_count"] == 2
    assert data["success_count"] == 2
    assert len(data["errors"]) == 0

    # Verify decks were created in database
    created_decks = session.query(Deck).filter(Deck.user_id == user.id).all()
    assert len(created_decks) == 2

    # Verify deck details
    deck_titles = [d.title for d in created_decks]
    assert "Imported Deck 1" in deck_titles
    assert "Imported Deck 2" in deck_titles


def test_import_decks_updates_existing_decks(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint updates existing decks based on created date"""
    user, token = user_token
    export_token = uuid.uuid4()

    # Create an existing deck with a specific created date
    existing_created = utcnow() - timedelta(days=3)
    existing_deck = create_deck_for_user(session, user)
    existing_deck.created = existing_created
    existing_deck.title = "Original Title"
    existing_deck.description = "Original Description"
    session.commit()

    # Create mock export data that updates the existing deck
    mock_deck_data = _create_mock_deck_data(
        existing_created, "Updated Title", "one-phoenixborn"
    )
    mock_deck_data["description"] = "Updated Description"

    mock_response = _create_mock_export_response([mock_deck_data])

    def mock_httpx_get(*args, **kwargs):
        return mock_response

    def mock_httpx_post(*args, **kwargs):
        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["total_count"] == 1
    assert data["success_count"] == 1
    assert len(data["errors"]) == 0

    # Verify deck was updated, not duplicated
    user_decks = session.query(Deck).filter(Deck.user_id == user.id).all()
    assert len(user_decks) == 1

    updated_deck = user_decks[0]
    assert updated_deck.title == "Updated Title"
    assert updated_deck.description == "Updated Description"


def test_import_decks_handles_snapshots_and_sources(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint correctly handles deck snapshots and source relationships"""
    user, token = user_token
    export_token = uuid.uuid4()

    # Create mock data: source deck and its snapshot
    source_created = utcnow() - timedelta(days=5)
    snapshot_created = utcnow() - timedelta(days=1)

    source_deck_data = _create_mock_deck_data(
        source_created, "Source Deck", "one-phoenixborn", is_snapshot=False
    )

    snapshot_deck_data = _create_mock_deck_data(
        snapshot_created,
        "Snapshot Deck",
        "one-phoenixborn",
        is_snapshot=True,
        source_created=source_created,
    )

    mock_response = _create_mock_export_response([source_deck_data, snapshot_deck_data])

    def mock_httpx_get(*args, **kwargs):
        return mock_response

    def mock_httpx_post(*args, **kwargs):
        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["total_count"] == 2
    assert data["success_count"] == 2
    assert len(data["errors"]) == 0

    # Verify both decks were created
    created_decks = session.query(Deck).filter(Deck.user_id == user.id).all()
    assert len(created_decks) == 2

    # Find source and snapshot
    source_deck = next((d for d in created_decks if not d.is_snapshot), None)
    snapshot_deck = next((d for d in created_decks if d.is_snapshot), None)

    assert source_deck is not None
    assert snapshot_deck is not None
    assert snapshot_deck.source_id == source_deck.id


def test_import_decks_imports_selected_cards(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint correctly imports first_five, effect_costs, and tutor_map data"""
    user, token = user_token
    export_token = uuid.uuid4()

    created_date = utcnow() - timedelta(days=1)

    # Create mock deck data with selected cards data
    mock_deck_data = _create_mock_deck_data(created_date, "Deck with Selected Cards")
    # Add extra cards so that we can set First Five and such
    mock_deck_data["cards"] += [
        {
            "name": "One Ready Spell A",
            "stub": "one-ready-spell-a",
            "count": 3,
            "type": "Ready Spell",
        },
        {
            "name": "One Ally",
            "stub": "one-ally",
            "count": 3,
            "type": "Ally",
        },
    ]
    # Actually specify our First Five, effect costs, etc.
    mock_deck_data["first_five"] = [
        "one-action-spell-a",
        "one-ready-spell-a",
        "one-ally",
    ]
    mock_deck_data["effect_costs"] = ["one-ready-spell-a"]
    mock_deck_data["tutor_map"] = {"one-action-spell-a": "one-ready-spell-a"}

    mock_response = _create_mock_export_response([mock_deck_data])

    def mock_httpx_get(*args, **kwargs):
        return mock_response

    def mock_httpx_post(*args, **kwargs):
        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["success_count"] == 1

    # Verify deck was created with selected cards data
    created_deck = session.query(Deck).filter(Deck.user_id == user.id).first()
    assert created_deck is not None

    # Check selected cards relationships
    selected_cards = created_deck.selected_cards
    first_five_cards = [sc for sc in selected_cards if sc.is_first_five]
    effect_cost_cards = [sc for sc in selected_cards if sc.is_paid_effect]
    tutor_cards = [sc for sc in selected_cards if sc.tutor_card_id != 0]

    # Verify selected cards were imported correctly
    assert len(first_five_cards) == 3
    assert len(effect_cost_cards) == 1
    assert len(tutor_cards) == 1


def test_import_decks_single_deck_import(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint can import a single deck and its snapshots"""
    user, token = user_token
    export_token = uuid.uuid4()
    target_deck_uuid = uuid.uuid4()

    # Create mock data: specific deck and its snapshot
    source_created = utcnow() - timedelta(days=5)
    snapshot_created = utcnow() - timedelta(days=1)

    source_deck_data = _create_mock_deck_data(
        source_created, "Target Deck", "one-phoenixborn", is_snapshot=False
    )

    snapshot_deck_data = _create_mock_deck_data(
        snapshot_created,
        "Target Deck Snapshot",
        "one-phoenixborn",
        is_snapshot=True,
        source_created=source_created,
    )

    mock_response = _create_mock_export_response([source_deck_data, snapshot_deck_data])

    def mock_httpx_get(url, **kwargs):
        # Verify the correct parameters are passed for single deck import
        params = kwargs.get("params", {})
        assert params.get("deck_share_uuid") == str(target_deck_uuid)
        return mock_response

    def mock_httpx_post(*args, **kwargs):
        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}?deck_share_uuid={target_deck_uuid}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["total_count"] == 2
    assert data["success_count"] == 2
    assert len(data["errors"]) == 0

    # Verify both the deck and its snapshot were imported
    created_decks = session.query(Deck).filter(Deck.user_id == user.id).all()
    assert len(created_decks) == 2

    source_deck = next((d for d in created_decks if not d.is_snapshot), None)
    snapshot_deck = next((d for d in created_decks if d.is_snapshot), None)

    assert source_deck is not None
    assert snapshot_deck is not None
    assert snapshot_deck.source_id == source_deck.id
    assert source_deck.title == "Target Deck"
    assert snapshot_deck.title == "Target Deck Snapshot"


def test_import_decks_pagination_handling(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint handles pagination correctly with next_page_from_date"""
    from api.tests import utils

    user, token = user_token
    export_token = uuid.uuid4()

    # Mock smaller page size for testing
    utils.monkeypatch_settings(monkeypatch, {"exports_per_request": 1})

    # Create mock data for multiple pages
    deck1_created = utcnow() - timedelta(days=3)
    deck2_created = utcnow() - timedelta(days=2)
    deck3_created = utcnow() - timedelta(days=1)

    # First page response
    first_page_response = _create_mock_export_response(
        [_create_mock_deck_data(deck1_created, "Deck 1")],
        total=3,
        next_page_from_date=deck2_created,
    )

    # Second page response
    second_page_response = _create_mock_export_response(
        [_create_mock_deck_data(deck2_created, "Deck 2")],
        total=3,
        next_page_from_date=deck3_created,
    )

    # Third page response
    third_page_response = _create_mock_export_response(
        [_create_mock_deck_data(deck3_created, "Deck 3")],
        total=3,
        next_page_from_date=None,
    )

    call_count = 0

    def mock_httpx_get(url, **kwargs):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            return first_page_response
        elif call_count == 2:
            # Verify pagination parameter is passed
            assert f"from_date={pydantic_style_datetime_str(deck2_created)}" in url
            return second_page_response
        else:
            assert f"from_date={pydantic_style_datetime_str(deck3_created)}" in url
            return third_page_response

    def mock_httpx_post(*args, **kwargs):
        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["total_count"] == 3  # This comes from the first response
    assert data["success_count"] == 1  # Only first page is actually imported
    assert len(data["errors"]) == 0
    assert data["next_page_from_date"] is not None  # Should have next page info

    # Verify only first deck was imported (pagination handled by front-end)
    created_decks = session.query(Deck).filter(Deck.user_id == user.id).all()
    assert len(created_decks) == 1

    deck_titles = [d.title for d in created_decks]
    assert "Deck 1" in deck_titles

    # Verify only one HTTP request was made (pagination handled by front-end)
    assert call_count == 1


# Error Scenarios


def test_import_decks_handles_missing_cards(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint handles decks with cards that don't exist in destination"""
    user, token = user_token
    export_token = uuid.uuid4()

    created_date = utcnow() - timedelta(days=1)

    # Create mock deck data with cards that don't exist in test database
    mock_deck_data = _create_mock_deck_data(created_date, "Deck with Missing Cards")
    mock_deck_data["cards"] = [
        {
            "name": "Nonexistent Card A",
            "stub": "nonexistent-card-a",
            "count": 3,
            "type": "Action Spell",
        },
        {
            "name": "One Action Spell A",  # This one exists
            "stub": "one-action-spell-a",
            "count": 3,
            "type": "Action Spell",
        },
        {
            "name": "Nonexistent Card B",
            "stub": "nonexistent-card-b",
            "count": 2,
            "type": "Ready Spell",
        },
    ]

    mock_response = _create_mock_export_response([mock_deck_data])

    def mock_httpx_get(*args, **kwargs):
        return mock_response

    def mock_httpx_post(*args, **kwargs):
        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Import should fail due to missing cards
    assert data["total_count"] == 1
    assert data["success_count"] == 0
    assert len(data["errors"]) == 1
    assert "missing cards" in data["errors"][0].lower()

    # Verify no decks were created
    created_decks = session.query(Deck).filter(Deck.user_id == user.id).all()
    assert len(created_decks) == 0


def test_import_decks_handles_missing_phoenixborn(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint handles decks with phoenixborn that don't exist in destination"""
    user, token = user_token
    export_token = uuid.uuid4()

    created_date = utcnow() - timedelta(days=1)

    # Create mock deck data with nonexistent phoenixborn
    mock_deck_data = _create_mock_deck_data(
        created_date, "Deck with Missing Phoenixborn"
    )
    mock_deck_data["phoenixborn"] = {
        "name": "Nonexistent Phoenixborn",
        "stub": "nonexistent-phoenixborn",
        "type": "Phoenixborn",
        "battlefield": 4,
        "life": 20,
        "spellboard": 5,
    }

    mock_response = _create_mock_export_response([mock_deck_data])

    def mock_httpx_get(*args, **kwargs):
        return mock_response

    def mock_httpx_post(*args, **kwargs):
        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Import should fail due to missing phoenixborn
    assert data["total_count"] == 1
    assert data["success_count"] == 0
    assert len(data["errors"]) == 1
    assert "missing phoenixborn" in data["errors"][0].lower()

    # Verify no decks were created
    created_decks = session.query(Deck).filter(Deck.user_id == user.id).all()
    assert len(created_decks) == 0


def test_import_decks_handles_http_errors(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint handles HTTP errors from source API gracefully"""
    user, token = user_token
    export_token = uuid.uuid4()

    # Mock HTTP error response
    def mock_httpx_get(*args, **kwargs):
        error_response = Mock()
        error_response.status_code = 404
        error_response.json.return_value = {"detail": "Export token not found"}
        error = httpx.HTTPStatusError(
            "404 Not Found",
            request=httpx.Request("GET", "https://example.com"),
            response=error_response,
        )
        raise error

    monkeypatch.setattr(httpx, "get", mock_httpx_get)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    data = response.json()
    assert "Source API responded with error" in data["detail"]
    assert "Export token not found" in data["detail"]


def test_import_decks_handles_network_errors(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint handles network connectivity errors gracefully"""
    user, token = user_token
    export_token = uuid.uuid4()

    # Mock network connection error
    def mock_httpx_get(*args, **kwargs):
        error = httpx.RequestError(
            "Connection timeout", request=httpx.Request("GET", "https://example.com")
        )
        raise error

    monkeypatch.setattr(httpx, "get", mock_httpx_get)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    data = response.json()
    assert "Unable to connect to source API" in data["detail"]


def test_import_decks_handles_source_api_error_response(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint handles error responses from source API"""
    user, token = user_token
    export_token = uuid.uuid4()

    # Mock API returning successful HTTP status but with error in response body
    def mock_httpx_get(*args, **kwargs):
        response = Mock()
        response.status_code = 200
        response.raise_for_status = Mock()
        response.json.return_value = {
            "decks": [],
            "total": 0,
            "next_page_from_date": None,
            "error": "Export token has expired",
        }
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Should handle gracefully with no decks imported
    assert data["total_count"] == 0
    assert data["success_count"] == 0
    assert len(data["errors"]) == 0


def test_import_decks_handles_partial_import_failures(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint handles cases where some decks fail to import"""
    user, token = user_token
    export_token = uuid.uuid4()

    # Create a mix of valid and invalid deck data
    deck1_created = utcnow() - timedelta(days=2)
    deck2_created = utcnow() - timedelta(days=1)

    # Valid deck
    valid_deck = _create_mock_deck_data(deck1_created, "Valid Deck")

    # Invalid deck with missing phoenixborn
    invalid_deck = _create_mock_deck_data(deck2_created, "Invalid Deck")
    invalid_deck["phoenixborn"] = {
        "name": "Missing Phoenixborn",
        "stub": "missing-phoenixborn",
        "type": "Phoenixborn",
        "battlefield": 4,
        "life": 20,
        "spellboard": 5,
    }

    mock_response = _create_mock_export_response([valid_deck, invalid_deck])

    def mock_httpx_get(*args, **kwargs):
        return mock_response

    def mock_httpx_post(*args, **kwargs):
        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Should have partial success
    assert data["total_count"] == 2
    assert data["success_count"] == 1
    assert len(data["errors"]) == 1
    assert "missing phoenixborn" in data["errors"][0].lower()

    # Verify only the valid deck was created
    created_decks = session.query(Deck).filter(Deck.user_id == user.id).all()
    assert len(created_decks) == 1
    assert created_decks[0].title == "Valid Deck"


# HTTP Request Handling


def test_import_decks_constructs_correct_export_url(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint constructs the correct URL for the export API call"""
    user, token = user_token
    export_token = uuid.uuid4()

    requested_url = None

    def mock_httpx_get(url, **kwargs):
        nonlocal requested_url
        requested_url = url

        # Return minimal valid response
        response = Mock()
        response.status_code = 200
        response.raise_for_status = Mock()
        response.json.return_value = {
            "decks": [],
            "total": 0,
            "next_page_from_date": None,
        }
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)

    # Test with default from_api
    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK

    # Verify correct URL was constructed
    assert requested_url == f"https://api.ashes.live/v2/decks/export/{export_token}"

    # Test with custom from_api
    response = client.get(
        f"/v2/decks/import/{export_token}?from_api=custom.example.com",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert requested_url == f"https://custom.example.com/v2/decks/export/{export_token}"


def test_import_decks_passes_correct_parameters(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint passes from_date and deck_share_uuid parameters correctly"""
    user, token = user_token
    export_token = uuid.uuid4()

    requested_params = None

    def mock_httpx_get(url, **kwargs):
        nonlocal requested_params
        requested_params = kwargs.get("params", {})

        # Return minimal valid response
        response = Mock()
        response.status_code = 200
        response.raise_for_status = Mock()
        response.json.return_value = {
            "decks": [],
            "total": 0,
            "next_page_from_date": None,
        }
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)

    # Test with from_date parameter
    test_date = utcnow() - timedelta(days=1)
    response = client.get(
        f"/v2/decks/import/{export_token}?from_date={pydantic_style_datetime_str(test_date)}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert "from_date" in requested_params
    assert requested_params["from_date"] == test_date.isoformat()

    # Test with deck_share_uuid parameter
    test_uuid = uuid.uuid4()
    response = client.get(
        f"/v2/decks/import/{export_token}?deck_share_uuid={test_uuid}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert "deck_share_uuid" in requested_params
    assert requested_params["deck_share_uuid"] == str(test_uuid)

    # Test with both parameters
    response = client.get(
        f"/v2/decks/import/{export_token}?from_date={pydantic_style_datetime_str(test_date)}&deck_share_uuid={test_uuid}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert "from_date" in requested_params
    assert "deck_share_uuid" in requested_params
    assert requested_params["from_date"] == test_date.isoformat()
    assert requested_params["deck_share_uuid"] == str(test_uuid)


def test_import_decks_handles_url_normalization(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint normalizes from_api URLs (adds https, removes trailing slash)"""
    user, token = user_token
    export_token = uuid.uuid4()

    requested_url = None

    def mock_httpx_get(url, **kwargs):
        nonlocal requested_url
        requested_url = url

        # Return minimal valid response
        response = Mock()
        response.status_code = 200
        response.raise_for_status = Mock()
        response.json.return_value = {
            "decks": [],
            "total": 0,
            "next_page_from_date": None,
        }
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)

    # Test URL without protocol gets https added
    response = client.get(
        f"/v2/decks/import/{export_token}?from_api=example.com",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert requested_url == f"https://example.com/v2/decks/export/{export_token}"

    # Test URL with trailing slash gets it removed
    response = client.get(
        f"/v2/decks/import/{export_token}?from_api=https://example.com/",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert requested_url == f"https://example.com/v2/decks/export/{export_token}"

    # Test URL without protocol and with trailing slash
    response = client.get(
        f"/v2/decks/import/{export_token}?from_api=example.com/",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert requested_url == f"https://example.com/v2/decks/export/{export_token}"


def test_import_decks_sends_success_notification(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint sends POST request to finalize successful imports"""
    user, token = user_token
    export_token = uuid.uuid4()

    created_date1 = utcnow() - timedelta(days=2)
    created_date2 = utcnow() - timedelta(days=1)

    mock_decks = [
        _create_mock_deck_data(created_date1, "Imported Deck 1"),
        _create_mock_deck_data(created_date2, "Imported Deck 2"),
    ]
    mock_response = _create_mock_export_response(mock_decks)

    post_url = None
    post_data = None

    def mock_httpx_get(*args, **kwargs):
        return mock_response

    def mock_httpx_post(url, **kwargs):
        nonlocal post_url, post_data
        post_url = url
        post_data = kwargs.get("json", [])

        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK

    # Verify notification was sent
    assert post_url == f"https://api.ashes.live/v2/decks/export/{export_token}"
    assert isinstance(post_data, list)
    assert len(post_data) == 2

    # Verify notification contains created dates of successfully imported decks
    assert pydantic_style_datetime_str(created_date1) in post_data
    assert pydantic_style_datetime_str(created_date2) in post_data


def test_import_decks_handles_notification_failure(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint handles failures when notifying source of successful imports"""
    user, token = user_token
    export_token = uuid.uuid4()

    created_date = utcnow() - timedelta(days=1)
    mock_decks = [_create_mock_deck_data(created_date, "Imported Deck")]
    mock_response = _create_mock_export_response(mock_decks)

    def mock_httpx_get(*args, **kwargs):
        return mock_response

    def mock_httpx_post(*args, **kwargs):
        # Simulate notification failure
        error = httpx.RequestError(
            "Connection timeout", request=httpx.Request("POST", "https://example.com")
        )
        raise error

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    # Notification failure should cause the import to fail
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    data = response.json()
    assert "Unable to connect to source API" in data["detail"]


# Edge Cases


def test_import_decks_handles_dice_validation(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint validates and limits dice counts properly"""
    user, token = user_token
    export_token = uuid.uuid4()

    created_date = utcnow() - timedelta(days=1)

    # Create mock deck data with excessive dice counts (over 10 total)
    mock_deck_data = _create_mock_deck_data(created_date, "Deck with Invalid Dice")
    mock_deck_data["dice"] = [
        {"name": "natural", "count": 5},
        {"name": "sympathy", "count": 4},
        {"name": "time", "count": 3},  # Total would be 12, exceeding limit of 10
    ]

    mock_response = _create_mock_export_response([mock_deck_data])

    def mock_httpx_get(*args, **kwargs):
        return mock_response

    def mock_httpx_post(*args, **kwargs):
        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Import should succeed but dice counts should be capped at 10
    assert data["total_count"] == 1
    assert data["success_count"] == 1
    assert len(data["errors"]) == 0

    # Verify deck was created with capped dice counts
    created_decks = session.query(Deck).filter(Deck.user_id == user.id).all()
    assert len(created_decks) == 1

    created_deck = created_decks[0]
    deck_dice = created_deck.dice
    total_dice_count = sum(die.count for die in deck_dice)
    assert total_dice_count == 10  # Should be capped at 10, not 12


def test_import_decks_handles_empty_export_response(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint handles empty deck lists from source API"""
    user, token = user_token
    export_token = uuid.uuid4()

    # Create mock response with empty deck list
    mock_response = _create_mock_export_response([], total=0)

    def mock_httpx_get(*args, **kwargs):
        return mock_response

    def mock_httpx_post(*args, **kwargs):
        # Should not be called since no decks were successfully imported
        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Should handle empty response gracefully
    assert data["total_count"] == 0
    assert data["success_count"] == 0
    assert len(data["errors"]) == 0
    assert data["next_page_from_date"] is None

    # Verify no decks were created
    created_decks = session.query(Deck).filter(Deck.user_id == user.id).all()
    assert len(created_decks) == 0


def test_import_decks_preserves_deck_relationships(
    client: TestClient, session: db.Session, user_token, monkeypatch
):
    """Test that import endpoint preserves snapshot-to-source deck relationships"""
    user, token = user_token
    export_token = uuid.uuid4()

    # Create mock data: source deck and two snapshots
    source_created = utcnow() - timedelta(days=5)
    snapshot1_created = utcnow() - timedelta(days=3)
    snapshot2_created = utcnow() - timedelta(days=1)

    source_deck_data = _create_mock_deck_data(
        source_created, "Original Source Deck", "one-phoenixborn", is_snapshot=False
    )

    # First snapshot points to source
    snapshot1_deck_data = _create_mock_deck_data(
        snapshot1_created,
        "First Snapshot",
        "one-phoenixborn",
        is_snapshot=True,
        source_created=source_created,
    )

    # Second snapshot also points to original source (not to snapshot1)
    snapshot2_deck_data = _create_mock_deck_data(
        snapshot2_created,
        "Second Snapshot",
        "one-phoenixborn",
        is_snapshot=True,
        source_created=source_created,  # Points to original source, not snapshot1
    )

    mock_response = _create_mock_export_response(
        [source_deck_data, snapshot1_deck_data, snapshot2_deck_data]
    )

    def mock_httpx_get(*args, **kwargs):
        return mock_response

    def mock_httpx_post(*args, **kwargs):
        response = Mock()
        response.status_code = 200
        return response

    monkeypatch.setattr(httpx, "get", mock_httpx_get)
    monkeypatch.setattr(httpx, "post", mock_httpx_post)

    response = client.get(
        f"/v2/decks/import/{export_token}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["total_count"] == 3
    assert data["success_count"] == 3
    assert len(data["errors"]) == 0

    # Verify all decks were created
    created_decks = session.query(Deck).filter(Deck.user_id == user.id).all()
    assert len(created_decks) == 3

    # Find the decks by type
    source_deck = next((d for d in created_decks if not d.is_snapshot), None)
    snapshot_decks = [d for d in created_decks if d.is_snapshot]

    assert source_deck is not None
    assert len(snapshot_decks) == 2
    assert source_deck.title == "Original Source Deck"

    # Verify both snapshots point to the source deck
    for snapshot in snapshot_decks:
        assert snapshot.source_id == source_deck.id
        assert snapshot.title in ["First Snapshot", "Second Snapshot"]

    # Verify snapshots don't point to each other
    snapshot_titles = [s.title for s in snapshot_decks]
    assert "First Snapshot" in snapshot_titles
    assert "Second Snapshot" in snapshot_titles

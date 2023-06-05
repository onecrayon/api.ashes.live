import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models import Card, Comment, Subscription
from api.services.deck import create_snapshot_for_deck
from api.services.stream import create_entity
from api.tests.utils import create_user_token

from .deck_utils import create_deck_for_user


@pytest.fixture(scope="module", autouse=True)
def user1(decks_session):
    user1, _ = create_user_token(decks_session)
    return user1


@pytest.fixture(scope="module", autouse=True)
def deck1(decks_session, user1):
    return create_deck_for_user(decks_session, user1, release_stub="master-set")


@pytest.fixture
def subscription(session, user1):
    card = session.query(Card).order_by(Card.id.desc()).first()
    sub = Subscription(
        user_id=user1.id,
        source_entity_id=card.entity_id,
    )
    session.add(sub)
    session.commit()
    return sub


def test_create_subscription(client: TestClient, session: db.Session, user1):
    """Verify that creating a card subscription works properly"""
    card = session.query(Card).first()
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/subscription/{card.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_create_subscription_deck(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify that creating a deck subscription works properly"""
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/subscription/{deck1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_create_subscription_bad_entity_id(
    client: TestClient, session: db.Session, user1
):
    """Verify we cannot subscribe to non-deck/card entity IDs"""
    bad_entity_id = create_entity(session)
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/subscription/{bad_entity_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_create_subscription_legacy(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify we cannot subscribe to legacy content"""
    deck1.is_legacy = True
    session.commit()
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/subscription/{deck1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_subscription_snapshot(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify we cannot subscribe to a snapshot"""
    snapshot = create_snapshot_for_deck(
        session,
        user1,
        deck1,
        title="First Snapshot",
        description="First description",
        is_public=True,
    )
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/subscription/{snapshot.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_subscription_existing_subscription(
    client: TestClient, session: db.Session, user1
):
    """Verify creating a subscription that already exists returns truthy"""
    card = session.query(Card).first()
    sub = Subscription(
        user_id=user1.id,
        source_entity_id=card.entity_id,
    )
    session.add(sub)
    session.commit()
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/subscription/{card.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_create_subscription_last_entity_id(
    client: TestClient, session: db.Session, user1
):
    """Verify subscriptions populate the last seen entity ID properly"""
    card = session.query(Card).first()
    # Add a pre-existing comment
    comment = Comment(
        entity_id=create_entity(session),
        user_id=user1.id,
        source_entity_id=card.entity_id,
        source_type="card",
        source_version=card.version,
        text="My first comment",
        ordering_increment=1,
    )
    session.add(comment)
    session.commit()
    # Create our subscription
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/subscription/{card.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    # Verify the last_seen_entity_id matches our previous comment
    subscription = (
        session.query(Subscription)
        .filter(
            Subscription.source_entity_id == card.entity_id,
            Subscription.user_id == user1.id,
        )
        .first()
    )
    assert subscription.last_seen_entity_id == comment.entity_id


def test_create_subscription_last_entity_id_snapshot(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify that the most recent published snapshot is used as the last seen entity ID for decks"""
    snapshot = create_snapshot_for_deck(
        session,
        user1,
        deck1,
        title="First Snapshot",
        description="First description",
        is_public=True,
    )
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/subscription/{deck1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    # Check the subscription last_seen_entity_id
    subscription = (
        session.query(Subscription)
        .filter(
            Subscription.source_entity_id == deck1.entity_id,
            Subscription.user_id == user1.id,
        )
        .first()
    )
    assert subscription.last_seen_entity_id == snapshot.entity_id


def test_delete_subscription(
    client: TestClient, session: db.Session, deck1, user1, subscription
):
    """Verify that deleting a subscription works"""
    _, token = create_user_token(session, user=user1)
    # No error if the subscription doesn't exist
    response = client.delete(
        f"/v2/subscription/{deck1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    # Properly deletes the subscription
    source_entity_id = subscription.source_entity_id
    response = client.delete(
        f"/v2/subscription/{source_entity_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert (
        session.query(Subscription)
        .filter(
            Subscription.source_entity_id == source_entity_id,
            Subscription.user_id == user1.id,
        )
        .first()
        is None
    )


def test_update_subscription(
    client: TestClient, session: db.Session, user1, subscription
):
    """Verify updating a subscription works properly"""
    # Create a new comment so that we can update the subscription
    comment = Comment(
        entity_id=create_entity(session),
        user_id=user1.id,
        source_entity_id=subscription.source_entity_id,
        source_type="card",
        source_version=1,
        text="My first comment",
        ordering_increment=1,
    )
    session.add(comment)
    session.commit()
    # Run the update
    _, token = create_user_token(session, user=user1)
    response = client.patch(
        f"/v2/subscription/{subscription.source_entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"last_seen_entity_id": comment.entity_id},
    )
    assert response.status_code == status.HTTP_200_OK


def test_update_subscription_no_sub(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify trying to update a subscription that doesn't exist fails"""
    comment = Comment(
        entity_id=create_entity(session),
        user_id=user1.id,
        source_entity_id=deck1.entity_id,
        source_type="deck",
        text="My first comment",
        ordering_increment=1,
    )
    session.add(comment)
    session.commit()
    _, token = create_user_token(session, user=user1)
    response = client.patch(
        f"/v2/subscription/{deck1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"last_seen_entity_id": comment.entity_id},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_subscription_bad_entity_id(
    client: TestClient, session: db.Session, deck1, user1, subscription
):
    """Verify updating to point to an entity ID that isn't related fails"""
    comment = Comment(
        entity_id=create_entity(session),
        user_id=user1.id,
        source_entity_id=subscription.source_entity_id,
        source_type="card",
        source_version=1,
        text="My first comment",
        ordering_increment=1,
    )
    session.add(comment)
    sub = Subscription(
        user_id=user1.id,
        source_entity_id=deck1.entity_id,
    )
    session.add(sub)
    session.commit()
    _, token = create_user_token(session, user=user1)
    response = client.patch(
        f"/v2/subscription/{deck1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"last_seen_entity_id": comment.entity_id},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_update_subscription_snapshot(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify setting the last_seen_entity_id to a snapshot works"""
    sub = Subscription(
        user_id=user1.id,
        source_entity_id=deck1.entity_id,
    )
    session.add(sub)
    session.commit()
    snapshot = create_snapshot_for_deck(
        session,
        user1,
        deck1,
        title="First Snapshot",
        description="First description",
        is_public=True,
    )
    _, token = create_user_token(session, user=user1)
    response = client.patch(
        f"/v2/subscription/{deck1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"last_seen_entity_id": snapshot.entity_id},
    )
    assert response.status_code == status.HTTP_200_OK
    session.refresh(sub)
    assert sub.last_seen_entity_id == snapshot.entity_id

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy import select

from api import db
from api.models import Card, Comment
from api.services.deck import create_snapshot_for_deck
from api.services.stream import create_entity

from ..utils import create_admin_token, create_user_token
from .deck_utils import create_deck_for_user


@pytest.fixture(scope="function", autouse=True)
def user1(session):
    user1, _ = create_user_token(session)
    return user1


@pytest.fixture(scope="function", autouse=True)
def deck1(session, user1):
    return create_deck_for_user(session, user1, release_stub="master-set")


@pytest.fixture(scope="function", autouse=True)
def snapshot1(session, user1, deck1):
    return create_snapshot_for_deck(
        session,
        user1,
        deck1,
        title="First Snapshot",
        description="First description",
        is_public=True,
    )


def test_get_comments(client: TestClient, session: db.Session, deck1, user1):
    """Verify listing comments works properly"""
    # Add a comment that we don't want to show up in the listing
    deck_comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My deck comment",
    )
    session.add(deck_comment)
    session.commit()
    #  Add the comments we do want to show up in the listing
    stmt = select(Card).limit(1)
    card = session.execute(stmt).scalar()
    comment1 = Comment(
        entity_id=create_entity(session),
        source_entity_id=card.entity_id,
        user_id=user1.id,
        source_type="card",
        source_version=card.version,
        ordering_increment=1,
        text="My first comment",
    )
    session.add(comment1)
    session.commit()
    comment2 = Comment(
        entity_id=create_entity(session),
        source_entity_id=card.entity_id,
        user_id=user1.id,
        source_type="card",
        source_version=card.version,
        ordering_increment=2,
        text="My second comment",
    )
    session.add(comment2)
    session.commit()
    response = client.get(f"/v2/comments/{card.entity_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 2
    assert data["results"][0]["entity_id"] == comment1.entity_id
    assert data["results"][1]["entity_id"] == comment2.entity_id

    # Verify ordering things the other way works
    response = client.get(f"/v2/comments/{card.entity_id}?order=desc")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["results"][0]["entity_id"] == comment2.entity_id
    assert data["results"][1]["entity_id"] == comment1.entity_id


def test_get_comments_deleted(client: TestClient, session: db.Session, deck1, user1):
    """Verify the behavior of deleted comments"""
    comment1 = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
    )
    session.add(comment1)
    session.commit()
    comment2 = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=2,
        text="My second comment",
        is_deleted=True,
    )
    session.add(comment2)
    session.commit()
    comment3 = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=3,
        text="My third comment",
    )
    session.add(comment3)
    session.commit()
    response = client.get(f"/v2/comments/{deck1.entity_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["count"] == 3
    assert data["results"][0]["entity_id"] == comment1.entity_id
    assert data["results"][1]["entity_id"] == comment2.entity_id
    assert data["results"][1]["text"] is None
    assert data["results"][2]["entity_id"] == comment3.entity_id
    # And verify that admins can still see the text
    admin, token = create_admin_token(session)
    response = client.get(
        f"/v2/comments/{deck1.entity_id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["results"][1]["entity_id"] == comment2.entity_id
    assert data["results"][1]["text"] == "My second comment"


def test_create_comment(client: TestClient, session: db.Session, deck1, user1):
    """Verify creating comments works properly"""
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/comments/{deck1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My second comment"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    stmt = select(Comment).order_by(Comment.created.desc()).limit(1)
    comment = session.execute(stmt).scalar()
    assert comment.ordering_increment == 1


def test_create_comment_previous_comments(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify creating comments with a previous comment works properly"""
    # Add an initial comment to test ordering increment
    comment1 = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
    )
    session.add(comment1)
    session.commit()
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/comments/{deck1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My second comment"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    stmt = select(Comment).order_by(Comment.created.desc()).limit(1)
    comment2 = session.execute(stmt).scalar()
    assert comment2.ordering_increment == 2


def test_create_comment_card(client: TestClient, session: db.Session, user1):
    """Verify creating a comment for a card works"""
    stmt = select(Card).limit(1)
    card = session.execute(stmt).scalar()
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/comments/{card.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My second comment"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    stmt = select(Comment).order_by(Comment.created.desc()).limit(1)
    comment = session.execute(stmt).scalar()
    assert comment.source_version == card.version


def test_create_comment_bad_entity_id(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify trying to access a non-deck and non-card entity ID fails"""
    bad_entity_id = create_entity(session)
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/comments/{bad_entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My second comment"},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_create_comment_legacy_resource(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify comments cannot be added to legacy content"""
    deck1.is_legacy = True
    session.commit()
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/comments/{deck1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My second comment"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_comment_snapshot(
    client: TestClient, session: db.Session, snapshot1, user1
):
    """Verify comments cannot be added to snapshots"""
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/comments/{snapshot1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My second comment"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_comment_empty(client: TestClient, session: db.Session, deck1, user1):
    """Verify comments cannot be empty"""
    _, token = create_user_token(session, user=user1)
    response = client.post(
        f"/v2/comments/{deck1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "  "},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_edit_comment(client: TestClient, session: db.Session, deck1, user1):
    """Verify users can edit their comments"""
    comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
    )
    session.add(comment)
    session.commit()
    _, token = create_user_token(session, user=user1)
    response = client.patch(
        f"/v2/comment/{comment.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My first edited comment"},
    )
    assert response.status_code == status.HTTP_200_OK
    session.refresh(comment)
    assert comment.text == "My first edited comment"


def test_edit_comment_admin(client: TestClient, session: db.Session, deck1, user1):
    """Verify an admin can moderate a comment"""
    comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
    )
    session.add(comment)
    session.commit()
    _, token = create_admin_token(session)
    response = client.patch(
        f"/v2/comment/{comment.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My first edited comment", "moderation_notes": "EDIT"},
    )
    assert response.status_code == status.HTTP_200_OK
    session.refresh(comment)
    assert comment.text == "My first edited comment"
    assert comment.moderation_notes == "EDIT"
    assert comment.is_moderated is True


def test_edit_comment_bad_entity_id(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify that a bad ID for a comment throws a 404"""
    _, token = create_user_token(session, user=user1)
    response = client.patch(
        f"/v2/comment/{deck1.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My first edited comment"},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_edit_comment_deleted(client: TestClient, session: db.Session, deck1, user1):
    """Verify deleted comments cannot be edited"""
    comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
        is_deleted=True,
    )
    session.add(comment)
    session.commit()
    _, token = create_user_token(session, user=user1)
    response = client.patch(
        f"/v2/comment/{comment.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My first edited comment"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_edit_comment_empty(client: TestClient, session: db.Session, deck1, user1):
    """Verify comments cannot be edited to be whitespace only"""
    comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
    )
    session.add(comment)
    session.commit()
    _, token = create_user_token(session, user=user1)
    response = client.patch(
        f"/v2/comment/{comment.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "  "},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_edit_comment_other_user(client: TestClient, session: db.Session, deck1, user1):
    """Verify that another user cannot edit your comments"""
    comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
    )
    session.add(comment)
    session.commit()
    _, token = create_user_token(session)
    response = client.patch(
        f"/v2/comment/{comment.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My first edited comment"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_edit_comment_moderation_notes_required(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify that moderation notes are required when admins edit other user's comments"""
    comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
    )
    session.add(comment)
    session.commit()
    _, token = create_admin_token(session)
    response = client.patch(
        f"/v2/comment/{comment.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My first edited comment"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_edit_comment_moderated(client: TestClient, session: db.Session, deck1, user1):
    """Verify that a user cannot edit a moderated comment"""
    comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
        is_moderated=True,
    )
    session.add(comment)
    session.commit()
    _, token = create_user_token(session, user=user1)
    response = client.patch(
        f"/v2/comment/{comment.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "My first edited comment"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_delete_comment(client: TestClient, session: db.Session, deck1, user1):
    """Verify comments can be deleted"""
    comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
    )
    session.add(comment)
    session.commit()
    _, token = create_user_token(session, user=user1)
    response = client.delete(
        f"/v2/comment/{comment.entity_id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    session.refresh(comment)
    assert comment.is_deleted is True


def test_delete_comment_bad_entity_id(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify that a bad ID for a comment deletion throws a 404"""
    _, token = create_user_token(session, user=user1)
    response = client.delete(
        f"/v2/comment/{deck1.entity_id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_comment_deleted(client: TestClient, session: db.Session, deck1, user1):
    """Verify deleted comments simply return with a truthy response"""
    comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
        is_deleted=True,
    )
    session.add(comment)
    session.commit()
    _, token = create_user_token(session, user=user1)
    response = client.delete(
        f"/v2/comment/{comment.entity_id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    session.refresh(comment)
    assert comment.is_deleted is True


def test_delete_comment_other_user(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify that another user cannot delete your comments"""
    comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
    )
    session.add(comment)
    session.commit()
    _, token = create_user_token(session)
    response = client.delete(
        f"/v2/comment/{comment.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    session.refresh(comment)
    assert comment.is_deleted is False


def test_delete_comment_admin(client: TestClient, session: db.Session, deck1, user1):
    """Verify an admin can delete a comment"""
    comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
    )
    session.add(comment)
    session.commit()
    _, token = create_admin_token(session)
    response = client.delete(
        f"/v2/comment/{comment.entity_id}?moderation_notes=DELETE",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    session.refresh(comment)
    assert comment.moderation_notes == "DELETE"
    assert comment.is_moderated is True
    assert comment.is_deleted is True


def test_delete_comment_moderation_notes_required(
    client: TestClient, session: db.Session, deck1, user1
):
    """Verify that moderation notes are required when admins delete other user's comments"""
    comment = Comment(
        entity_id=create_entity(session),
        source_entity_id=deck1.entity_id,
        user_id=user1.id,
        source_type="deck",
        ordering_increment=1,
        text="My first comment",
    )
    session.add(comment)
    session.commit()
    _, token = create_admin_token(session)
    response = client.delete(
        f"/v2/comment/{comment.entity_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

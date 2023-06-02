from fastapi import APIRouter, Depends, Response, status

from api import db
from api.depends import AUTH_RESPONSES, get_session, login_required
from api.exceptions import APIException, NotFoundException
from api.models import Card, Comment, Deck, Subscription, User
from api.schemas import DetailResponse
from api.schemas.subscriptions import SubscriptionIn

router = APIRouter()


@router.post(
    "/subscription/{entity_id}",
    response_model=DetailResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Subscription failed.",
        },
        404: {
            "model": DetailResponse,
            "description": "Entity ID could not be found.",
        },
        **AUTH_RESPONSES,
    },
)
def create_subscription(
    entity_id: int,
    # Standard dependencies
    current_user: "User" = Depends(login_required),
    session: db.Session = Depends(get_session),
):
    """Subscribe to comments and updates for a deck or card."""
    # Make sure the entity ID can be subscribed to
    source = session.query(Card).filter(Card.entity_id == entity_id).first()
    is_deck = False
    if not source:
        source = session.query(Deck).filter(Deck.entity_id == entity_id).first()
        is_deck = True
    if source is None:
        raise NotFoundException(detail="No valid resource found to subscribe to.")
    if source.is_legacy:
        raise APIException(detail="Subscribing to legacy content is not allowed.")
    try:
        if source.is_snapshot:
            raise APIException(detail="You cannot subscribe to snapshots.")
    except AttributeError:
        # Cards don't have this attribute, so we can safely ignore it
        pass

    success_response = {"detail": "You have subscribed to this content."}
    # Check if they already have a subscription
    subscription = (
        session.query(Subscription)
        .filter(
            Subscription.source_entity_id == entity_id,
            Subscription.user_id == current_user.id,
        )
        .first()
    )
    if subscription:
        return success_response

    # Look up the most recently seen entity ID (assumes that they subscribed from the detail page, since it's silly to
    #  force them to immediately update the last seen ID after subscribing).
    last_seen_entity_id = (
        session.query(Comment.entity_id)
        .filter(Comment.source_entity_id == entity_id)
        .order_by(Comment.entity_id.desc())
        .scalar()
    )
    if not last_seen_entity_id and is_deck:
        # If we don't have any comments on this deck, grab the latest entity ID for the most recent published snapshot
        last_seen_entity_id = (
            session.query(Deck.entity_id)
            .filter(
                Deck.source_id == source.id,
                Deck.is_deleted == False,
                Deck.is_snapshot == True,
                Deck.is_public == True,
            )
            .order_by(Deck.entity_id.desc())
            .scalar()
        )

    # Create a new subscription
    session.add(
        Subscription(
            user_id=current_user.id,
            source_entity_id=entity_id,
            last_seen_entity_id=last_seen_entity_id,
        )
    )
    session.commit()
    return success_response


@router.delete(
    "/subscription/{entity_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Subscription deletion failed.",
        },
        404: {
            "model": DetailResponse,
            "description": "Entity ID could not be found.",
        },
        **AUTH_RESPONSES,
    },
)
def delete_subscription(
    entity_id: int,
    # Standard dependencies
    current_user: "User" = Depends(login_required),
    session: db.Session = Depends(get_session),
):
    """Delete a subscription to comments and updates for a deck or card."""
    session.query(Subscription).filter(
        Subscription.user_id == current_user.id,
        Subscription.source_entity_id == entity_id,
    ).delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch(
    "/subscription/{entity_id}",
    response_model=DetailResponse,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Subscription update failed.",
        },
        404: {
            "model": DetailResponse,
            "description": "No such subscription.",
        },
        **AUTH_RESPONSES,
    },
)
def update_subscription(
    entity_id: int,
    data: SubscriptionIn,
    # Standard dependencies
    current_user: "User" = Depends(login_required),
    session: db.Session = Depends(get_session),
):
    """Update a subscription with the last viewed entity ID.

    Card subscriptions should only use an entity ID for a comment attached to the card. Decks may use the entity ID of
    the latest viewed comment or the latest published deck snapshot.
    """
    # Grab the relevant subscription
    subscription = (
        session.query(Subscription)
        .filter(
            Subscription.user_id == current_user.id,
            Subscription.source_entity_id == entity_id,
        )
        .first()
    )
    if not subscription:
        raise NotFoundException(detail="You are not subscribed to this content.")
    # Validate the entity ID that was passed in
    last_seen = (
        session.query(Comment)
        .filter(
            Comment.source_entity_id == entity_id,
            Comment.entity_id == data.last_seen_entity_id,
        )
        .first()
    )
    if not last_seen:
        # This might be a deck snapshot, so check for that
        last_seen = (
            session.query(Deck)
            .filter(
                Deck.entity_id == data.last_seen_entity_id,
                Deck.is_snapshot == True,
                Deck.is_public == True,
                Deck.is_deleted == False,
            )
            .first()
        )
    if not last_seen:
        raise APIException(detail="Invalid entity ID passed for this subscription.")
    subscription.last_seen_entity_id = data.last_seen_entity_id
    session.commit()
    return {"detail": "Subscription updated!"}

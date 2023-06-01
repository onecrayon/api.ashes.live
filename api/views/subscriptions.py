from fastapi import APIRouter, Depends, status

from api import db
from api.depends import AUTH_RESPONSES, get_session, login_required
from api.exceptions import APIException, NotFoundException
from api.models import Card, Comment, Deck, Subscription, User
from api.schemas import DetailResponse

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

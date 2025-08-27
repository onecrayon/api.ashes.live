from collections import defaultdict
from datetime import datetime
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, Query, Request, Response, status
from pydantic import UUID4
from sqlalchemy import and_, delete, or_, select, update

from api import db
from api.depends import (
    AUTH_RESPONSES,
    anonymous_required,
    get_current_user,
    get_session,
    login_required,
    paging_options,
)
from api.environment import settings
from api.exceptions import APIException, NotFoundException, NoUserAccessException
from api.models import (
    AnonymousUser,
    Card,
    Deck,
    DeckCard,
    DeckDie,
    DeckSelectedCard,
    Release,
    Stream,
    Subscription,
    User,
    UserType,
)
from api.models.card import DiceFlags
from api.schemas import DetailResponse
from api.schemas.decks import (
    DeckDetails,
    DeckExportOut,
    DeckExportResults,
    DeckFilters,
    DeckFiltersMine,
    DeckFullOut,
    DeckImportOut,
    DeckIn,
    DeckListingOut,
    DeckSaveOut,
    SnapshotCreateOut,
    SnapshotEditIn,
    SnapshotIn,
)
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.services.deck import (
    BadPhoenixbornUnique,
    ConjurationInDeck,
    PhoenixbornInDeck,
    RedRainsConversionFailed,
    create_or_update_deck,
    create_snapshot_for_deck,
    deck_to_dict,
    generate_deck_dict,
    get_conjuration_mapping,
    get_decks_stmt,
    paginate_deck_listing,
)
from api.services.stream import create_entity
from api.utils.dates import pydantic_style_datetime_str

router = APIRouter()


@router.get(
    "/decks",
    response_model=DeckListingOut,
    response_model_exclude_unset=True,
)
def list_published_decks(
    request: Request,
    filters: DeckFilters = Depends(),
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    # Standard dependencies
    paging: PaginationOptions = Depends(paging_options),
    session: db.Session = Depends(get_session),
):
    """Get a paginated listing of published snapshots with optional filters.

    ## Available filters

    * `q`: deck title search
    * `phoenixborn`: list of Phoenixborn slugs
    * `card`: list of card slugs
    * `player`: list of player badges
    * `show_preconstructed` (default: false): if true, only include preconstructed decks
    * `show_legacy` (default: false): if true, legacy 1.0 decks will be returned
    * `show_red_rains` (default: false): if true, only Red Rains decks will be returned
    """
    # For now, keep using get_decks_query but need to handle the session parameter
    # This will be addressed when updating views/decks.py fully
    stmt = get_decks_stmt(
        show_legacy=filters.show_legacy,
        show_red_rains=filters.show_red_rains,
        is_public=True,
        order=order,
        q=filters.q,
        phoenixborn=filters.phoenixborn,
        cards=filters.card,
        players=filters.player,
        show_preconstructed=filters.show_preconstructed,
    )
    return paginate_deck_listing(stmt, session, request, paging)


@router.get(
    "/decks/mine",
    response_model=DeckListingOut,
    response_model_exclude_unset=True,
    responses=AUTH_RESPONSES,
)
def list_my_decks(
    request: Request,
    filters: DeckFiltersMine = Depends(),
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    paging: PaginationOptions = Depends(paging_options),
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Get a paginated listing of private decks for the current logged-in user.

    Please note that unlike the public-facing GET `/v2/decks` (which solely returns snapshots) this
    endpoint solely returns the base deck listings (no snapshots are included in the list at all).

    ## Available query parameter filters

    * `q`: deck title search
    * `phoenixborn`: list of Phoenixborn slugs
    * `card`: list of card slugs
    * `show_legacy` (default: false): if true, legacy 1.0 decks will be returned
    * `show_red_rains` (default: false): if true, only Red Rains decks will be returned
    """
    stmt = get_decks_stmt(
        show_legacy=filters.show_legacy,
        show_red_rains=filters.show_red_rains,
        is_public=False,
        order=order,
        q=filters.q,
        phoenixborn=filters.phoenixborn,
        cards=filters.card,
        players=[current_user.badge],
    )
    return paginate_deck_listing(stmt, session, request, paging)


@router.get(
    "/decks/shared/{direct_share_uuid}",
    response_model=DeckFullOut,
    responses={
        404: {
            "model": DetailResponse,
            "description": "Deck could not be found",
        },
    },
)
def get_private_deck(
    direct_share_uuid: UUID4,
    session: db.Session = Depends(get_session),
):
    """Fetch a single deck using its direct share UUID.

    This endpoint returns just a specific deck or snapshot based on its direct share UUID. This is
    primarily intended for loading a deck into an external application such as TableTop Simulator
    or Ashteki, but can also be used to privately share access to a deck with another user.
    """
    stmt = select(Deck).where(
        Deck.direct_share_uuid == direct_share_uuid, Deck.is_deleted.is_(False)
    )
    deck = session.execute(stmt).scalar_one_or_none()
    if not deck:
        raise NotFoundException(
            detail="No such deck; it might have been deleted, or your share ID might be wrong."
        )
    deck_dict = deck_to_dict(session, deck=deck, include_share_uuid=True)
    return deck_dict


@router.get(
    "/decks/{deck_id}",
    response_model=DeckDetails,
    response_model_exclude_unset=True,
    responses={
        404: {
            "model": DetailResponse,
            "description": "No public snapshot available for this source deck ID.",
        },
        **AUTH_RESPONSES,
    },
)
def get_deck(
    deck_id: int,
    show_saved: bool = Query(
        False,
        description="When viewing a source deck ID, whether the actual latest save should be returned.",
    ),
    session: db.Session = Depends(get_session),
    current_user: "UserType" = Depends(get_current_user),
):
    """Read a single deck's details.

    This endpoint will return different information depending on the requesting user. For decks the
    user did not create (and for anonymous users):

    * passing a source deck's ID will always return the most recent published snapshot
    * passing a published snapshot's ID will return that snapshot
    * passing a private snapshot's ID (or a deck ID without any public snapshots) will throw an
      authentication error

    For authenticated users who own the deck:

    * passing a source deck's ID will return the most recent published snapshot
    * passing a source deck's ID with the query parameter `show_saved=true` will return the most
      recent saved copy of that deck (allows previewing how a deck will display prior to creating
      a public snapshot)
    * passing any snapshot's ID will return that snapshot
    """
    source_deck: Deck = session.get(Deck, deck_id)
    if not source_deck:
        raise NotFoundException(detail="Deck not found.")
    own_deck = (
        not current_user.is_anonymous() and source_deck.user_id == current_user.id
    )
    if source_deck.is_deleted:
        raise NotFoundException(detail="Deck not found.")
    if (source_deck.is_snapshot and not source_deck.is_public and not own_deck) or (
        not own_deck and show_saved
    ):
        raise NoUserAccessException(detail="You do not have access to this deck.")
    # Check for the instances where we just return the source deck (separated into discrete
    #  conditionals to make things more readable)
    # Public snapshots simply get returned
    if source_deck.is_snapshot and source_deck.is_public:
        deck = source_deck
    # Private snapshots get returned if the user owns the deck
    elif source_deck.is_snapshot and own_deck:
        deck = source_deck
    # The actual deck gets returned if we are showing the latest saved copy
    elif not source_deck.is_snapshot and own_deck and show_saved:
        deck = source_deck
    # By default, re-route to the latest public snapshot
    else:
        stmt = (
            select(Deck)
            .where(
                Deck.source_id == source_deck.id,
                Deck.is_snapshot.is_(True),
                Deck.is_public.is_(True),
                Deck.is_deleted.is_(False),
            )
            .order_by(Deck.created.desc())
        )
        deck: Deck = session.execute(stmt).scalar_one_or_none()
        if not deck:
            raise NotFoundException(detail="Deck not found.")

    deck_dict = deck_to_dict(
        session,
        deck=deck,
        include_comment_entity_id=True,
        include_share_uuid=own_deck or deck.is_public,
    )

    # Add our `is_saved` flag, if we're viewing a saved deck
    if not source_deck.is_snapshot and show_saved:
        deck_dict["is_saved"] = True

    # Check to see if we can include the direct_share_uuid
    if deck.is_public or own_deck:
        deck_dict["direct_share_uuid"] = deck.direct_share_uuid

    # And finally look up the releases that are required by this deck
    card_stubs = set(x["stub"] for x in deck_dict["cards"])
    card_stubs.add(deck_dict["phoenixborn"]["stub"])
    release_stubs = set()
    # Even if cards don't require a particular set, check for dice
    dice_to_release = {
        "ceremonial": "master-set",
        "charm": "master-set",
        "illusion": "master-set",
        "natural": "master-set",
        "divine": "the-law-of-lions",
        "sympathy": "the-song-of-soaksend",
        "time": "the-breaker-of-fate",
    }
    for die in deck_dict["dice"]:
        release_stubs.add(dice_to_release[die["name"]])
    stmt = (
        select(Release, Deck)
        .outerjoin(Card, Card.release_id == Release.id)
        .outerjoin(Deck, Deck.preconstructed_release == Release.id)
        .where(
            db.or_(
                Release.stub.in_(release_stubs),
                Card.stub.in_(card_stubs),
            ),
            Release.is_legacy.is_(bool(deck_dict.get("is_legacy"))),
        )
        .order_by(Release.id.asc())
        .distinct(Release.id)
    )
    release_results = session.execute(stmt).all()
    release_data = []
    for result in release_results:
        release_data.append(
            {
                "name": result.Release.name,
                "stub": result.Release.stub,
                "is_legacy": result.Release.is_legacy,
                "preconstructed_deck_id": (
                    result.Deck.source_id
                    # Don't bother including the preconstructed ID if the viewed deck is the precon
                    if result.Deck and result.Deck.source_id != deck_dict["source_id"]
                    else None
                ),
            }
        )

    deck_details = {
        "releases": release_data,
        "deck": deck_dict,
    }
    if show_saved:
        source_id = (
            source_deck.id if not source_deck.is_snapshot else source_deck.source_id
        )
        stmt = select(Deck.id).where(
            Deck.source_id == source_id,
            Deck.is_snapshot.is_(True),
            Deck.is_public.is_(True),
            Deck.is_deleted.is_(False),
        )
        count = session.execute(
            select(db.func.count()).select_from(stmt.subquery())
        ).scalar()
        deck_details["has_published_snapshot"] = bool(count)

    # If the user is subscribed to this deck, note their last seen entity ID for this deck
    if not current_user.is_anonymous():
        if not deck.is_snapshot:
            deck_source_entity_id = deck.entity_id
        else:
            stmt = select(Deck.entity_id).where(Deck.id == deck.source_id)
            deck_source_entity_id = session.execute(stmt).scalar()
        stmt = select(Subscription).where(
            Subscription.user_id == current_user.id,
            Subscription.source_entity_id == deck_source_entity_id,
        )
        subscription = session.execute(stmt).scalar_one_or_none()
        if subscription:
            deck_details["last_seen_entity_id"] = subscription.last_seen_entity_id

    return deck_details


@router.put(
    "/decks",
    response_model=DeckSaveOut,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Deck creation failed.",
        },
        **AUTH_RESPONSES,
    },
)
def save_deck(
    data: DeckIn,
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Create or update a deck in place.

    **This is not a patch!** You must pass the entire deck object in the body every time, and it
    will only be treated as an update if there is an ID included.
    """
    # Verify that the user has access to this deck, if we're saving over an existing deck
    if data.id:
        stmt = select(
            Deck.user_id, Deck.is_legacy, Deck.is_snapshot, Deck.is_deleted
        ).where(Deck.id == data.id)
        deck_check = session.execute(stmt).first()
        if not deck_check or deck_check.user_id != current_user.id:
            raise NoUserAccessException(detail="You cannot save a deck you do not own.")
        if deck_check.is_legacy:
            raise APIException(detail="Legacy decks cannot be saved.")
        if deck_check.is_snapshot:
            raise APIException(detail="You cannot save over a snapshot.")
        if deck_check.is_deleted:
            raise APIException(detail="This deck has been deleted.")
    # Ensure we have a Phoenixborn stub
    phoenixborn_stub = (
        data.phoenixborn
        if isinstance(data.phoenixborn, str)
        else data.phoenixborn.get("stub")
    )
    stmt = select(Card.id, Card.name).where(
        Card.stub == phoenixborn_stub, Card.is_legacy.is_(False)
    )
    phoenixborn = session.execute(stmt).first()
    if not phoenixborn:
        raise APIException(detail="Valid Phoenixborn is required.")
    try:
        deck = create_or_update_deck(
            session,
            current_user,
            phoenixborn=phoenixborn,
            deck_id=data.id,
            title=data.title,
            description=data.description,
            dice=[x.model_dump() for x in data.dice] if data.dice else None,
            cards=[x.model_dump() for x in data.cards] if data.cards else None,
            first_five=data.first_five,
            effect_costs=data.effect_costs,
            tutor_map=data.tutor_map,
            is_red_rains=data.is_red_rains,
        )
    except PhoenixbornInDeck:
        raise APIException(
            detail="Your deck listing includes a Phoenixborn. Please pass the Phoenixborn at the root level of the deck object."
        )
    except ConjurationInDeck as e:
        raise APIException(
            detail=f"Your deck includes the conjuration {e.card_name}, but conjurations should not be included in the list of cards."
        )
    except BadPhoenixbornUnique as e:
        raise APIException(
            detail=f"Your deck includes {e.card_name}, but this card requires {e.required_phoenixborn}."
        )
    except RedRainsConversionFailed as e:
        raise APIException(
            detail="You cannot convert between Red Rains and PvP for decks with a public snapshot."
        )
    return deck_to_dict(session, deck=deck)


@router.post(
    "/decks/{deck_id}/snapshot",
    response_model=SnapshotCreateOut,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Snapshot creation failed.",
        },
        **AUTH_RESPONSES,
    },
)
def create_snapshot(
    deck_id: int,
    data: SnapshotIn = None,
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Create a snapshot of the currently-saved version of the deck.

    **Please note:** you must save the deck prior to calling this endpoint! This endpoint will create a snapshot from
    the most recent saved copy of the deck (although it does allow you to set a custom title and description).
    """
    stmt = (
        select(Deck)
        .options(
            db.joinedload(Deck.cards),
            db.joinedload(Deck.dice),
            db.joinedload(Deck.selected_cards),
        )
        .where(Deck.id == deck_id)
    )
    deck: Deck = session.execute(stmt).unique().scalar_one_or_none()
    if not deck or deck.user_id != current_user.id:
        raise NoUserAccessException(
            detail="You cannot save a snapshot of a deck you do not own."
        )
    if deck.is_legacy:
        raise APIException(detail="You cannot save snapshots for legacy decks.")
    if deck.is_snapshot:
        raise APIException(detail="You cannot create a snapshot of another snapshot.")
    if deck.is_deleted:
        raise APIException(
            detail="This deck has been deleted and can no longer be updated."
        )
    if not data:
        data = SnapshotIn()
    # Ensure that public snapshots are legal decks
    if data.is_public:
        total_cards = 0
        total_dice = 0
        for deck_card in deck.cards:
            total_cards += deck_card.count
        for deck_die in deck.dice:
            total_dice += deck_die.count
        if total_cards != 30 or total_dice != 10:
            raise APIException(
                detail="You must have exactly 30 cards and 10 dice in your deck to publish it."
            )
    # If setting a preconstructed release, ensure that we have permissions and a valid release
    preconstructed_release_id = None
    if data.preconstructed_release:
        if not current_user.is_admin:
            raise NoUserAccessException(
                detail="Only site admins may publish preconstructed decks."
            )
        if not data.is_public:
            raise APIException(
                detail="Only public decks may be associated with a preconstructed deck."
            )
        stmt = (
            select(Release.id)
            .outerjoin(Deck, Deck.preconstructed_release == Release.id)
            .where(
                Release.stub == data.preconstructed_release,
                Release.is_legacy.is_(False),
                Release.is_public.is_(True),
                Deck.id.is_(None),
            )
        )
        preconstructed_release_id = session.execute(stmt).scalar()
        if not preconstructed_release_id:
            raise APIException(
                detail="No such release, or release already has a preconstructed deck."
            )
    # TODO: Ensure that there is at least one thing changed from the most recent snapshot?
    title = data.title if data.title else deck.title
    description = deck.description
    if data.description:
        description = data.description
    elif data.description is not None:
        # Falsey descriptions that aren't None mean they intentionally want a blank description
        description = None
    snapshot = create_snapshot_for_deck(
        session,
        current_user,
        deck,
        title=title,
        description=description,
        is_public=data.is_public,
        preconstructed_release_id=preconstructed_release_id,
        include_first_five=data.include_first_five,
    )
    return {"detail": "Snapshot successfully created!", "snapshot_id": snapshot.id}


@router.get(
    "/decks/{deck_id}/snapshots",
    response_model=DeckListingOut,
    response_model_exclude_unset=True,
    responses={
        404: {
            "model": DetailResponse,
            "description": "No such source deck found.",
        },
    },
)
def list_snapshots(
    request: Request,
    deck_id: int,
    show_public_only: bool = Query(
        False,
        description="Only affects output if the current user is the owner of the deck (private snapshots will only be included for owners).",
    ),
    order: PaginationOrderOptions = PaginationOrderOptions.desc,
    paging: PaginationOptions = Depends(paging_options),
    session: db.Session = Depends(get_session),
    current_user: "UserType" = Depends(get_current_user),
):
    """List snapshots saved for a given deck.

    The `show_public_only` query parameter only does anything if the current user is the owner of the deck (users who
    do not own decks can only ever see public snapshots, so no private snapshots will be included even if they ask
    for them).
    """
    source_deck: Deck = session.get(Deck, deck_id)
    if not source_deck or source_deck.is_deleted or source_deck.is_snapshot:
        raise NotFoundException(detail="Deck not found.")
    stmt = select(Deck).where(
        Deck.is_deleted.is_(False),
        Deck.is_snapshot.is_(True),
        Deck.source_id == source_deck.id,
    )
    if (
        current_user.is_anonymous()
        or current_user.id != source_deck.user_id
        or show_public_only is True
    ):
        stmt = stmt.where(Deck.is_public.is_(True))
    stmt = stmt.options(db.joinedload(Deck.user)).order_by(
        getattr(Deck.created, order)()
    )
    return paginate_deck_listing(
        stmt,
        session,
        request,
        paging,
        include_share_uuids=not current_user.is_anonymous()
        and current_user.id == source_deck.user_id,
    )


@router.delete(
    "/decks/{deck_id}", status_code=status.HTTP_204_NO_CONTENT, responses=AUTH_RESPONSES
)
def delete_deck(
    deck_id: int,
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Delete a deck.

    When requested for a source deck:

    * If there are no snapshots, the deck is truly deleted (unrecoverable). Intended use-case
      is for decks that get auto-saved, but not completed.
    * For decks with snapshots, it's a soft deletion that can potentially be recovered from (no
      user-facing support for recovering deleted decks currently planned, though). Deleted decks
      and their snapshots will be removed from all listings (including the stream).

    When requested for a snapshot, it's a soft deletion and the snapshot will no longer show up
    in any listings (including the stream).
    """
    stmt = select(Deck).options(db.joinedload(Deck.source)).where(Deck.id == deck_id)
    deck: Deck = session.execute(stmt).unique().scalar_one_or_none()
    if not deck or deck.user_id != current_user.id:
        raise NoUserAccessException(detail="You cannot delete a deck you do not own.")
    if deck.is_legacy:
        raise APIException(detail="You cannot delete legacy decks.")
    success_response = Response(status_code=status.HTTP_204_NO_CONTENT)
    # If the deck was previously deleted, just claim success and call it good
    if deck.is_deleted:
        return success_response
    # Check if we have any snapshots for source decks, and just delete that sucker for real if not
    if (
        not deck.is_snapshot
        and session.execute(
            select(db.func.count()).select_from(
                select(Deck).where(Deck.source_id == deck.id).subquery()
            )
        ).scalar()
        == 0
    ):
        delete_stmt = delete(DeckCard).where(DeckCard.deck_id == deck.id)
        session.execute(delete_stmt)
        delete_stmt = delete(DeckDie).where(DeckDie.deck_id == deck_id)
        session.execute(delete_stmt)
        delete_stmt = delete(DeckSelectedCard).where(
            DeckSelectedCard.deck_id == deck_id
        )
        session.execute(delete_stmt)
        delete_stmt = delete(Deck).where(Deck.id == deck_id)
        session.execute(delete_stmt)
        session.commit()
        return success_response

    # Otherwise, we're looking at a snapshot or a source deck that has snapshots
    deck.is_deleted = True
    # For snapshots, we need to remove only the Stream entries for that snapshot (leave the rest
    #  of the source deck's snapshots alone).
    if deck.is_snapshot and deck.is_public:
        # Check to see if we have a Stream entry that needs updating
        stmt = select(Stream).where(
            Stream.source_entity_id == deck.source.entity_id,
            Stream.entity_type == "deck",
            Stream.entity_id == deck.entity_id,
        )
        stream_entry: Stream = session.execute(stmt).scalar_one_or_none()
        if stream_entry:
            # We have a stream entry pointed to this snapshot, so check if we have an older snapshot
            #  that we can swap in
            stmt = (
                select(Deck)
                .where(
                    Deck.source_id == deck.source_id,
                    Deck.created < deck.created,
                    Deck.is_deleted.is_(False),
                )
                .order_by(Deck.created.desc())
            )
            previous_snapshot: Deck = session.execute(stmt).scalar_one_or_none()
            if previous_snapshot:
                stream_entry.entity_id = previous_snapshot.entity_id
                stream_entry.posted = previous_snapshot.created
            else:
                # Otherwise, just delete the stream entry because this deck no longer has any public
                #  snapshots
                session.delete(stream_entry)
    elif not deck.is_snapshot:
        # If we're not deleting a snapshot, then we need to completely clear out the Stream entry
        delete_stmt = delete(Stream).where(
            Stream.source_entity_id == deck.entity_id, Stream.entity_type == "deck"
        )
        session.execute(delete_stmt)
        # And mark all snapshots as deleted
        update_stmt = (
            update(Deck)
            .where(
                Deck.source_id == deck.id,
                Deck.is_snapshot.is_(True),
                Deck.is_deleted.is_(False),
            )
            .values(is_deleted=True)
        )
        session.execute(update_stmt)
    # Commit any pending changes, and return success
    session.commit()
    return success_response


@router.get(
    "/decks/{deck_id}/clone",
    response_model=DeckSaveOut,
    responses={
        404: {"model": DetailResponse, "description": "Invalid deck ID."},
        **AUTH_RESPONSES,
    },
)
def clone_deck(
    deck_id: int,
    direct_share_uuid: UUID4 = Query(
        None,
        description="Optional direct share UUID, if cloning a privately shared deck.",
    ),
    red_rains: bool = Query(
        False,
        description="Optional boolean to mark the cloned copy of the deck as a Red Rains deck.",
    ),
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Clone a snapshot, deck, or private share.

    Allows users to create a new deck that is an exact copy of:

    * one of their own decks
    * a public snapshot of someone else's deck
    * a privately shared deck or snapshot

    Returns a copy of the deck suitable for editing.

    Note that unlike the legacy site, cloning a deck in v2 will automatically create an initial snapshot of the source
    deck. This allows viewing the source deck even if it is deleted, overwritten, or otherwise inaccessible.
    """
    # Simple check if the target exists first (no need for joins)
    snapshot_or_deck_filters = [
        db.and_(
            Deck.is_public.is_(True),
            Deck.is_snapshot.is_(True),
        ),
        Deck.user_id == current_user.id,
    ]
    if direct_share_uuid:
        snapshot_or_deck_filters.append(
            Deck.direct_share_uuid == direct_share_uuid,
        )
    valid_deck_filters = (
        db.or_(*snapshot_or_deck_filters),
        Deck.id == deck_id,
        Deck.is_legacy.is_(False),
        Deck.is_deleted.is_(False),
    )
    stmt = select(Deck.id).where(*valid_deck_filters)
    deck = session.execute(stmt).first()
    if not deck:
        raise NotFoundException(detail="Invalid ID for cloning.")
    # Then we grab a new entity_id first because it causes a commit and kills the process otherwise
    entity_id = create_entity(session)
    # Then we can finally grab our full deck and copy it
    stmt = (
        select(Deck)
        .options(
            db.joinedload(Deck.cards),
            db.joinedload(Deck.dice),
            db.joinedload(Deck.selected_cards),
        )
        .where(*valid_deck_filters)
    )
    deck = session.execute(stmt).unique().scalar_one_or_none()
    # Create a clone of our deck object (transient cloning was too error-prone, so we're doing everything by hand)
    cloned_deck = Deck(
        entity_id=entity_id,
        title=f"Copy of {deck.title}",
        description=deck.description,
        # Only track source IDs if we own the source or it's a public snapshot
        source_id=(
            deck.id
            if current_user.id == deck.user_id or (deck.is_snapshot and deck.is_public)
            else None
        ),
        user_id=current_user.id,
        phoenixborn_id=deck.phoenixborn_id,
        is_red_rains=red_rains,
    )
    session.add(cloned_deck)
    session.commit()
    for die in deck.dice:
        session.add(
            DeckDie(deck_id=cloned_deck.id, die_flag=die.die_flag, count=die.count)
        )
    for card in deck.cards:
        session.add(
            DeckCard(deck_id=cloned_deck.id, card_id=card.card_id, count=card.count)
        )
    for card in deck.selected_cards:
        session.add(
            DeckSelectedCard(
                deck_id=cloned_deck.id,
                card_id=card.card_id,
                tutor_card_id=card.tutor_card_id,
                is_first_five=card.is_first_five,
                is_paid_effect=card.is_paid_effect,
            )
        )
    session.commit()
    # Finally create an initial snapshot for the deck so we can see its original state even if the source changes
    create_snapshot_for_deck(
        session,
        current_user,
        cloned_deck,
        title=f"Source: {deck.title}",
        is_public=False,
        include_first_five=True,
    )
    return deck_to_dict(session, deck=cloned_deck)


@router.patch(
    "/decks/snapshots/{snapshot_id}",
    response_model=DeckSaveOut,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Snapshot editing failed.",
        },
        **AUTH_RESPONSES,
    },
)
def edit_snapshot(
    snapshot_id: int,
    data: SnapshotEditIn,
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Edit a snapshot's title or description

    Users can use this to update the descriptions of snapshots that have already been published. Admins can use this
    endpoint to moderate any snapshot that has been published on the site (as long as they include moderation notes).

    Title and description can be intentionally cleared by passing in an empty string for one or the other.
    """
    # First look up the snapshot
    deck: Deck = session.get(Deck, snapshot_id)
    # Run basic validation to make sure they have access to this snapshot (and it is indeed a snapshot)
    if not deck:
        raise NotFoundException(detail="No such snapshot found.")
    if not current_user.is_admin and deck.user_id != current_user.id:
        raise NoUserAccessException(detail="You cannot edit a snapshot you do not own.")
    if not deck.is_snapshot:
        raise APIException(detail="Not a valid snapshot.")
    # Ensure admins pass in moderation notes
    if current_user.is_admin:
        if deck.user_id != current_user.id:
            if not data.moderation_notes:
                raise APIException(detail="Moderation notes are required.")
            deck.moderation_notes = data.moderation_notes
            deck.is_moderated = True
            if data.description is not None and data.description != deck.description:
                deck.original_description = deck.description
    elif data.moderation_notes is not None:
        raise APIException(detail="You do not have permission to moderate snapshots.")
    # Now that we've verified everything is kosher, update our object
    for field in ("title", "description"):
        value = getattr(data, field)
        if value:
            setattr(deck, field, value)
        elif value is not None:
            # If the value is falsey (empty string) but not none, that means they intentionally want it cleared
            setattr(deck, field, None)
    session.commit()
    return deck_to_dict(session, deck=deck)


class DeckImportException(Exception):
    """Used internally to record exceptions when trying to import decks"""

    pass


@router.get(
    "/decks/import/{export_token}",
    response_model=DeckImportOut,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Error fetching decks to import from source.",
        },
        **AUTH_RESPONSES,
    },
)
def import_decks(
    export_token: UUID4,
    from_date: datetime | None = None,
    deck_share_uuid: Annotated[
        UUID4 | None,
        Query(
            description="If specified, only this deck and its snapshots will be imported."
        ),
    ] = None,
    from_api: str = "api.ashes.live",
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Imports decks from another instance of the Ashes.live backend.

    Mainly intended to be called on the Plaid Hat AshesDB in order to import decks from Ashes.live.
    """
    if not from_api.startswith("http"):
        from_api = f"https://{from_api}"
    if from_api.endswith("/"):
        from_api = from_api[:-1]
    params = {}
    if from_date:
        params["from_date"] = from_date.isoformat()
    if deck_share_uuid:
        params["deck_share_uuid"] = str(deck_share_uuid)
    if not params:
        params = None
    try:
        response = httpx.get(
            f"{from_api}/v2/decks/export/{export_token}", params=params
        )
        response.raise_for_status()
        exported_decks = response.json()
    except httpx.HTTPStatusError as e:
        raise APIException(
            detail=f"Source API responded with error: {e.response.json()['detail']}"
        )
    except httpx.RequestError as e:
        raise APIException(detail=f"Unable to connect to source API at {e.request.url}")

    # Time to import those decks! This is complicated for a few reasons:
    #  1. We're using created date + user as the primary key, because auto-incremented integers will differ
    #  2. We need to catch unusual errors such as cards existing in the external instance but not in ours
    #  3. We need to perform as few SQL calls wherever possible, because we're working in large batches
    #  4. Decks could be new or updated
    #
    #  All of these combined mean that we can't easily use the existing utility method for saving decks.

    # Before we do anything else, we need to gather the cards and past decks that are necessary for bulk operations
    card_stubs = set()
    created_dates = set()
    rendered_decks: list[DeckExportOut] = []
    for export_dict in exported_decks["decks"]:
        rendered = DeckExportOut(**export_dict)
        for card in rendered.cards:
            card_stubs.add(card.stub)
        card_stubs.add(rendered.phoenixborn.stub)
        created_dates.add(rendered.created)
        rendered_decks.append(rendered)
    stmt = (
        select(Card.stub, Card.id)
        .join(Card.release)
        .where(
            Card.stub.in_(card_stubs),
            Card.is_legacy == False,
            Release.is_public == True,
        )
    )
    card_stub_to_id: dict[str, int] = {x[0]: x[1] for x in session.execute(stmt).all()}
    stmt = (
        select(Deck)
        .options(
            db.joinedload(Deck.cards),
            db.joinedload(Deck.dice),
            db.joinedload(Deck.selected_cards),
        )
        .where(Deck.created.in_(created_dates), Deck.user_id == current_user.id)
    )
    created_to_deck: dict[datetime, Deck] = {
        x.created: x for x in session.execute(stmt).scalars().unique().all()
    }
    successfully_imported_created_dates = set()
    errors = []
    source_created_to_deck = defaultdict(list)
    for export_deck in rendered_decks:
        try:
            phoenixborn_id = card_stub_to_id.get(export_deck.phoenixborn.stub)
            if not phoenixborn_id:
                raise DeckImportException(
                    f"Deck '{export_deck.title}' failed to import; missing Phoenixborn {export_deck.phoenixborn.name}."
                )
            # Check if this is an update
            deck = created_to_deck.get(export_deck.created)
            if deck is not None:
                deck.title = export_deck.title
                deck.description = export_deck.description
                deck.phoenixborn_id = phoenixborn_id
                deck.modified = export_deck.modified
                # Intentionally ignoring the Red Rains conversion logic, because life is too short
            else:
                deck = Deck(
                    entity_id=create_entity(session),
                    title=export_deck.title,
                    description=export_deck.description,
                    created=export_deck.created,
                    modified=export_deck.modified,
                    user_id=current_user.id,
                    phoenixborn_id=phoenixborn_id,
                    is_snapshot=export_deck.is_snapshot,
                    is_public=export_deck.is_public,
                    is_red_rains=export_deck.is_red_rains,
                )

            # Save the created date if this has a source set (we have to set these later once everything in this batch
            #  is created or updated, because before then some of them might not have IDs)
            if export_deck.source_created:
                source_created_to_deck[export_deck.source_created].append(deck)

            # Update the dice listing
            deck_dice: list[DeckDie] = []
            total_dice = 0
            for die in export_deck.dice:
                die_name = die.name
                count = die.count
                if count:
                    if total_dice + count > 10:
                        count = 10 - total_dice
                    if count == 0:
                        break
                    total_dice = total_dice + count
                    deck_dice.append(
                        DeckDie(die_flag=DiceFlags[die_name].value, count=count)
                    )
            deck.dice = deck_dice

            # And then the card listing
            deck_cards: list[DeckCard] = []
            for card in export_deck.cards:
                card_id = card_stub_to_id.get(card.stub)
                if card_id is None:
                    raise DeckImportException(
                        f"Deck '{export_deck.title}' failed to import; missing card {card.name}."
                    )
                deck_cards.append(DeckCard(card_id=card_id, count=card.count))
            deck.cards = deck_cards

            # Save everything up!
            deck.selected_cards = []
            session.add(deck)
            # Unfortunately, this means we have 1-2 writes for every deck we import; however, I can't think of a way
            #  around this, because we're relying on the ORM relationship logic to properly manage cards (and
            #  particularly the selected cards) which isn't really possible with any SQLAlchemy bulk methods.
            session.commit()
            successfully_imported_created_dates.add(deck.created)
            # No need to proceed if there is no first five, effect costs, and/or tutor map
            if (
                not export_deck.first_five
                and not export_deck.effect_costs
                and not export_deck.tutor_map
            ):
                continue

            # Finally set selected cards
            selected_cards: list[DeckSelectedCard] = []
            if export_deck.effect_costs:
                for card_stub in export_deck.effect_costs:
                    card_id = card_stub_to_id.get(card_stub)
                    # pytest-cov simply can't handle catching this usage, so we have to skip it
                    if not card_id:  # pragma: no cover
                        continue
                    if (
                        export_deck.first_five
                        and card_stub not in export_deck.first_five
                    ):
                        selected_cards.append(
                            DeckSelectedCard(card_id=card_id, is_paid_effect=True)
                        )
            if export_deck.first_five:
                for card_stub in export_deck.first_five:
                    card_id = card_stub_to_id.get(card_stub)
                    if not card_id:  # pragma: no cover
                        continue
                    selected_cards.append(
                        DeckSelectedCard(
                            card_id=card_id,
                            is_first_five=True,
                            is_paid_effect=(
                                card_stub in export_deck.effect_costs
                                if export_deck.effect_costs
                                else False
                            ),
                        )
                    )
            if export_deck.tutor_map:
                for tutor_stub, card_stub in export_deck.tutor_map.items():
                    tutor_card_id = card_stub_to_id.get(tutor_stub)
                    card_id = card_stub_to_id.get(card_stub)
                    if not tutor_card_id or not card_id:  # pragma: no cover
                        continue
                    selected_cards.append(
                        DeckSelectedCard(card_id=card_id, tutor_card_id=tutor_card_id)
                    )
            deck.selected_cards = selected_cards
            session.commit()
        except DeckImportException as e:
            errors.append(str(e))

    # Now that we have imported everything, it's time to see if we can map source IDs
    stmt = select(Deck.created, Deck.id).where(
        Deck.created.in_(source_created_to_deck.keys()),
        Deck.user_id == current_user.id,
    )
    for row in session.execute(stmt).all():
        source_created = row[0]
        source_id = row[1]
        snapshot_decks = source_created_to_deck[source_created]
        for deck in snapshot_decks:
            deck.source_id = source_id
    session.commit()

    # Final step is to notify the source API which decks we imported successfully
    total_successes = len(successfully_imported_created_dates)
    if total_successes:
        try:
            response = httpx.post(
                f"{from_api}/v2/decks/export/{export_token}",
                json=[
                    pydantic_style_datetime_str(dt)
                    for dt in successfully_imported_created_dates
                ],
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise APIException(
                detail=f"Source API responded with error: {e.response.json()['detail']}"
            )
        except httpx.RequestError as e:
            raise APIException(
                detail=f"Unable to connect to source API at {e.request.url}"
            )

    # And at long last, we can return!
    return {
        "success_count": total_successes,
        "total_count": exported_decks["total"],
        "next_page_from_date": exported_decks["next_page_from_date"],
        "errors": errors,
    }


@router.get(
    "/decks/export/{export_token}",
    response_model=DeckExportResults,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Error when trying to generate list of decks for export.",
        },
        **AUTH_RESPONSES,
    },
)
def export_decks(
    export_token: UUID4,
    from_date: datetime | None = None,
    deck_share_uuid: Annotated[
        UUID4 | None,
        Query(
            description="If specified, only this deck and its snapshots will be exported."
        ),
    ] = None,
    session: db.Session = Depends(get_session),
    _: "AnonymousUser" = Depends(anonymous_required),
):
    """Exports user decks.

    Intended to be called from another instance via its `/decks/import/{export_token}` endpoint.
    """
    if not settings.allow_exports:
        raise APIException(detail="Deck exports are not allowed from this site.")
    stmt = select(User).where(User.deck_export_uuid == export_token)
    deck_user = session.execute(stmt).scalar_one_or_none()
    if not deck_user:
        raise NotFoundException(detail="No user matching export token.")

    # If we are exporting a "single" deck, then gather the source deck and all of its snapshots
    initial_deck = None
    if deck_share_uuid:
        stmt = select(Deck).where(
            Deck.direct_share_uuid == deck_share_uuid,
            Deck.user_id == deck_user.id,
            Deck.is_deleted == False,
            Deck.is_legacy == False,
        )
        initial_deck = session.execute(stmt).scalar_one_or_none()
        if not initial_deck:
            raise NotFoundException(
                detail="Current user does not have a deck with this share UUID."
            )
        if initial_deck.is_snapshot:
            stmt = select(Deck).where(Deck.id == initial_deck.source_id)
            initial_deck = session.execute(stmt).scalar_one_or_none()

    deck_filters = [
        Deck.user_id == deck_user.id,
        Deck.is_exported == False,
        Deck.is_deleted == False,
        Deck.is_legacy == False,
    ]
    if initial_deck:
        deck_filters.append(
            or_(
                Deck.id == initial_deck.id,
                and_(Deck.source_id == initial_deck.id, Deck.is_snapshot == True),
            )
        )
    if from_date:
        deck_filters.append(Deck.created > from_date)
    stmt = select(Deck).where(*deck_filters).order_by(Deck.created.asc())
    total_to_export = session.execute(
        select(db.func.count()).select_from(stmt.subquery())
    ).scalar()
    # Find our next set of decks to export. We limit by 1 more than our max so we can determine if there is a next page
    decks_to_export = (
        session.execute(stmt.limit(settings.exports_per_request + 1)).scalars().all()
    )
    # Check if we have a next page, and discard the extra, if so
    have_next_page = len(decks_to_export) == settings.exports_per_request + 1
    if have_next_page:
        decks_to_export.pop()

    # Parse through the decks so that we can load their cards en masse with a single query; this is largely lifted
    #  straight from the deck services pagination logic, but we need to look up source created dates so I'mma copy/paste
    deck_ids = set()
    source_ids = set()
    needed_cards = set()
    for deck_row in decks_to_export:
        deck_ids.add(deck_row.id)
        if deck_row.source_id:
            source_ids.add(deck_row.source_id)
        # Ensure we lookup our Phoenixborn cards
        needed_cards.add(deck_row.phoenixborn_id)
    # Fetch and collate our dice information for all decks
    deckdie_stmt = select(DeckDie).where(DeckDie.deck_id.in_(deck_ids))
    deck_dice = session.execute(deckdie_stmt).scalars().all()
    deck_id_to_dice = defaultdict(list)
    for deck_die in deck_dice:
        deck_id_to_dice[deck_die.deck_id].append(deck_die)
    # Now that we have all our basic deck information, look up the cards and quantities they include
    deckcard_stmt = select(DeckCard).where(DeckCard.deck_id.in_(deck_ids))
    deck_cards = session.execute(deckcard_stmt).scalars().all()
    deck_id_to_deck_cards = defaultdict(list)
    for deck_card in deck_cards:
        needed_cards.add(deck_card.card_id)
        deck_id_to_deck_cards[deck_card.deck_id].append(deck_card)
    # And finally we need to fetch all top-level conjurations
    card_id_to_conjurations = get_conjuration_mapping(
        session=session, card_ids=needed_cards
    )
    # Now that we have root-level conjurations, we can gather all our cards and setup our decks
    card_stmt = select(Card).where(Card.id.in_(needed_cards))
    cards = session.execute(card_stmt).scalars().all()
    card_id_to_card = {x.id: x for x in cards}
    # Gather our selected cards for these decks
    deckselected_stmt = select(DeckSelectedCard).where(
        DeckSelectedCard.deck_id.in_(deck_ids)
    )
    deck_selected_cards = session.execute(deckselected_stmt).scalars().all()
    deck_id_to_selected_cards = defaultdict(list)
    for deck_selected_card in deck_selected_cards:
        deck_id_to_selected_cards[deck_selected_card.deck_id].append(deck_selected_card)
    # Gather all source IDs *that belong to this user* and stick them in a mapping
    source_stmt = select(Deck.id, Deck.created).where(
        Deck.id.in_(source_ids),
        Deck.is_deleted == False,
    )
    source_decks = session.execute(source_stmt).all()
    source_id_to_created = {x[0]: x[1] for x in source_decks}
    # And finally generate a dict for our deck export
    deck_output = []
    for deck in decks_to_export:
        deck_dict = generate_deck_dict(
            deck=deck,
            card_id_to_card=card_id_to_card,
            card_id_to_conjurations=card_id_to_conjurations,
            deck_cards=deck_id_to_deck_cards[deck.id],
            deck_dice=deck_id_to_dice.get(deck.id),
            include_share_uuid=False,
        )
        deck_dict["description"] = deck.description
        if deck_row.source_id and deck_row.source_id in source_id_to_created:
            deck_dict["source_created"] = source_id_to_created[deck_row.source_id]
        selected_cards = deck_id_to_selected_cards.get(deck.id, [])
        first_five = []
        effect_costs = []
        tutor_map = {}
        for selected_card in selected_cards:
            card = card_id_to_card.get(selected_card.card_id)
            # This situation should theoretically never happen, but just in case...
            if not card:  # pragma: no cover
                continue
            if selected_card.is_first_five:
                first_five.append(card.stub)
            if selected_card.is_paid_effect:
                effect_costs.append(card.stub)
            if selected_card.tutor_card_id:
                tutor_card = card_id_to_card.get(selected_card.tutor_card_id)
                if tutor_card:
                    tutor_map[tutor_card.stub] = card.stub
        deck_dict["first_five"] = first_five
        deck_dict["effect_costs"] = effect_costs
        deck_dict["tutor_map"] = tutor_map
        deck_output.append(deck_dict)
    return {
        "next_page_from_date": decks_to_export[-1].created if have_next_page else None,
        "total": total_to_export,
        "decks": deck_output,
    }


@router.post(
    "/decks/export/{export_token}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        400: {
            "model": DetailResponse,
            "description": "Error when trying to mark decks as exported.",
        },
        404: {
            "model": DetailResponse,
            "description": "No user matching the export token.",
        },
        **AUTH_RESPONSES,
    },
)
def finalize_exported_decks(
    export_token: UUID4,
    deck_create_dates: list[datetime],
    session: db.Session = Depends(get_session),
    _: "AnonymousUser" = Depends(anonymous_required),
):
    """Final step for importing decks is to call this endpoint and tell it which decks have been successfully
    imported.

    Accepts a list of deck created dates that were successfully imported.
    """
    if not settings.allow_exports:
        raise APIException(detail="Deck exports are not allowed from this site.")
    stmt = select(User).where(User.deck_export_uuid == export_token)
    deck_user = session.execute(stmt).scalar_one_or_none()
    if not deck_user:
        raise NotFoundException(detail="No user matching export token.")
    if len(deck_create_dates) == 0:
        raise APIException(
            detail="You must pass one or more created dates for decks that were successfully imported."
        )
    if len(deck_create_dates) > settings.exports_per_request:
        raise APIException(
            detail=f"You cannot mark more than {settings.exports_per_request} decks as successfully imported at once."
        )

    update_stmt = (
        update(Deck)
        .where(Deck.user_id == deck_user.id, Deck.created.in_(deck_create_dates))
        .values(is_exported=True)
    )
    session.execute(update_stmt)

from fastapi import APIRouter, Depends, Query, Request, Response, status
from pydantic import UUID4

from api import db
from api.depends import (
    AUTH_RESPONSES,
    get_current_user,
    get_session,
    login_required,
    paging_options,
)
from api.exceptions import APIException, NotFoundException, NoUserAccessException
from api.models import (
    Card,
    Deck,
    DeckCard,
    DeckDie,
    DeckSelectedCard,
    Release,
    Stream,
    User,
    UserType,
)
from api.schemas import DetailResponse
from api.schemas.decks import (
    DeckDetails,
    DeckFilters,
    DeckFiltersMine,
    DeckFullOut,
    DeckIn,
    DeckListingOut,
    DeckSaveOut,
    SnapshotEditIn,
    SnapshotIn,
)
from api.schemas.pagination import PaginationOptions, PaginationOrderOptions
from api.services.deck import (
    BadPhoenixbornUnique,
    ConjurationInDeck,
    PhoenixbornInDeck,
    create_or_update_deck,
    create_snapshot_for_deck,
    deck_to_dict,
    get_decks_query,
    paginate_deck_listing,
)

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
    """
    query = get_decks_query(
        session,
        show_legacy=filters.show_legacy,
        is_public=True,
        order=order,
        q=filters.q,
        phoenixborn=filters.phoenixborn,
        cards=filters.card,
        players=filters.player,
        show_preconstructed=filters.show_preconstructed,
    )
    return paginate_deck_listing(query, session, request, paging)


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
    """
    query = get_decks_query(
        session,
        show_legacy=filters.show_legacy,
        is_public=False,
        order=order,
        q=filters.q,
        phoenixborn=filters.phoenixborn,
        cards=filters.card,
        players=[current_user.badge],
    )
    return paginate_deck_listing(query, session, request, paging)


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
    deck = (
        session.query(Deck)
        .filter(Deck.direct_share_uuid == direct_share_uuid, Deck.is_deleted.is_(False))
        .first()
    )
    if not deck:
        raise NotFoundException(
            detail="No such deck; it might have been deleted, or your share ID might be wrong."
        )
    deck_dict = deck_to_dict(session, deck=deck)
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
    source_deck: Deck = session.query(Deck).get(deck_id)
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
        deck: Deck = (
            session.query(Deck)
            .filter(
                Deck.source_id == source_deck.id,
                Deck.is_snapshot.is_(True),
                Deck.is_public.is_(True),
                Deck.is_deleted.is_(False),
            )
            .order_by(Deck.created.desc())
            .first()
        )
        if not deck:
            raise NotFoundException(detail="Deck not found.")

    deck_dict = deck_to_dict(session, deck=deck, include_comment_entity_id=True)

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
    release_results = (
        session.query(Release, Deck)
        .outerjoin(Card, Card.release_id == Release.id)
        .outerjoin(Deck, Deck.preconstructed_release == Release.id)
        .filter(
            db.or_(
                Release.stub.in_(release_stubs),
                Card.stub.in_(card_stubs),
            ),
            Release.is_legacy.is_(bool(deck_dict.get("is_legacy"))),
        )
        .order_by(Release.id.asc())
        .distinct(Release.id)
        .all()
    )
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
        deck_details["has_published_snapshot"] = bool(
            session.query(Deck.id)
            .filter(
                Deck.source_id == source_id,
                Deck.is_snapshot.is_(True),
                Deck.is_public.is_(True),
                Deck.is_deleted.is_(False),
            )
            .count()
        )

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
        deck_check: Deck = (
            session.query(
                Deck.user_id, Deck.is_legacy, Deck.is_snapshot, Deck.is_deleted
            )
            .filter(Deck.id == data.id)
            .first()
        )
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
    phoenixborn = (
        session.query(Card.id, Card.name)
        .filter(Card.stub == phoenixborn_stub, Card.is_legacy.is_(False))
        .first()
    )
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
            dice=[x.dict() for x in data.dice] if data.dice else None,
            cards=[x.dict() for x in data.cards] if data.cards else None,
            first_five=data.first_five,
            effect_costs=data.effect_costs,
            tutor_map=data.tutor_map,
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
    return deck_to_dict(session, deck=deck)


@router.post(
    "/decks/{deck_id}/snapshot",
    response_model=DetailResponse,
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
    deck: Deck = (
        session.query(Deck)
        .options(
            db.joinedload("cards"),
            db.joinedload("dice"),
            db.joinedload("selected_cards"),
        )
        .get(deck_id)
    )
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
        preconstructed_release_id = (
            session.query(Release.id)
            .outerjoin(Deck, Deck.preconstructed_release == Release.id)
            .filter(
                Release.stub == data.preconstructed_release,
                Release.is_legacy.is_(False),
                Release.is_public.is_(True),
                Deck.id.is_(None),
            )
            .scalar()
        )
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
    create_snapshot_for_deck(
        session,
        current_user,
        deck,
        title=title,
        description=description,
        is_public=data.is_public,
        preconstructed_release_id=preconstructed_release_id,
        include_first_five=data.include_first_five,
    )
    return {"detail": "Snapshot successfully created!"}


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
    deck: Deck = session.query(Deck).options(db.joinedload("source")).get(deck_id)
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
        and session.query(Deck).filter(Deck.source_id == deck.id).count() == 0
    ):
        session.query(DeckCard).filter(DeckCard.deck_id == deck.id).delete(
            synchronize_session=False
        )
        session.query(DeckDie).filter(DeckDie.deck_id == deck_id).delete(
            synchronize_session=False
        )
        session.query(DeckSelectedCard).filter(
            DeckSelectedCard.deck_id == deck_id
        ).delete(synchronize_session=False)
        session.query(Deck).filter(Deck.id == deck_id).delete(synchronize_session=False)
        session.commit()
        return success_response

    # Otherwise, we're looking at a snapshot or a source deck that has snapshots
    deck.is_deleted = True
    # For snapshots, we need to remove only the Stream entries for that snapshot (leave the rest
    #  of the source deck's snapshots alone).
    if deck.is_snapshot and deck.is_public:
        # Check to see if we have a Stream entry that needs updating
        stream_entry: Stream = (
            session.query(Stream)
            .filter(
                Stream.source_entity_id == deck.source.entity_id,
                Stream.entity_type == "deck",
                Stream.entity_id == deck.entity_id,
            )
            .first()
        )
        if stream_entry:
            # We have a stream entry pointed to this snapshot, so check if we have an older snapshot
            #  that we can swap in
            previous_snapshot: Deck = (
                session.query(Deck)
                .filter(
                    Deck.source_id == deck.source_id,
                    Deck.created < deck.created,
                    Deck.is_deleted.is_(False),
                )
                .order_by(Deck.created.desc())
                .first()
            )
            if previous_snapshot:
                stream_entry.entity_id = previous_snapshot.entity_id
                stream_entry.posted = previous_snapshot.created
            else:
                # Otherwise, just delete the stream entry because this deck no longer has any public
                #  snapshots
                session.delete(stream_entry)
    elif not deck.is_snapshot:
        # If we're not deleting a snapshot, then we need to completely clear out the Stream entry
        session.query(Stream).filter(
            Stream.source_entity_id == deck.entity_id, Stream.entity_type == "deck"
        ).delete(synchronize_session=False)
        # And mark all snapshots as deleted
        session.query(Deck).filter(
            Deck.source_id == deck.id,
            Deck.is_snapshot.is_(True),
            Deck.is_deleted.is_(False),
        ).update({"is_deleted": True}, synchronize_session=False)
    # Commit any pending changes, and return success
    session.commit()
    return success_response


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
    # TODO: Need to complete the logic for snapshot editing/moderation
    pass

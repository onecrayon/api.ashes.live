from typing import List, Union

from fastapi import APIRouter, Depends

from api import db
from api.depends import (
    AUTH_RESPONSES,
    admin_required,
    get_current_user,
    get_session,
    login_required,
)
from api.exceptions import NotFoundException
from api.models import Release, User, UserRelease, UserType
from api.schemas import DetailResponse
from api.schemas.releases import ReleaseIn, ReleaseOut, ReleaseOutAdmin
from api.services.releases import get_releases_query

router = APIRouter()


@router.get(
    "/releases", response_model=List[ReleaseOut], response_model_exclude_unset=True
)
def list_releases(
    show_legacy: bool = False,
    current_user: "UserType" = Depends(get_current_user),
    session: db.Session = Depends(get_session),
):
    """List all releases currently available

    Will include a flag to note which are in the user's collection, if the user has configured
    their collection.

    ## Available filters

    * `show_legacy` (default: false): if true, legacy 1.0 card data will be returned
    """
    query = get_releases_query(
        session=session, current_user=current_user, show_legacy=show_legacy
    )
    return query.all()


@router.put(
    "/releases/mine",
    response_model=List[ReleaseOut],
    response_model_exclude_unset=True,
    responses=AUTH_RESPONSES,
)
def save_collection(
    collection: List[str],
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Update the user's collection in place.

    PUT a list of release slugs to set them as the user's collection (e.g. `['master-set',
    'the-frostdale-giants']`.

    **This is not a patch!** You must pass the entire list of the user's collections every time.
    """
    # Clear out our existing releases
    session.query(UserRelease).filter(UserRelease.user_id == current_user.id).delete()
    session.commit()
    release_ids = (
        (
            session.query(Release.id)
            .filter(
                Release.is_legacy.is_(False),
                Release.is_public.is_(True),
                Release.stub.in_(collection),
            )
            .all()
        )
        if collection
        else None
    )
    if release_ids:
        for row in release_ids:
            session.add(UserRelease(user_id=current_user.id, release_id=row.id))
        session.commit()
    query = get_releases_query(session=session, current_user=current_user)
    return query.all()


@router.patch(
    "/releases/{release_stub}",
    response_model=ReleaseOutAdmin,
    responses={
        404: {
            "model": DetailResponse,
            "description": "Deck could not be found",
        },
        **AUTH_RESPONSES,
    },
)
def update_release(
    release_stub: str,
    data: ReleaseIn,
    session: db.Session = Depends(get_session),
    _: "User" = Depends(admin_required),
):
    """Update a release.

    **Admin only.**
    """
    release = (
        session.query(Release)
        .filter(Release.stub == release_stub, Release.is_legacy.is_(False))
        .first()
    )
    if not release:
        raise NotFoundException(detail="Release not found.")
    release.is_public = data.is_public
    session.commit()
    return release

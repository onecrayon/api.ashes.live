from fastapi import APIRouter, Depends
from sqlalchemy import delete, select

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
    "/releases", response_model=list[ReleaseOut], response_model_exclude_unset=True
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
    stmt = get_releases_query(current_user=current_user, show_legacy=show_legacy)
    return session.execute(stmt).all()


@router.put(
    "/releases/mine",
    response_model=list[ReleaseOut],
    response_model_exclude_unset=True,
    responses=AUTH_RESPONSES,
)
def save_collection(
    collection: list[str],
    session: db.Session = Depends(get_session),
    current_user: "User" = Depends(login_required),
):
    """Update the user's collection in place.

    PUT a list of release slugs to set them as the user's collection (e.g. `['master-set',
    'the-frostdale-giants']`.

    **This is not a patch!** You must pass the entire list of the user's collections every time.
    """
    # Clear out our existing releases
    delete_stmt = delete(UserRelease).where(UserRelease.user_id == current_user.id)
    session.execute(delete_stmt)
    session.commit()
    release_ids = None
    if collection:
        stmt = select(Release.id).where(
            Release.is_legacy.is_(False),
            Release.is_public.is_(True),
            Release.stub.in_(collection),
        )
        release_ids = session.execute(stmt).all()
    if release_ids:
        for row in release_ids:
            session.add(UserRelease(user_id=current_user.id, release_id=row.id))
        session.commit()
    stmt = get_releases_query(current_user=current_user)
    return session.execute(stmt).all()


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
    stmt = select(Release).where(
        Release.stub == release_stub, Release.is_legacy.is_(False)
    )
    release = session.execute(stmt).scalar_one_or_none()
    if not release:
        raise NotFoundException(detail="Release not found.")
    release.is_public = data.is_public
    session.commit()
    return release

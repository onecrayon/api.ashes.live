from typing import List, Union

from fastapi import APIRouter, Depends

from api import db
from api.depends import get_current_user, get_session, login_required
from api.models import Release, User, UserRelease, UserType
from api.schemas.releases import ReleaseOut
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
    "/releases/mine", response_model=List[ReleaseOut], response_model_exclude_unset=True
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

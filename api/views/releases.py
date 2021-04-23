from typing import List, Union

from fastapi import APIRouter, Depends

from api import db
from api.depends import get_current_user, get_session
from api.models import AnonymousUser, Release, User, UserRelease
from api.schemas.releases import ReleaseOut

router = APIRouter()


@router.get(
    "/releases", response_model=List[ReleaseOut], response_model_exclude_unset=True
)
def list_releases(
    show_legacy: bool = False,
    current_user: Union["User", "AnonymousUser"] = Depends(get_current_user),
    session: db.Session = Depends(get_session),
):
    """List all releases currently available

    Will include a flag to note which are in the user's collection, if the user has configured
    their collection.

    ## Available filters

    * `show_legacy` (default: false): if true, legacy 1.0 card data will be returned
    """
    if current_user.is_anonymous():
        query = session.query(Release.name, Release.stub, Release.is_legacy)
    else:
        query = session.query(
            Release.name,
            Release.stub,
            Release.is_legacy,
            db.case(
                [
                    (UserRelease.release_id == Release.id, True),
                ],
                else_=False,
            ).label("is_mine"),
        ).outerjoin(
            UserRelease,
            db.and_(
                UserRelease.release_id == Release.id,
                UserRelease.user_id == current_user.id,
            ),
        )
    releases = query.filter(
        Release.is_legacy.is_(show_legacy),
        Release.is_public.is_(True),
    )
    return releases.all()

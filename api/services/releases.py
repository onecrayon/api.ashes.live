from api import db
from api.models import Release, UserRelease, UserType


def get_releases_query(session: db.Session, current_user: UserType, show_legacy=False):
    """Returns the query necessary to fetch a list of releases

    If a user is passed, then the releases will be tagged `is_mine` if in that user's collection.
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
    query = query.filter(
        Release.is_legacy.is_(show_legacy),
        Release.is_public.is_(True),
    ).order_by(Release.id.asc())
    return query

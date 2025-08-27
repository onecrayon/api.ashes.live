import inspect
import urllib.parse
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Query
from sqlalchemy.sql import Select

from api import db
from api.environment import settings
from api.schemas.pagination import PaginationOptions


def replace_offset(url: str, offset: int) -> str:
    """Updates the offset in the given URL's query string"""
    url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(url.query)
    if offset == 0 and "offset" in query_params:
        del query_params["offset"]
    else:
        query_params["offset"] = [offset]
    encoded_query = urllib.parse.urlencode(query_params, doseq=True)
    # Force HTTPS (unfortunately Render performs some hijinks that result in the scheme improperly being reported
    #  as HTTP internally)
    scheme = "https" if settings.env == "production" else url.scheme
    return urllib.parse.ParseResult(
        scheme, url.netloc, url.path, url.params, encoded_query, url.fragment
    ).geturl()


def paginated_results_for_query(
    session: db.Session,
    stmt: Select,
    paging: PaginationOptions,
    url: str,
) -> dict:
    """Generic pagination results output"""
    # Fetch count and actual query data
    count_stmt = select(db.func.count()).select_from(stmt.subquery())
    total_rows = session.execute(count_stmt).scalar()
    stmt = stmt.limit(paging.limit).offset(paging.offset)
    # Check if this is a single column select of scalars vs ORM objects
    is_orm_query = (
        len(stmt.column_descriptions) == 1
        and inspect.isclass(stmt.column_descriptions[0]["type"])
        and issubclass(stmt.column_descriptions[0]["type"], db.AlchemyBase)
    )

    if is_orm_query:
        rows = session.execute(stmt).scalars().all()
        row_list = rows
    else:
        rows = session.execute(stmt).all()
        if len(stmt.column_descriptions) == 1:
            row_list = [x[0] for x in rows]
        else:
            row_list = rows

    # Construct our next and previous links
    previous_url = None
    if paging.offset > 0:
        prev_offset = paging.offset - paging.limit
        if prev_offset < 0:
            prev_offset = 0
        previous_url = replace_offset(url, prev_offset)

    next_url = None
    next_offset = paging.offset + paging.limit
    if next_offset < total_rows:
        next_url = replace_offset(url, next_offset)
    return {
        "count": total_rows,
        "next": next_url,
        "previous": previous_url,
        "results": row_list,
    }

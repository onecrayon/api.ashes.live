from datetime import datetime, timezone


def utcnow():
    """Returns an *actual* UTC datetime"""
    return datetime.now(tz=timezone.utc)


def pydantic_style_datetime_str(d: datetime) -> str:
    """Returns a datetime formatted for Pydantic usage"""
    return d.isoformat().replace("+00:00", "Z")

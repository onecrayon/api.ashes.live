from datetime import datetime, timezone


def utcnow():
    """Returns an *actual* UTC datetime"""
    return datetime.now(tz=timezone.utc)

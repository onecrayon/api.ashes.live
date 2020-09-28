import re


def stubify(text: str) -> str:
    """Converts the given text into a stub"""
    if not text:
        return None
    return re.sub(r"[^a-z0-9-]", "", text.trim().lower().replace(" ", "-"), flags=re.I)

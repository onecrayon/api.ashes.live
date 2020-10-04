import re


def stubify(text: str) -> str:
    """Converts the given text into a stub"""
    text = text.strip()
    if not text:
        return None
    return re.sub(r"[^a-z0-9-]", "", text.lower().replace(" ", "-"), flags=re.I)

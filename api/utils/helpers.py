from typing import Union
import re


def stubify(text: str) -> str:
    """Converts the given text into a stub"""
    text = text.strip()
    if not text:
        return None
    return re.sub(r"[^a-z0-9-]", "", text.lower().replace(" ", "-"), flags=re.I)


def str_or_int(value: str) -> Union[str, int]:
    """Converts to an integer, but only if it's nothing but digits"""
    if isinstance(value, int):
        return value
    if re.fullmatch(r"\d+", value):
        return int(value)
    return value


def to_prefixed_tsquery(text: str) -> str:
    """If `text` has no spaces, ensures that our TSQUERY tests for prefixes"""
    text = text.strip()
    if " " in text:
        return text
    return f"{text} | {text}:*"

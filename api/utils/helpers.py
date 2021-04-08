import re
from itertools import chain, combinations
from typing import Union


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
    # If there are spaces in text, we assume that they're doing an exact phrase search
    if " " in text:
        return " <-> ".join(text.split())
    return f"{text} | {text}:*"


def powerset(iterable):
    """Returns the powerset of the passed iterable:

    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

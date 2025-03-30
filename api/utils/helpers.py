import re
from itertools import chain, combinations


def stubify(text: str) -> str:
    """Converts the given text into a stub"""
    text = text.strip()
    if not text:
        return None
    return re.sub(r"[^a-z0-9-]", "", text.lower().replace(" ", "-"), flags=re.I)


def str_or_int(value: str | None) -> str | int | None:
    """Converts to an integer, but only if it's nothing but digits"""
    if value is None:
        return value
    if isinstance(value, int):
        return value
    if re.fullmatch(r"\d+", value):
        return int(value)
    return value


def to_prefixed_tsquery(text: str) -> str:
    """If `text` has no spaces, ensures that our TSQUERY tests for prefixes"""
    # Convert some special characters that could mess with our results to spaces
    text = re.sub(r"[&:-]", " ", text)
    # Collapse multiple spaces into a single space
    text = re.sub(r"[ ]{2,}", " ", text)
    # And remove all other special characters
    text = re.sub(r"[^a-z ]", "", text, flags=re.I)
    # Finally strip spaces off the sides
    text = text.strip()
    # If there are spaces in text, we assume that they're doing an exact phrase search
    if " " in text:
        all_words = " <-> ".join(text.split())
        return f"({all_words}) | ({all_words}:*)"
    return f"{text} | {text}:*"


def powerset(iterable):
    """Returns the powerset of the passed iterable:

    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

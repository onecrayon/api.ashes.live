from api.utils.helpers import stubify


def test_stubify_empty():
    """Stubify logic must return None if it doesn't have a name"""
    assert stubify("") is None
    assert stubify("    ") is None

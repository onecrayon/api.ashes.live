from fastapi.testclient import TestClient

from api import db

from .deck_utils import populate_cards_for_decks


def test_deck_listing(client: TestClient, session: db.Session):
    """Deck filtration must function properly"""
    # I really hate giant test methods (tests should be as small as possible), but this is an
    #  exception because we have to do a ton of SQL queries to populate example data, so it's
    #  better to populate once and then test comprehensively.
    populate_cards_for_decks(session)
    # TODO: implement actual tests once I have a full card and deck database populated

import pytest

from api.db import Session

from .deck_utils import create_cards_for_decks


@pytest.fixture(scope="package")
def cards_session(session_local: Session, monkeypatch_package) -> Session:
    """Populate our database with the cards needed to create decks once for the package

    This causes our session to be reused between all tests in this package, with specific classes
    handling deck/user data persistence using nested rollbacks.
    """
    # Creates a nested transaction that includes standard card data
    session = session_local()
    session.begin_nested()
    # Overwrite commits with flushes so that we can query stuff, but it's in the same transaction
    monkeypatch_package.setattr(session, "commit", session.flush)
    create_cards_for_decks(session)
    try:
        yield session
    finally:
        session.rollback()
        session.close()


@pytest.fixture(scope="module")
def decks_session(cards_session):
    """Adds a module-level layer of nesting to keep the decks and such created in modules isolated"""
    cards_session.begin_nested()
    try:
        yield cards_session
    finally:
        cards_session.rollback()


@pytest.fixture(scope="function")
def session(decks_session):
    """Return a nested transaction on the outer session, to prevent rolling back card data"""
    decks_session.begin_nested()
    try:
        yield decks_session
    finally:
        decks_session.rollback()

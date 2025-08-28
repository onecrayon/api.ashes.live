import pytest
from sqlalchemy.engine import Engine

from api.db import Session

from .deck_utils import create_cards_for_decks


@pytest.fixture(scope="package")
def cards_connection(test_engine: Engine) -> Session:
    """Populate our database with the cards needed to create decks once for the package

    This causes our session to be reused between all tests in this package, with specific files
    handling deck/user data persistence using nested rollbacks.
    """
    # Create a nested transaction that includes standard card data
    connection = test_engine.connect()
    cards_transaction = connection.begin()
    cards_session = Session(bind=connection, join_transaction_mode="create_savepoint")
    # Create our fake cards that are relied on by the tests in this module
    create_cards_for_decks(cards_session)

    try:
        yield connection
    finally:
        cards_transaction.rollback()
        connection.close()


@pytest.fixture(scope="function")
def session(cards_connection):
    """Return a nested transaction on the outer session, to prevent rolling back card data"""
    savepoint = cards_connection.begin_nested()
    try:
        with Session(bind=cards_connection, join_transaction_mode="create_savepoint") as session:
            yield session
    finally:
        savepoint.rollback()

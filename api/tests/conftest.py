"""Standard pytest fixtures used across all API tests

## USAGE
    from fastapi import status
    from fastapi.testclient import TestClient

    def test_endpoint(client: TestClient):
        response = client.get("/my-endpoint/")
        assert response.status_code == status.HTTP_200_OK
"""

import pytest
from _pytest.monkeypatch import MonkeyPatch
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists, drop_database

import api.environment

# `models` is necessary to ensure that AlchemyBase is properly populated
from api import app, db
from api.depends import get_session

from . import utils


@pytest.fixture(scope="function", autouse=True)
def testing_environment(monkeypatch):
    # Ensure we don't have any SendGrid API key stored for a real SendGrid account
    utils.monkeypatch_settings(monkeypatch, {"sendgrid_api_key": None})
    # Ensure we don't have any SMTP host key stored so the tests won't accidentally send emails
    utils.monkeypatch_settings(monkeypatch, {"smtp_host": None})


@pytest.fixture(scope="session")
def test_engine():
    """Override the default database with our testing database, and make sure to run migrations"""
    settings = api.environment.ApplicationSettings()
    test_engine = create_engine(
        (
            f"postgresql+psycopg2://{settings.postgres_user}:{settings.postgres_password}"
            f"@{settings.postgres_host}:{settings.postgres_port}/test"
        ),
        echo=False,
        future=True,
    )
    # Drop database and recreate to ensure tests are always run against a clean slate
    if database_exists(test_engine.url):
        drop_database(test_engine.url)
    create_database(test_engine.url)
    # Install necessary pgcrypto extension (for database-level default UUIDs)
    with test_engine.connect() as connection:
        with connection.begin():
            connection.execute(db.text("create extension pgcrypto"))
    # Create all tables
    db.AlchemyBase.metadata.create_all(bind=test_engine)
    try:
        yield test_engine
    finally:
        drop_database(test_engine.url)


@pytest.fixture(scope="function")
def session(test_engine: Engine, monkeypatch) -> Session:
    """Return an SQLAlchemy session for this test, complete with SAVEPOINT for internal rollbacks"""
    connection = test_engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection, join_transaction_mode="create_savepoint")
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


@pytest.fixture(scope="function")
def client(session: Session) -> TestClient:
    """Return a FastAPI TestClient for issuing requests and rollback session transaction"""

    def override_get_session():
        yield session

    app.dependency_overrides[get_session] = override_get_session

    yield TestClient(app)


@pytest.fixture(scope="package")
def monkeypatch_package():
    """Monkeypatch must be re-implemented to be included in fixtures for non-function scopes

    See: https://github.com/pytest-dev/pytest/issues/363
    """
    monkeypatch = MonkeyPatch()
    yield monkeypatch
    monkeypatch.undo()

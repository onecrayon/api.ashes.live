from fastapi import status
from fastapi.testclient import TestClient
import sqlalchemy.orm
from sqlalchemy.exc import TimeoutError


def test_health_check_success(client: TestClient):
    """Health check must return 200 on success"""
    response = client.get("/health-check/")
    assert response.status_code == status.HTTP_200_OK


def test_health_check_postgres_failure(client: TestClient, monkeypatch):
    """Health check must return 503 on Postgres failure"""

    def _raise_postgres_error(*args, **kwargs):
        """Fakes a Postgres connection failure"""
        raise TimeoutError()

    monkeypatch.setattr(sqlalchemy.orm.Session, "query", _raise_postgres_error)
    response = client.get("/health-check/")
    assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE

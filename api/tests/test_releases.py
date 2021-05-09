from fastapi import status
from fastapi.testclient import TestClient

from api import db
from api.models import Release, UserRelease
from api.tests.utils import create_user_token


def test_get_releases(client: TestClient, session: db.Session):
    """Releases endpoint must return a list of all releases"""
    master_set = Release(name="Master Set")
    master_set.is_public = True
    session.add(master_set)
    session.commit()
    response = client.get("/v2/releases")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


def test_get_releases_public_only(client: TestClient, session: db.Session):
    """Releases list must only include public releases"""
    master_set = Release(name="Master Set")
    master_set.is_public = True
    session.add(master_set)
    session.add(Release(name="Unreleased"))
    session.commit()
    response = client.get("/v2/releases")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 1
    assert data[0]["stub"] == master_set.stub


def test_get_releases_legacy(client: TestClient, session: db.Session):
    """Releases list must only show legacy releases when they are requested"""
    master_set = Release(name="Master Set")
    master_set.is_public = True
    session.add(master_set)
    core_set = Release(name="Core Set")
    core_set.is_legacy = True
    core_set.is_public = True
    session.add(core_set)
    session.commit()
    response = client.get("/v2/releases")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 1
    assert data[0]["stub"] == master_set.stub
    response = client.get("/v2/releases", params={"show_legacy": True})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 1
    assert data[0]["stub"] == core_set.stub


def test_get_releases_mine(client: TestClient, session: db.Session):
    """Releases list must mark which releases are in the user's collection"""
    master_set = Release(name="Master Set")
    master_set.is_public = True
    session.add(master_set)
    first_expansion = Release(name="First Expansion")
    first_expansion.is_public = True
    session.add(first_expansion)
    session.commit()
    user, token = create_user_token(session)
    session.add(UserRelease(release_id=master_set.id, user_id=user.id))
    session.commit()
    response = client.get(
        "/v2/releases",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data[0]["stub"] == master_set.stub
    assert data[0]["is_mine"] == True
    assert data[1]["is_mine"] == False


def test_put_releases(client: TestClient, session: db.Session):
    """Putting my releases must work"""
    master_set = Release(name="Master Set")
    master_set.is_public = True
    session.add(master_set)
    first_expansion = Release(name="First Expansion")
    first_expansion.is_public = True
    session.add(first_expansion)
    session.commit()
    user, token = create_user_token(session)
    assert (
        session.query(UserRelease).filter(UserRelease.user_id == user.id).count() == 0
    )
    response = client.put(
        "/v2/releases/mine",
        json=[master_set.stub],
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data[0]["stub"] == master_set.stub
    assert data[0]["is_mine"] == True
    assert data[1]["is_mine"] == False


def test_put_releases_bad_release(client: TestClient, session: db.Session):
    """Putting a nonsense stub must work"""
    master_set = Release(name="Master Set")
    master_set.is_public = True
    session.add(master_set)
    session.commit()
    user, token = create_user_token(session)
    response = client.put(
        "/v2/releases/mine",
        json=["fake-set"],
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data[0]["stub"] == master_set.stub
    assert data[0]["is_mine"] == False

from api import db
from api.services.user import _random_badges, generate_badges
from api.utils.auth import verify_password
from .utils import _create_user_password


def test_create_user(session: db.Session):
    """Unit test to verify user creation logic"""
    user, password = _create_user_password(session)
    assert verify_password(password, user.password) == True


def test_generate_badges_ten_failures(session: db.Session):
    """Unit test to simulate 10 failures to generate unique badges"""
    badge = _random_badges(number=1)[0]
    new_badge = generate_badges(session, single=True, number=1, length=4, _tries=11)
    assert len(new_badge) == len(badge) + 1


def test_generate_badges_kid_friendly_failure(session: db.Session, monkeypatch):
    """Unit test to simulate badge generation failing kid-friendly test"""
    # Monkeypatch the resopnse from our badge generator
    def _fake_badges(*args, **kwargs):
        # We only want this to hijack the function once
        monkeypatch.undo()
        return ["2g1c"]

    monkeypatch.setattr("api.services.user._random_badges", _fake_badges)
    badge = generate_badges(session, single=True, number=1)
    assert badge != "2g1c"


def test_generate_badges_all_taken(session: db.Session, monkeypatch):
    """Unit test to simulate all badges being taken"""
    # Create a user with our target badge
    user, _ = _create_user_password(session)
    user.badge = "1234"
    session.commit()

    # Ensure our target badge is "randomly" generated the first time
    def _fake_badges(*args, **kwargs):
        # We only want to hijack this once
        monkeypatch.undo()
        return ["1234"]

    monkeypatch.setattr("api.services.user._random_badges", _fake_badges)

    badge = generate_badges(session, single=True, number=1)
    assert badge != "1234"


def test_generate_badges_some_taken(session: db.Session, monkeypatch):
    """Unit test to simulate some badges being taken (recursion)"""
    user, _ = _create_user_password(session)
    user.badge = "1234"
    session.commit()

    # Ensure our target badge is "randomly" generated the first time
    def _fake_badges(*args, **kwargs):
        # We only want to hijack this once
        monkeypatch.undo()
        return ["1234", "5678"]

    monkeypatch.setattr("api.services.user._random_badges", _fake_badges)

    badges = generate_badges(session, single=False, number=2)
    assert "5678" in badges

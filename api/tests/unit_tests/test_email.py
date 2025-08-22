import api.utils.email as email_utils

from .. import utils


def _set_sender_settings(
    monkeypatch, sender_email: bool = True, smtp_host: bool = True
):
    """Automatically set the necessary settings for sending email"""
    utils.monkeypatch_settings(
        monkeypatch,
        {
            "mail_sender_address": (
                utils.generate_random_email() if sender_email else None
            ),
            "smtp_host": "localhost" if smtp_host else None,
        },
    )


_GOOD_DATA = {
    "invite_token": "fake-token",
    "email": "fake@email.com",
}


def test_email_no_smtp_host(monkeypatch):
    """Trying to email without an SMTP host should fail"""
    # Make sure that we don't fail due to a missing sender
    _set_sender_settings(monkeypatch, sender_email=True, smtp_host=False)
    email = utils.generate_random_email()
    assert (
        email_utils.send_message(email, "invite", subject="Test", data=_GOOD_DATA)
        == False
    )


def test_email_no_sender_address(monkeypatch):
    """Trying to send an email without a sender address should fail"""
    # Ensure sender address is blank but we have an SMTP host
    _set_sender_settings(monkeypatch, sender_email=False, smtp_host=True)
    email = utils.generate_random_email()
    assert (
        email_utils.send_message(email, "invite", subject="Test", data=_GOOD_DATA)
        == False
    )


def test_email_no_template_name(monkeypatch):
    """Trying to send an email without a template ID should fail"""
    _set_sender_settings(monkeypatch)
    email = utils.generate_random_email()
    assert (
        email_utils.send_message(email, None, subject="Test", data=_GOOD_DATA) == False
    )


def test_debug_email_remap_missing(monkeypatch):
    """Sending in debug mode requires an address to remap to"""
    _set_sender_settings(monkeypatch)
    utils.monkeypatch_settings(
        monkeypatch,
        {
            "mail_debug_recipient": None,
            "debug": True,
        },
    )
    email = utils.generate_random_email()
    assert (
        email_utils.send_message(email, "invite", subject="Test", data=_GOOD_DATA)
        == False
    )


def test_debug_email_remap(monkeypatch):
    """Sending in debug mode will remap the address"""
    sent_to_address = None

    def _send_to_smtp_success(
        from_address: str, to_address: str, email_body: str
    ) -> bool:
        nonlocal sent_to_address
        sent_to_address = to_address
        return True

    monkeypatch.setattr(email_utils, "send_to_smtp", _send_to_smtp_success)
    _set_sender_settings(monkeypatch)
    debug_redirect_email = utils.generate_random_email()
    utils.monkeypatch_settings(
        monkeypatch,
        {
            "mail_debug_recipient": debug_redirect_email,
            "debug": True,
        },
    )
    email = utils.generate_random_email()
    assert (
        email_utils.send_message(email, "invite", subject="Test", data=_GOOD_DATA)
        == True
    )
    assert sent_to_address == debug_redirect_email


def test_email_success(monkeypatch):
    """Sending an email successfully must send to the right address"""
    sent_to_address = None

    def _send_to_smtp_success(
        from_address: str, to_address: str, email_body: str
    ) -> bool:
        nonlocal sent_to_address
        sent_to_address = to_address
        return True

    monkeypatch.setattr(email_utils, "send_to_smtp", _send_to_smtp_success)
    _set_sender_settings(monkeypatch)
    utils.monkeypatch_settings(
        monkeypatch,
        {
            "debug": False,
        },
    )
    email = utils.generate_random_email()
    assert (
        email_utils.send_message(email, "invite", subject="Test", data=_GOOD_DATA)
        == True
    )
    assert sent_to_address == email

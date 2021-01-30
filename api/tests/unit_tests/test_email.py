from collections import namedtuple

from sendgrid.helpers.mail.exceptions import SendGridException

import api.utils.email as email_utils
from api.environment import settings
from .. import utils

# Define utility functions
Response = namedtuple("Response", ["status_code", "body"])


class SendGridAPIMock:
    """Mock class that mimics the minimal behavior of the SendGridAPIClient that we're using"""

    VALID_TOKEN = utils.generate_random_chars(8)
    VALID_TEMPLATE_ID = "faketemplateID"

    def __init__(self, api_key: str = None, throws_exception: bool = False):
        self.api_key = api_key
        self.throws_exception = throws_exception
        self.sent_emails = []

    def send(self, message):
        if self.throws_exception:
            raise SendGridException("Not happening.")
        if message.template_id.template_id != self.VALID_TEMPLATE_ID:
            return Response(status_code=400, body="Bad template ID.")
        self.sent_emails.append(
            [x["email"] for p in message.personalizations for x in p.tos]
        )
        return Response(status_code=200, body="Nice going.")


def _set_sender_token(
    monkeypatch, sender_email: bool = True, sendgrid_token: bool = True
):
    """Automatically set the necessary settings for sending email"""
    utils.monkeypatch_settings(
        monkeypatch,
        {
            "mail_sender_address": utils.generate_random_email()
            if sender_email
            else None,
            "sendgrid_api_key": SendGridAPIMock.VALID_TOKEN if sendgrid_token else None,
        },
    )


def test_email_no_sendgrid_token(caplog, monkeypatch):
    """Trying to email without a Sendgrid token should fail"""
    # Make sure that we don't fail due to a missing sender
    _set_sender_token(monkeypatch, sender_email=True, sendgrid_token=False)
    email = utils.generate_random_email()
    assert email_utils.send_message(email, SendGridAPIMock.VALID_TEMPLATE_ID) == False
    # Verify the error was logged
    assert len(caplog.records) == 1


def test_email_no_sender_address(caplog, monkeypatch):
    """Trying to send an email without a sender address should fail"""
    # Ensure sender address is blank but we have a SendGrid token
    _set_sender_token(monkeypatch, sender_email=False, sendgrid_token=True)
    email = utils.generate_random_email()
    assert email_utils.send_message(email, SendGridAPIMock.VALID_TEMPLATE_ID) == False
    # Verify the error was logged
    assert len(caplog.records) == 1


def test_email_no_template_id(caplog, monkeypatch):
    """Trying to send an email without a template ID should fail"""
    _set_sender_token(monkeypatch)
    email = utils.generate_random_email()
    assert email_utils.send_message(email, None) == False
    assert len(caplog.records) == 1


def test_debug_email_remap_missing(monkeypatch):
    """Sending in debug mode requires an address to remap to"""
    _set_sender_token(monkeypatch)
    utils.monkeypatch_settings(
        monkeypatch,
        {
            "mail_debug_recipient": None,
            "debug": True,
        },
    )
    email = utils.generate_random_email()
    assert email_utils.send_message(email, SendGridAPIMock.VALID_TEMPLATE_ID) == False


def test_debug_email_remap(monkeypatch):
    """Sending in debug mode will remap the address"""
    sendgrid_client_mock = None

    def _prep_sendgrid_mock(api_key):
        nonlocal sendgrid_client_mock
        sendgrid_client_mock = SendGridAPIMock(api_key=api_key)
        return sendgrid_client_mock

    monkeypatch.setattr(email_utils, "SendGridAPIClient", _prep_sendgrid_mock)
    _set_sender_token(monkeypatch)
    utils.monkeypatch_settings(
        monkeypatch,
        {
            "mail_debug_recipient": utils.generate_random_email(),
            "debug": True,
        },
    )
    email = utils.generate_random_email()
    assert email_utils.send_message(email, SendGridAPIMock.VALID_TEMPLATE_ID) == True
    assert len(sendgrid_client_mock.sent_emails) == 1
    assert sendgrid_client_mock.sent_emails[0][0] == settings.mail_debug_recipient


def test_email_sendgrid_error(monkeypatch):
    """Sending email handles SendGrid 400+ errors"""
    monkeypatch.setattr(email_utils, "SendGridAPIClient", SendGridAPIMock)
    _set_sender_token(monkeypatch)
    utils.monkeypatch_settings(
        monkeypatch,
        {
            "debug": False,
        },
    )
    email = utils.generate_random_email()
    assert email_utils.send_message(email, "badTemplateID") == False


def test_email_sendgrid_exception(monkeypatch):
    """Sending email handles SendGrid exceptions"""

    def _prep_sendgrid_mock(api_key):
        return SendGridAPIMock(api_key=api_key, throws_exception=True)

    monkeypatch.setattr(email_utils, "SendGridAPIClient", _prep_sendgrid_mock)
    _set_sender_token(monkeypatch)
    utils.monkeypatch_settings(
        monkeypatch,
        {
            "debug": False,
        },
    )
    email = utils.generate_random_email()
    assert email_utils.send_message(email, SendGridAPIMock.VALID_TEMPLATE_ID) == False


def test_email_success(monkeypatch):
    """Sending an email successfully must send to the right address"""
    sendgrid_client_mock = None

    def _prep_sendgrid_mock(api_key):
        nonlocal sendgrid_client_mock
        sendgrid_client_mock = SendGridAPIMock(api_key=api_key)
        return sendgrid_client_mock

    monkeypatch.setattr(email_utils, "SendGridAPIClient", _prep_sendgrid_mock)
    _set_sender_token(monkeypatch)
    utils.monkeypatch_settings(
        monkeypatch,
        {
            "debug": False,
        },
    )
    email = utils.generate_random_email()
    data = {"fake": "yep"}
    assert (
        email_utils.send_message(email, SendGridAPIMock.VALID_TEMPLATE_ID, data) == True
    )
    assert len(sendgrid_client_mock.sent_emails) == 1
    assert sendgrid_client_mock.sent_emails[0][0] == email

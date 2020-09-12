import logging
from typing import Optional

from sendgrid import SendGridAPIClient
import sendgrid.helpers.mail as sendgrid_helpers

from api.environment import settings


logger = logging.getLogger(__name__)


def send_message(recipient, template_id, data: Optional[dict] = None) -> bool:
    """Sends a transactional email through SendGrid

    Templates are stored within SendGrid with a copy of the most recent version checked into
    version control within the root `email_templates` folder. You can define templates in either
    location, as long as you sync them up afterward (automated process for this is a WIP).

    Once you have a template, you will need to define its ID in your `.env` file.

    Then you can send it by passing recipient email, the template ID, and the dynamic data
    with which to populate the template (which data is required depends on the template).

    Returns a bool whether the email was successfully queued up by SendGrid or not.
    """
    api_key = settings.sendgrid_api_key
    sender = settings.mail_sender_address
    if not api_key or not sender:
        logger.error(
            f"Unable to send email due to missing API key <{api_key}> or sender <{sender}>."
        )
        return False
    if not template_id:
        logger.error(
            f"Template ID <{template_id}> not defined! Email has not been sent."
        )
        return False
    # Remap addresses
    if settings.debug:
        if not settings.mail_debug_recipient:
            logger.info(
                f"DEBUG: Transactional email <{template_id}> to <{recipient}> has not been sent. "
                f"Please add `MAIL_DEBUG_RECIPIENT` to your .env file if you wish to send email "
                f"while debugging."
            )
            return False
        new_recipient = settings.mail_debug_recipient
        logger.info(f"Replacing email recipient: <{recipient}>")
        recipient = new_recipient

    sendgrid_client = SendGridAPIClient(api_key=api_key)
    # sender might be a tuple of (name, email)
    sendgrid_helpers.Email(sender)
    to_email = sendgrid_helpers.To(recipient)
    message = sendgrid_helpers.Mail(from_email=sender, to_emails=to_email)
    message.template_id = template_id
    if data:
        message.dynamic_template_data = data
    try:
        response = sendgrid_client.send(message)
        if response.status_code >= 400:
            logger.error(
                f"Mail delivery failed ({response.status_code}): {response.body}"
            )
            return False
        return True
    except Exception as e:
        logger.error(f"Failed to send email via SendGrid API: {e}")
        logger.error(f"Mail request: {message}")
        return False

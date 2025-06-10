import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from functools import lru_cache
from pathlib import Path
from smtplib import SMTP, SMTP_SSL, SMTPException
from string import Template

from api.environment import settings

logger = logging.getLogger(__name__)


@lru_cache
def read_template(template_name: str) -> tuple[str, str]:
    """Reads email template files from disk, and returns their contents"""
    base_path = Path(__file__).parent / "../../email_templates"
    text_path = base_path / f"{template_name}.txt"
    html_path = base_path / f"{template_name}.html"
    with text_path.open() as f:
        text_template = f.read()
    with html_path.open() as f:
        html_template = f.read()
    return text_template, html_template


def send_to_smtp(
    from_address: str, to_address: str, email_body: str
) -> bool:  # pragma: no cover
    """Actually sends the email via SMTP

    Separated into its own method for easier testing.
    """
    # Figure out if we're using TLS or SSL
    use_starttls = settings.smtp_port == 587
    SMTP_Class = SMTP if use_starttls else SMTP_SSL
    try:
        with SMTP_Class(host=settings.smtp_host, port=settings.smtp_port) as smtp:
            if use_starttls:
                smtp.starttls()
            if settings.smtp_username and settings.smtp_password:
                smtp.login(settings.smtp_username, settings.smtp_password)
            smtp.sendmail(from_address, to_address, email_body)
        return True
    except SMTPException as e:
        logger.error(f"Unable to send email due to SMTP error: {e}", exc_info=e)
        return False


def send_message(recipient, template_name: str, subject: str, data: dict) -> bool:
    """Sends a transactional email through SMTP

    Template names are the shared filename between the `*.txt` and `*.html` files in the
    `email_templates` directory (and both files are REQUIRED!).

    Templates use `string.Template` syntax (e.g. variables are `$var_name` and literal dollars are
    `$$`).

    Returns a bool whether the email was successfully sent or not.
    """
    smtp_host = settings.smtp_host
    sender = settings.mail_sender_address
    if not smtp_host or not sender:
        logger.error(
            f"Unable to send email due to missing SMTP host <{smtp_host}> or sender <{sender}>."
        )
        return False
    if not template_name:
        logger.error(
            f"Template name <{template_name}> not defined! Email has not been sent."
        )
        return False
    # Remap addresses
    if settings.debug:
        if not settings.mail_debug_recipient:
            logger.info(
                f"DEBUG: Transactional email <{template_name}> to <{recipient}> has not been sent. "
                f"Please add `MAIL_DEBUG_RECIPIENT` to your .env file if you wish to send email "
                f"while debugging."
            )
            return False
        new_recipient = settings.mail_debug_recipient
        logger.info(f"Replacing email recipient: <{recipient}>")
        recipient = new_recipient

    # Create our email message
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = settings.mail_sender_address
    message["To"] = recipient

    # Parse our templates
    text_template, html_template = read_template(template_name)
    body_text = Template(text_template).substitute(**data)
    body_html = Template(html_template).substitute(**data)

    # Record the MIME types of both parts - text/plain and text/html.
    text_part = MIMEText(body_text, "plain")
    html_part = MIMEText(body_html, "html")

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    message.attach(text_part)
    message.attach(html_part)

    return send_to_smtp(settings.mail_sender_address, recipient, message.as_string())

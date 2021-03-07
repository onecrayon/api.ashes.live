import re
import string
from datetime import timedelta
from random import choice

from api import db, models
from api.environment import settings
from api.utils.auth import create_access_token, generate_password_hash


def access_token_for_user(user: "models.User", is_long_term=False) -> str:
    """Returns an access token for the given user"""
    if is_long_term:
        access_token_expires = timedelta(days=settings.access_token_remember_me_days)
    else:
        access_token_expires = timedelta(minutes=settings.access_token_expiry)
    return create_access_token(
        data={"sub": user.badge},
        expires_delta=access_token_expires,
    )


def get_invite_for_email(session: "db.Session", email: str) -> "models.Invite":
    """Fetches or creates a new invite for the given email"""
    invitation = (
        session.query(models.Invite).filter(models.Invite.email == email).first()
    )
    if invitation:
        invitation.requests += 1
    else:
        # Create our invitation
        invitation = models.Invite(email=email)
        session.add(invitation)
    session.commit()
    return invitation


def create_user(
    session: "db.Session",
    email,
    password,
    badge=None,
    username=None,
    description=None,
    newsletter_opt_in=False,
) -> "models.User":
    """Creates a User and adds them to the database"""
    # Hash the password
    password = generate_password_hash(password)
    if not badge or not re.search(r"^[0-9][a-z0-9*&+=-]+[a-z0-9*!]$", badge):
        badge = generate_badges(session, single=True)
    username = (
        username
        if username
        else choice(
            [
                "Aradel Summergaard",
                "Brennen Blackcloud",
                "Coal Roarkwin",
                "Dimona Odinstar",
                "Jessa Na Ni",
                "Leo Sunshadow",
                "Lulu Firststone",
                "Maeoni Viper",
                "Namine Hymntide",
                "Noah Redmoon",
                "Odette Diamondcrest",
                "Orrick Gilstream",
                "Rin Northfell",
                "Saria Guideman",
                "Victoria Glassfire",
                "Echo Greystorm",
                "Jericho Kill",
                "Astrea",
                "Koji Wolfcub",
                "Harold Westraven",
                "Sembali Grimtongue",
                "Rimea Careworn",
                "Xander Heartsblood",
                "Fiona Mercywind",
                "James Endersight",
            ]
        )
    )
    user = models.User(
        email=email,
        password=password,
        badge=badge,
        username=username,
        description=description,
        newsletter_opt_in=newsletter_opt_in,
    )
    session.add(user)
    session.commit()
    return user


def generate_badges(
    session: "db.Session", single=False, number=8, length=4, _tries=1, _current=None
):
    """Generates a list of user badges

    * `single`: if True, returns a single badge
    * `number`: number of badges to generate
    * `length`: the length of each individual badge
    * `_tries`: do not set; used internally to track recursion on failure
    * `_current`: do not set; used internally
    """
    # Increase the length if we failed to find badges 10 times in a row
    if _tries > 10:
        return generate_badges(session, single=single, number=number, length=length + 1)
    # Generate our badges
    options = _random_badges(number=number, length=length)
    # Test for kid-friendliness
    options = [x for x in options if kid_friendly(x)]
    # Highly unlikely, but if *all* options were bad, try again
    if not options:
        return generate_badges(
            session,
            single=single,
            number=number,
            length=length,
            _tries=_tries + 1,
            _current=_current,
        )
    taken = [
        badge
        for (badge,) in session.query(models.User.badge)
        .filter(models.User.badge.in_(options))
        .all()
    ]
    if taken:
        options = [x for x in options if x not in taken]
    # Highly unlikely, but if all random badges are taken, try again
    if not options:
        return generate_badges(
            session,
            single=single,
            number=number,
            length=length,
            _tries=_tries + 1,
            _current=_current,
        )
    # Add pre-located options to our list
    if _current:
        options = _current + options
    # If we had to discard some, generate some more to fill in the gaps
    if len(options) < number:
        return generate_badges(
            session,
            single=single,
            number=number,
            length=length,
            _tries=_tries + 1,
            _current=options,
        )
    return options[0] if single else options[:number]


def _random_badges(number=8, length=4):
    return [
        "".join(
            [
                # First character is always a number
                choice(string.digits),
                # Next characters are alphanumeric or middle punctuation
                "".join(
                    choice(string.ascii_lowercase + string.digits + "*&-+=")
                    for _ in range(length - 2)
                ),
                # Final character alphanumeric or ending punctuation
                choice(string.ascii_lowercase + string.digits + "*!"),
            ]
        )
        for _ in range(number)
    ]


def kid_friendly(badge):
    return kid_unfriendly_re.search(badge) is None


# This is compiled based on data and logic from a file outside the project repo
kid_unfriendly_re = re.compile(
    r"2(?:g|6)1(?:c|k)|(?:a|\*|@)n(?:a|\*|@)(?:i|\*|l|!|1)|(?:a|\*|@)n(?:u|\*|v)(?:s|\$|5|z|2)"
    r"|(?:a|\*|@)(?:s|\$|5|z|2)(?:s|\$|5|z|2)|(?:b|l3|i3)(?:b|l3|i3)(?:w|vv)|(?:b|l3|i3)d(?:s|\$|5|z|2)m"
    r"|(?:b|l3|i3)(?:i|\*|l|!|1)m(?:b|l3|i3)(?:o|\*|0)|(?:b|l3|i3)(?:i|\*|l|!|1)(?:t|7)(?:c|k)h"
    r"|(?:b|l3|i3)(?:o|\*|0)n(?:e|\*|3)r|(?:b|l3|i3)(?:o|\*|0)(?:o|\*|0)(?:b|l3|i3)"
    r"|(?:b|l3|i3)(?:u|\*|v)(?:t|7)(?:t|7)|(?:c|k)(?:i|\*|l|!|1)(?:i|\*|l|!|1)(?:t|7)"
    r"|(?:c|k)(?:o|\*|0)(?:c|k)(?:c|k)|(?:c|k)(?:o|\*|0)(?:o|\*|0)n|(?:c|k)(?:u|\*|v)m|(?:c|k)(?:u|\*|v)n(?:t|7)"
    r"|d(?:i|\*|l|!|1)(?:c|k)(?:c|k)|d(?:i|\*|l|!|1)(?:i|\*|l|!|1)d(?:o|\*|0)|d(?:o|\*|0)mm(?:e|\*|3)(?:s|\$|5|z|2)"
    r"|d(?:u|\*|v)d(?:a|\*|@)|(?:e|\*|3)(?:c|k)(?:c|k)h(?:i|\*|l|!|1)|(?:f|ph)(?:a|\*|@)(?:g|6)"
    r"|(?:f|ph)(?:e|\*|3)(?:c|k)(?:a|\*|@)(?:i|\*|l|!|1)|(?:f|ph)(?:e|\*|3)(?:i|\*|l|!|1)(?:c|k)h"
    r"|(?:f|ph)(?:e|\*|3)(?:i|\*|l|!|1)(?:t|7)(?:c|k)h|(?:f|ph)(?:e|\*|3)md(?:o|\*|0)m"
    r"|(?:f|ph)(?:u|\*|v)(?:c|k)(?:c|k)|(?:g|6)-(?:s|\$|5|z|2)p(?:o|\*|0)(?:t|7)|(?:g|6)(?:a|\*|@)y"
    r"|(?:g|6)(?:o|\*|0)(?:a|\*|@)(?:t|7)(?:c|k)x|(?:g|6)(?:o|\*|0)(?:a|\*|@)(?:t|7)(?:s|\$|5|z|2)(?:e|\*|3)"
    r"|(?:g|6)(?:o|\*|0)(?:c|k)(?:c|k)(?:u|\*|v)n|(?:g|6)r(?:o|\*|0)p(?:e|\*|3)"
    r"|(?:g|6)(?:s|\$|5|z|2)p(?:o|\*|0)(?:t|7)|(?:g|6)(?:u|\*|v)r(?:o|\*|0)"
    r"|h(?:e|\*|3)n(?:t|7)(?:a|\*|@)(?:i|\*|l|!|1)|h(?:o|\*|0)m(?:o|\*|0)|h(?:o|\*|0)n(?:c|k)(?:e|\*|3)y"
    r"|h(?:o|\*|0)(?:o|\*|0)(?:c|k)(?:e|\*|3)r|h(?:u|\*|v)mp|(?:i|\*|l|!|1)n(?:c|k)(?:e|\*|3)(?:s|\$|5|z|2)(?:t|7)"
    r"|j(?:i|\*|l|!|1)(?:s|\$|5|z|2)(?:s|\$|5|z|2)|j(?:u|\*|v)(?:g|6)(?:g|6)(?:s|\$|5|z|2)"
    r"|(?:c|k)(?:i|\*|l|!|1)(?:c|k)(?:e|\*|3)|(?:c|k)(?:i|\*|l|!|1)n(?:c|k)y"
    r"|(?:i|\*|l|!|1)(?:o|\*|0)(?:i|\*|l|!|1)(?:i|\*|l|!|1)(?:t|7)(?:a|\*|@)|m(?:i|\*|l|!|1)(?:i|\*|l|!|1)(?:f|ph)"
    r"|n(?:a|\*|@)m(?:b|l3|i3)(?:i|\*|l|!|1)(?:a|\*|@)|n(?:a|\*|@)(?:w|vv)(?:a|\*|@)(?:s|\$|5|z|2)h(?:i|\*|l|!|1)"
    r"|n(?:a|\*|@)(?:s|\$|5|z|2)(?:i|\*|l|!|1)|n(?:e|\*|3)(?:g|6)r(?:o|\*|0)"
    r"|n(?:e|\*|3)(?:o|\*|0)n(?:a|\*|@)(?:s|\$|5|z|2)(?:i|\*|l|!|1)|n(?:i|\*|l|!|1)(?:g|6)(?:g|6)(?:a|\*|@)"
    r"|n(?:i|\*|l|!|1)(?:g|6)(?:g|6)(?:e|\*|3)r|n(?:i|\*|l|!|1)pp(?:i|\*|l|!|1)(?:e|\*|3)|n(?:u|\*|v)d(?:e|\*|3)"
    r"|n(?:u|\*|v)d(?:i|\*|l|!|1)(?:t|7)y|nymph(?:o|\*|0)|(?:o|\*|0)r(?:g|6)(?:a|\*|@)(?:s|\$|5|z|2)m"
    r"|(?:o|\*|0)r(?:g|6)y|p(?:a|\*|@)(?:c|k)(?:i|\*|l|!|1)"
    r"|p(?:a|\*|@)n(?:t|7)(?:i|\*|l|!|1)(?:e|\*|3)(?:s|\$|5|z|2)|p(?:a|\*|@)n(?:t|7)y|p(?:e|\*|3)d(?:o|\*|0)"
    r"|p(?:e|\*|3)n(?:i|\*|l|!|1)(?:s|\$|5|z|2)|p(?:i|\*|l|!|1)(?:s|\$|5|z|2)(?:s|\$|5|z|2)"
    r"|p(?:o|\*|0)(?:o|\*|0)(?:f|ph)|p(?:o|\*|0)(?:o|\*|0)n|p(?:o|\*|0)(?:o|\*|0)p|p(?:o|\*|0)rn"
    r"|p(?:t|7)h(?:c|k)|p(?:u|\*|v)(?:b|l3|i3)(?:e|\*|3)(?:s|\$|5|z|2)|p(?:u|\*|v)(?:s|\$|5|z|2)(?:s|\$|5|z|2)y"
    r"|(?:q|9)(?:u|\*|v)(?:e|\*|3)(?:a|\*|@)(?:f|ph)|(?:q|9)(?:u|\*|v)(?:e|\*|3)(?:e|\*|3)(?:f|ph)"
    r"|(?:q|9)(?:u|\*|v)(?:i|\*|l|!|1)m|r(?:a|\*|@)p(?:e|\*|3)|r(?:a|\*|@)p(?:i|\*|l|!|1)n(?:g|6)"
    r"|r(?:a|\*|@)p(?:i|\*|l|!|1)(?:s|\$|5|z|2)(?:t|7)|r(?:e|\*|3)(?:c|k)(?:t|7)(?:u|\*|v)m"
    r"|r(?:i|\*|l|!|1)mj(?:o|\*|0)(?:b|l3|i3)|(?:s|\$|5|z|2)&m"
    r"|(?:s|\$|5|z|2)(?:a|\*|@)d(?:i|\*|l|!|1)(?:s|\$|5|z|2)m|(?:s|\$|5|z|2)(?:c|k)(?:a|\*|@)(?:t|7)"
    r"|(?:s|\$|5|z|2)(?:c|k)h(?:i|\*|l|!|1)(?:o|\*|0)n(?:g|6)|(?:s|\$|5|z|2)(?:e|\*|3)m(?:e|\*|3)n"
    r"|(?:s|\$|5|z|2)(?:e|\*|3)x|(?:s|\$|5|z|2)(?:e|\*|3)x(?:o|\*|0)|(?:s|\$|5|z|2)(?:e|\*|3)xy"
    r"|(?:s|\$|5|z|2)h(?:e|\*|3)m(?:a|\*|@)(?:i|\*|l|!|1)(?:e|\*|3)|(?:s|\$|5|z|2)h(?:i|\*|l|!|1)(?:t|7)"
    r"|(?:s|\$|5|z|2)h(?:o|\*|0)(?:t|7)(?:a|\*|@)|(?:s|\$|5|z|2)(?:c|k)(?:e|\*|3)(?:e|\*|3)(?:t|7)"
    r"|(?:s|\$|5|z|2)(?:i|\*|l|!|1)(?:u|\*|v)(?:t|7)|(?:s|\$|5|z|2)m(?:u|\*|v)(?:t|7)"
    r"|(?:s|\$|5|z|2)n(?:a|\*|@)(?:t|7)(?:c|k)h|(?:s|\$|5|z|2)(?:o|\*|0)d(?:o|\*|0)my"
    r"|(?:s|\$|5|z|2)p(?:i|\*|l|!|1)(?:c|k)|(?:s|\$|5|z|2)p(?:i|\*|l|!|1)(?:o|\*|0)(?:o|\*|0)(?:g|6)(?:e|\*|3)"
    r"|(?:s|\$|5|z|2)p(?:o|\*|0)(?:o|\*|0)(?:g|6)(?:e|\*|3)|(?:s|\$|5|z|2)p(?:u|\*|v)n(?:c|k)"
    r"|(?:s|\$|5|z|2)(?:t|7)r(?:i|\*|l|!|1)p|(?:s|\$|5|z|2)(?:u|\*|v)(?:c|k)(?:c|k)|(?:t|7)(?:i|\*|l|!|1)(?:t|7)"
    r"|(?:t|7)r(?:a|\*|@)nny|(?:t|7)(?:u|\*|v)(?:s|\$|5|z|2)hy|(?:t|7)(?:w|vv)(?:a|\*|@)(?:t|7)"
    r"|(?:t|7)(?:w|vv)(?:i|\*|l|!|1)n(?:c|k)|(?:u|\*|v)r(?:e|\*|3)(?:t|7)hr(?:a|\*|@)"
    r"|(?:u|\*|v)(?:a|\*|@)(?:g|6)(?:i|\*|l|!|1)n(?:a|\*|@)|(?:u|\*|v)(?:o|\*|0)y(?:e|\*|3)(?:u|\*|v)r"
    r"|(?:u|\*|v)(?:u|\*|v)(?:i|\*|l|!|1)(?:u|\*|v)(?:a|\*|@)|(?:w|vv)(?:a|\*|@)n(?:c|k)"
    r"|(?:w|vv)h(?:o|\*|0)r(?:e|\*|3)|y(?:a|\*|@)(?:o|\*|0)(?:i|\*|l|!|1)|y(?:i|\*|l|!|1)(?:f|ph)(?:f|ph)y"
)

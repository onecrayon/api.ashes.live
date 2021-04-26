"""Configures the main FastAPI app and routes"""
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import views
from .environment import settings

__version__ = "2.0.0a2"

logging.basicConfig(level=logging.WARNING if not settings.debug else logging.DEBUG)

# Create our main application
app = FastAPI(
    title="Ashes.live API",
    description=(
        "Backend API for Ashes.live, a fan-developed deckbuilder "
        "and community website for Ashes Reborn."
    ),
    version=__version__,
    docs_url="/",
    redoc_url="/redoc",
)

# Setup CORS rules to ensure that we can access the API from our front-end apps
# We have to use the regex option, because for some reason the proper header isn't sent otherwise.
# This setup allows access from local development servers or the official Ashes.live domain
cors_regex = "https://([a-z0-9_-]+\.)?(ashes\.live|onrender\.com)"
if settings.env != "production":
    cors_regex = "https?://(localhost|192\.168\.\d+\.\d+):300[0-9]"

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=cors_regex,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup our application routes
app.include_router(views.health_check.router)
app.include_router(views.auth.router, prefix="/v2", tags=["auth"])
app.include_router(views.cards.router, prefix="/v2", tags=["cards"])
app.include_router(views.decks.router, prefix="/v2", tags=["decks"])
app.include_router(views.players.router, prefix="/v2", tags=["players"])
app.include_router(views.releases.router, prefix="/v2", tags=["releases"])

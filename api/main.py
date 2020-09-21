"""Configures the main FastAPI app and routes"""
import logging
from fastapi import FastAPI

from . import views
from .environment import settings

__version__ = "2.0.0a0"

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

# Setup our application routes
app.include_router(views.health_check.router)
app.include_router(views.auth.router, prefix="/v2", tags=["auth"])
app.include_router(views.cards.router, prefix="/v2", tags=["cards"])
app.include_router(views.players.router, prefix="/v2", tags=["players"])

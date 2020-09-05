"""Configures the main FastAPI app and routes"""
from fastapi import FastAPI

from . import views

__version__ = "2.0.0a0"

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
app.include_router(views.players.router, prefix="/v2", tags=["players"])

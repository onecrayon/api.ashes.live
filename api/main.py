"""Configures the main FastAPI app and routes"""
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from . import views
from .environment import settings

__version__ = "2.0.0a1"

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

# Include ProxyHeadersMiddleware to ensure that we use an HTTPS scheme even when we're behind proxies
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts='0.0.0.0')

# Setup CORS rules to ensure that we can access the API from our front-end apps
# We have to use the regex option, because for some reason the proper header isn't sent otherwise.
# This setup allows access from local development servers or the official Ashes.live domain
cors_regex = "https://([a-z0-9_-]+\.)?ashes\.live"
if settings.env != "production":
    cors_regex = "https?://localhost:300[0-9]"

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
app.include_router(views.players.router, prefix="/v2", tags=["players"])

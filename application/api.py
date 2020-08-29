"""Configures the main FastAPI app and routes

`app` is hoisted to the main application; e.g.:

    from application import app
"""
from fastapi import FastAPI

from . import views
from .environment import settings

# Create our main application
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

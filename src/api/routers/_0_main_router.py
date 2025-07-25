"""
Main API router.\n
This module defines the top-level API router that includes all sub-routers.
"""

# -- Imports

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from src.core.config import settings
from .auth import auth_router

# --

http_bearer = HTTPBearer(auto_error=False)

main_router = APIRouter(
    prefix=settings.api.prefix,
    dependencies=[Depends(http_bearer)],
)

main_router.include_router(auth_router)

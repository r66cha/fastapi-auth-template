"""
Main API router.\n
This module defines the top-level API router that includes all sub-routers.
"""

# -- Imports

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from src.core.config import settings
from .auth_db_bearer import auth_db_bearer_router
from .auth_db_cookie import auth_db_cookie_router
from .auth_jwt_bearer import auth_jwt_bearer_router
from .auth_jwt_cookie import auth_jwt_cookie_router
from .auth_refresh_jwt import refresh_router

# --

http_bearer = HTTPBearer(auto_error=False)

main_router_db_bearer = APIRouter(
    prefix=settings.api.prefix,
    dependencies=[Depends(http_bearer)],
)

main_router_db_bearer.include_router(auth_db_bearer_router)

# --

main_router_db_cookie = APIRouter(prefix=settings.api.prefix)
main_router_db_cookie.include_router(auth_db_cookie_router)

# --

main_router_jwt_bearer = APIRouter(
    prefix=settings.api.prefix,
    dependencies=[Depends(http_bearer)],
)
main_router_jwt_bearer.include_router(auth_jwt_bearer_router)
main_router_jwt_bearer.include_router(refresh_router)

# --

main_router_jwt_cookie = APIRouter(prefix=settings.api.prefix)
main_router_jwt_cookie.include_router(auth_jwt_cookie_router)
main_router_jwt_cookie.include_router(refresh_router)

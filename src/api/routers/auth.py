"""
Authentication router.

Defines routes for user authentication, registration, and related actions.
"""

# -- Imports

from fastapi import APIRouter
from src.api._0_fau import fastapi_users, authentication_backend
from src.core.config import settings
from src.core.schemas import UserRead, UserCreate

# --

auth_router = APIRouter(
    prefix=settings.api.auth,
    tags=["Auth"],
)

# Registration endpoint (/register)
auth_router.include_router(
    router=fastapi_users.get_register_router(
        user_schema=UserRead,
        user_create_schema=UserCreate,
    ),
)

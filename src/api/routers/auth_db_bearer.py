"""Authentication router with DB + Bearer."""

# -- Imports

from fastapi import APIRouter
from src.api._0_fau import fastapi_users_db_strategy, authentication_backend_db_bearer
from src.core.config import settings
from src.core.schemas import UserRead, UserCreate

# --

# Router instance
auth_db_bearer_router = APIRouter(
    prefix=settings.api.auth_db_bearer,
    tags=["Auth-DB-Bearer"],
)

# /register
auth_db_bearer_router.include_router(
    router=fastapi_users_db_strategy.get_register_router(
        user_schema=UserRead,
        user_create_schema=UserCreate,
    ),
)


# /login
# /logout
auth_db_bearer_router.include_router(
    router=fastapi_users_db_strategy.get_auth_router(
        backend=authentication_backend_db_bearer,
        # requires_verification=True,
    ),
)


# /request-verify-token
# /verify
auth_db_bearer_router.include_router(
    router=fastapi_users_db_strategy.get_verify_router(
        user_schema=UserRead,
    ),
)


# /forgot-password
# /reset-password
auth_db_bearer_router.include_router(
    router=fastapi_users_db_strategy.get_reset_password_router(),
)

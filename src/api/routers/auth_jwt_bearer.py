"""Authentication router with JWT + Bearer."""

# -- Imports

from fastapi import APIRouter
from src.api._0_fau import fastapi_users_jwt_strategy, authentication_backend_jwt_bearer
from src.core.config import settings
from src.core.schemas import UserRead, UserCreate

# --

# Router instance
auth_jwt_bearer_router = APIRouter(
    prefix=settings.api.auth_jwt_bearer,
    tags=["Auth-JWT-Bearer"],
)

# /register
auth_jwt_bearer_router.include_router(
    router=fastapi_users_jwt_strategy.get_register_router(
        user_schema=UserRead,
        user_create_schema=UserCreate,
    ),
)


# /login
# /logout
auth_jwt_bearer_router.include_router(
    router=fastapi_users_jwt_strategy.get_auth_router(
        backend=authentication_backend_jwt_bearer,
        # requires_verification=True,
    ),
)


# /request-verify-token
# /verify
auth_jwt_bearer_router.include_router(
    router=fastapi_users_jwt_strategy.get_verify_router(
        user_schema=UserRead,
    ),
)


# /forgot-password
# /reset-password
auth_jwt_bearer_router.include_router(
    router=fastapi_users_jwt_strategy.get_reset_password_router(),
)

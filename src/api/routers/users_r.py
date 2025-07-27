"""Users router /me"""

# -- Imports


from fastapi import APIRouter, Depends
from src.api._0_fau._0_fastapi_users import (
    fastapi_users_db_strategy,
    fastapi_users_jwt_strategy,
    current_active_user_db,
    current_active_user_jwt,
)
from src.core.schemas.user import UserRead, UserCreate
from src.core.config import settings


# --


user_router_db = APIRouter(
    prefix=settings.api.user,
    tags=["User-DB"],
)

user_router_jwt = APIRouter(
    prefix=settings.api.user,
    tags=["User-JWT"],
)


# -- User router DB

# /me
# /{id}
user_router_db.include_router(
    router=fastapi_users_db_strategy.get_users_router(
        UserRead,
        UserCreate,
    )
)


# -- User router JWT


# /me
# /{id}
user_router_jwt.include_router(
    router=fastapi_users_jwt_strategy.get_users_router(
        UserRead,
        UserCreate,
    )
)

"""FastAPI Users core setup."""

# -- Imports

from fastapi_users import FastAPIUsers
from src.core.database.models import User
from src.core.dependencies.user_manager_dep import get_user_manager
from src.api._0_fau.security.auth_back import (
    authentication_backend_db_bearer,
    authentication_backend_db_cookie,
    authentication_backend_jwt_bearer,
    authentication_backend_jwt_cookie,
)


# -- FastAPI Users DB

# FastAPIUsers instance db bearer and cookie
fastapi_users_db_strategy = FastAPIUsers[User, int](
    get_user_manager=get_user_manager,
    auth_backends=[
        authentication_backend_db_bearer,
        authentication_backend_db_cookie,
    ],
)


# Dependencies for user access db
current_active_user_db = fastapi_users_db_strategy.current_user(active=True)
current_active_superuser_db = fastapi_users_db_strategy.current_user(
    active=True,
    superuser=True,
)


# -- FastAPI Users DB JWT

# FastAPIUsers instance jwt bearer and cookie
fastapi_users_jwt_strategy = FastAPIUsers[User, int](
    get_user_manager=get_user_manager,
    auth_backends=[
        authentication_backend_jwt_bearer,
        authentication_backend_jwt_cookie,
    ],
)

# Dependencies for user access jwt
current_active_user_jwt = fastapi_users_jwt_strategy.current_user(active=True)
current_active_superuser_jwt = fastapi_users_jwt_strategy.current_user(
    active=True,
    superuser=True,
)

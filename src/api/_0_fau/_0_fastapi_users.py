"""FastAPI Users core setup."""

# -- Imports

from fastapi_users import FastAPIUsers
from src.core.database.models import User
from src.core.dependencies.user_manager_dep import get_user_manager
from src.api._0_fau.auth_back import authentication_backend

# --

# FastAPIUsers instance
fastapi_users = FastAPIUsers[User, int](
    get_user_manager=get_user_manager,
    auth_backends=[authentication_backend],
)

# -- Dependencies for user access

current_active_user = fastapi_users.current_user(active=True)
current_active_superuser = fastapi_users.current_user(active=True, superuser=True)

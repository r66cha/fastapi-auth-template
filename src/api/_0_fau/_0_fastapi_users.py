from fastapi_users import FastAPIUsers
from src.core.database.models.db_models import User
from src.core.dependencies.user_manager_dep import get_user_manager
from src.api.v1._0_fau.auth_back import authentication_backend

fastapi_users = FastAPIUsers[User, int](
    get_user_manager=get_user_manager,
    auth_backends=[authentication_backend],
)


current_active_user = fastapi_users.current_user(active=True)
current_active_superuser = fastapi_users.current_user(active=True, superuser=True)

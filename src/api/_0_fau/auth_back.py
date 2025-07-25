"""Authentication backend setup using FastAPI Users."""

# -- Imports

from fastapi_users.authentication import AuthenticationBackend
from src.api._0_fau.transport import bearer_transport
from src.core.dependencies.token_strategy_db_dep import get_database_strategy

# --

authentication_backend = AuthenticationBackend(
    name="access-token-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)

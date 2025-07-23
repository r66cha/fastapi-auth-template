from fastapi_users.authentication import AuthenticationBackend
from src.api.v1._0_fau.transport import bearer_transport
from src.core.dependencies.strategy_db_dep import get_database_strategy


authentication_backend = AuthenticationBackend(
    name="access-token-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)

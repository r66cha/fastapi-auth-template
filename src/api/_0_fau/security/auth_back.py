"""Authentication backend setup using FastAPI Users."""

# -- Imports

from fastapi_users.authentication import AuthenticationBackend
from src.api._0_fau.security.transport import bearer_transport, cookie_transport
from src.core.dependencies.token_strategy_db_dep import get_database_strategy
from src.core.dependencies.token_strategy_jwt_dep import get_jwt_strategy

# -- DB strategy

# Database-backed access token strategy + bearer
authentication_backend_db_bearer = AuthenticationBackend(
    name="access-token-db-bearer",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)

# Database-backed access token strategy + cookie
authentication_backend_db_cookie = AuthenticationBackend(
    name="access-token-db-cookie",
    transport=cookie_transport,
    get_strategy=get_database_strategy,
)

# -- JWT strategy

# JWT strategy + bearer
authentication_backend_jwt_bearer = AuthenticationBackend(
    name="access-token-jwt-bearer",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


# JWT strategy + cookie
authentication_backend_jwt_cookie = AuthenticationBackend(
    name="access-token-jwt-cookie",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

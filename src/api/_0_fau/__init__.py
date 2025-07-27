"""FastaAPI Users core module"""

# -- Imports

from ._0_fastapi_users import fastapi_users_db_strategy, fastapi_users_jwt_strategy
from .security.auth_back import (
    authentication_backend_db_bearer,
    authentication_backend_db_cookie,
    authentication_backend_jwt_bearer,
    authentication_backend_jwt_cookie,
)
from .security.transport import bearer_transport

# --

__all__ = [
    "fastapi_users_db_strategy",
    "fastapi_users_jwt_strategy",
    "authentication_backend_db_bearer",
    "authentication_backend_db_cookie",
    "authentication_backend_jwt_bearer",
    "authentication_backend_jwt_cookie",
    "bearer_transport",
]

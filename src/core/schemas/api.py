"""Schema configuration for constructing API endpoint paths."""

# -- Imports

from pydantic import BaseModel


# --


class ApiSchema(BaseModel):
    """Configuration schema for base API endpoints."""

    prefix: str = "/api"
    auth: str = "/auth"

    auth_db_bearer: str = "/auth/db/bearer"
    auth_db_cookie: str = "/auth/db/cookie"
    auth_jwt_bearer: str = "/auth/jwt/bearer"
    auth_jwt_cookie: str = "/auth/jwt/cookie"

    users: str = "/users"

    @property
    def login_url(self) -> str:
        """Full login route path constructed from base prefixes.

        Returns:
            str: Complete URL path to the login endpoint."""

        return f"{self.prefix}{self.auth_jwt_cookie}/login"  # Choose your path

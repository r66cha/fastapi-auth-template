"""Schema configuration for constructing API endpoint paths."""

# -- Imports

from pydantic import BaseModel


# --


class ApiSchema(BaseModel):
    """Configuration schema for base API endpoints."""

    prefix: str = "/api"
    auth: str = "/auth"
    users: str = "/users"

    @property
    def login_url(self) -> str:
        """Full login route path constructed from base prefixes.

        Returns:
            str: Complete URL path to the login endpoint."""

        return f"{self.prefix}{self.auth}/login"

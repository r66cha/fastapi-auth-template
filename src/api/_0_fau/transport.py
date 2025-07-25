"""
Authentication transport configurations for FastAPI Users.

This module defines multiple transport mechanisms used for delivering authentication tokens:
- Bearer transport (header-based)
- Cookie transport (session-style, frontend friendly)
"""

# -- Imports

from fastapi_users.authentication import (
    BearerTransport,
    CookieTransport,
)
from src.core.config import settings

# --

bearer_transport = BearerTransport(
    tokenUrl=settings.api.login_url  # URL to obtain token via /auth/login
)


cookie_transport = CookieTransport(
    cookie_name="access_token",  # Name of the cookie
    cookie_max_age=3600,  # Lifetime in seconds
    cookie_secure=False,  # Use True in production with HTTPS
    cookie_httponly=True,  # Prevent JS access to cookie
    cookie_samesite="lax",  # CSRF protection
)

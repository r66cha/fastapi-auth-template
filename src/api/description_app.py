title = "FastAPI Auth Template"
description = """
A universal FastAPI authorization template based on the core of the **FastAPI Users** library.

### Authentication strategies:
- **JWT** — storing access tokens in memory (without database)
- **Database (DB)** — storing access tokens in a database with the possibility of revocation

### Token transport methods:
- **Bearer** — token passed in `Authorization: Bearer <token>` header
- **Cookies** — secure `HttpOnly` cookies for frontend token storage

### Protocol integrations (under development):
- **OAuth2 / OpenID Connect** — external provider authentication (Google, Yandex, etc.)

### Main components:
- `fastapi-users` — user management core
- `sqlalchemy` — ORM models for users and tokens
- `alembic` — database schema migrations
- Extensible classes `User`, `AccessToken` and `RefreshToken`
- Asynchronous `UserManager` with custom logic

### Features:
- Registration, login, logout
- Email verification
- Password reset
- Handling `access` and `refresh` tokens
- Support for custom dependencies and strategies

### Purpose:
- Base module for all authentication types
- Ready for MVPs, pet projects, and production use
"""

version = "1.0.0"
contact = {
    "name": "r66cha",
    "url": "https://github.com/r66cha/fastapi-auth-template.git",
}

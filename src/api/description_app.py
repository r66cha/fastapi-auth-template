title = "FastAPI Auth Template"
description = """
A universal FastAPI authorization template based on the core of the **FastAPI Users** library.

### Authentication strategies:
- **JWT** — storing access tokens in memory (without database)
- **Database (DB)** — storing access tokens in a database with the possibility of revocation

### Transports:
- **Bearer** — header `Authorization: Bearer <token>`
- **Cookies** — secure `HttpOnly` cookies for frontend
- **OAuth2** (under development) — integration with Google, Yandex and other providers

### Main components:
- `fastapi-users` — user management core
- `sqlalchemy` — ORM model of users and tokens
- `alembic` — database schema migrations
- Extensible classes `User` and `AccessToken`
- Asynchronous `UserManager' with custom logic

### Features:
- Registration, Login (entry), Logout (exit)
- Email verification
- Reset password
- Working with `access` and `refresh` tokens
- Support for custom dependencies and strategies

### Purpose:
- Used as a basic module for all types of authentication
- Ready for use in MVP, pet projects and production
"""

version = "1.0.0"
contact = {
    "name": "r66cha",
    "url": "https://github.com/r66cha/fastapi-auth-template.git",
}

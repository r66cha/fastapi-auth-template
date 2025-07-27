# 🚀 FastAPI Auth Template

**FastAPI Auth Template** is a universal authentication template for FastAPI, based on the core of the [FastAPI Users](https://github.com/fastapi-users/fastapi-users) library.

Suitable for MVPs, pet projects, and production-ready systems with flexible strategies, token transport methods, and extendable models.

---

## Features

### Authentication Strategies

- **JWT** — stateless access tokens (in-memory)
- **Database (DB)** — persistent access tokens with revocation support

### Token Transport Methods

- **Bearer** — via `Authorization: Bearer <token>` header
- **Cookies** — secure `HttpOnly` cookies (frontend-friendly)

### Protocol Integration (planned)

- **OAuth2 / OpenID Connect** — external authentication via Google, Yandex, etc.

---

## Core Stack

- `fastapi` — main framework
- `fastapi-users` — user management framework
- `sqlalchemy` — ORM for users and tokens
- `alembic` — schema migrations
- `asyncpg` — async PostgreSQL driver
- Extendable models: `User`, `AccessToken`, `RefreshToken`
- Async `UserManager` with custom logic support

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/r66cha/fastapi-auth-template.git
cd fastapi-auth-template
```

### 2. Install uv package manager

```bash
make install-uv
```

### 3. Install project dependencies

```bash
make install-req
```

### 4. Apply database migrations

```bash
make alembic-upgrade
```

### 5. (Optional) Create initial superuser

```bash
make superuser
```

### 6. Run the project

- with uvicorn (development)

```bash
make urun
```

- with gunicorn

```bash
make run
```

### 7. Swagger docs available at:

- http://localhost:8000/docs

---

## License

No License.

## Author

r66cha

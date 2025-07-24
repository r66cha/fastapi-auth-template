"""
Database models for user and access token management using FastAPI Users.

This module defines the ORM models required for authentication and user handling:
- `Base`: Declarative base for all ORM models.
- `User`: Model for storing user data.
- `AccessToken`: Model for storing access tokens (used in DB strategy).
"""

# Imports from the fastapi-users library for working with users and tokens
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)

# SQLAlchemy imports for asynchronous DATABASE work
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession

# Imports from the standard library
from typing import TYPE_CHECKING, Annotated

# Internal project mixin for adding an id field
from src.core.database.mixin import IdIntPkMixin

# Import for type annotation inside a conditional block
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


# --


class Base(DeclarativeBase):
    """The basic declarative class for all ORM models of the project."""

    pass


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    """User database model."""

    __tablename__ = "users"

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        """Returns an instance of SQLAlchemyUserDatabase for working with the user's model."""

        return SQLAlchemyUserDatabase(session, cls)


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[int]):
    """Access token model linked to a user."""

    __tablename__ = "accesstokens"

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False,
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        """Returns an instance of SQLAlchemyAccessTokenDatabase for working with the access token table."""

        return SQLAlchemyAccessTokenDatabase(session, cls)

"""
Database manager module for configuring SQLAlchemy async engine and session.

This module sets up the database connection using an asynchronous SQLAlchemy engine.
It provides:
- `DatabaseManager`: A class to manage async session creation.
- `db_manager`: A default instance initialized from the project config.
"""

# -- Imports

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
)
from collections.abc import AsyncGenerator
from .config import db_url


# --


class DatabaseManager:
    """Manages async engine and session for database operations."""

    def __init__(self, db_url: str):
        self.engine: AsyncEngine = create_async_engine(db_url)
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Asynchronously returns the database connection session.

        Uses sessionmaker to create an asynchronous SQLAlchemy session.
        The session is automatically closed at the end of the usage block.

        Yields:
            AsyncSession: An active asynchronous session for working with the database.
        """

        async with self.session_factory() as session:
            yield session


db_manager = DatabaseManager(db_url=db_url.get_DB_URL)


__all__ = ["db_manager"]

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
)
from collections.abc import AsyncGenerator
from .config import db_url


class DatabaseManager:
    def __init__(self, db_url: str):
        self.engine: AsyncEngine = create_async_engine(db_url)
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_manager = DatabaseManager(db_url=db_url.get_DB_URL)


__all__ = ["db_manager"]

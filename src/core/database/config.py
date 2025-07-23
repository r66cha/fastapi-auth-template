from pydantic_settings import BaseSettings, SettingsConfigDict
from src.core.schemas import DB_URL_Schema
from enum import Enum


class DatabaseDialect(BaseSettings):
    postgres_asyncpg = "postgres+asynchpg"


class DB_URL(BaseSettings, DB_URL_Schema, DatabaseDialect):
    @property
    def get_DB_URL(self) -> str:
        return f"{self.postgres_asyncpg}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}"


db_url = DB_URL()


__all__ = ["db_url"]

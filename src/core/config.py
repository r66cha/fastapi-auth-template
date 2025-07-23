from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.core.schemas import (
    DatabaseConfigSchema,
    ApiSchema,
    LoggingConfigSchema,
    RunConfigSchema,
    AccessTokenSchema,
    GunicornConfigSchema,
)


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=(BASE_DIR / ".env.template"),  # override in .env
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )

    db: DatabaseConfigSchema = DatabaseConfigSchema()
    api: ApiSchema = ApiSchema()
    access_token: AccessTokenSchema = AccessTokenSchema()
    logging: LoggingConfigSchema = LoggingConfigSchema()
    run: RunConfigSchema = RunConfigSchema()
    gunicorn: GunicornConfigSchema = GunicornConfigSchema()


settings = Settings()

__all__ = ["settings"]

from pydantic_settings import BaseSettings, SettingsConfigDict


class DB_URL(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    dialect: str = "postgres+asynchpg"

    model_config = SettingsConfigDict(
        env_file=".env.template",
        extra="ignore",
    )

    @property
    def get_DB_URL(self) -> str:
        return f"{self.dialect}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}"


db_url = DB_URL()


__all__ = ["db_url"]

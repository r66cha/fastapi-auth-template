from pydantic_settings import BaseSettings


class DB_URL_Schema(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

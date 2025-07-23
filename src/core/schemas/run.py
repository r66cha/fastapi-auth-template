from pydantic import BaseModel


class RunConfigSchema(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class GunicornConfigSchema(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 1
    timeout: int = 900

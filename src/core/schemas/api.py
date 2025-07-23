from pydantic import BaseModel


class ApiSchema(BaseModel):
    prefix: str = "/api"
    auth: str = "/auth"
    users: str = "/users"

    @property
    def login_url(self) -> str:
        return f"{self.prefix}{self.auth}/login"

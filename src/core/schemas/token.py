from pydantic import BaseModel


class AccessTokenSchema(BaseModel):
    lifetime_second: int = 3000
    reset_password_token_secret: str
    verification_token_secret: str

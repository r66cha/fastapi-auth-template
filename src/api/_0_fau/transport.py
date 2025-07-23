from fastapi_users.authentication import BearerTransport
from src.core.config import settings

bearer_transport = BearerTransport(tokenUrl=settings.api.login_url)

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from src.core.config import settings


http_bearer = HTTPBearer(auto_error=False)

main_router = APIRouter(
    prefix=settings.api.prefix,
    dependencies=[Depends(http_bearer)],
    # description="some description",
)

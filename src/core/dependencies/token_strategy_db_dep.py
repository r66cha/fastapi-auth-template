from typing import Annotated, TYPE_CHECKING
from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy
from src.core.dependencies.token_db_dep import get_access_token_db
from src.core.config import settings

if TYPE_CHECKING:
    from src.core.database.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase


def get_database_strategy(
    access_token_db: Annotated[
        "AccessTokenDatabase[AccessToken]",
        Depends(get_access_token_db),
    ],
):
    return DatabaseStrategy(
        database=access_token_db,
        lifetime_seconds=settings.access_token.lifetime_second,
    )

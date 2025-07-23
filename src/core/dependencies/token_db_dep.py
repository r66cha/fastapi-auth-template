from fastapi import Depends
from typing import Annotated, TYPE_CHECKING

from core.database.manager import db_manager
from src.core.database.models import AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_token_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_manager.get_session),
    ],
):
    yield AccessToken.get_db(session=session)

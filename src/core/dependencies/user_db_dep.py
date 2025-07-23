from fastapi import Depends
from typing import TYPE_CHECKING, Annotated

from core.database.manager import db_manager
from src.core.database.models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_manager.get_session),
    ],
):
    yield User.get_db(session=session)

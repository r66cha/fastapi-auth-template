"""Dependency for retrieving the AccessToken database adapter."""

# -- Imports

from fastapi import Depends
from typing import Annotated, TYPE_CHECKING
from src.core.database.manager import db_manager
from src.core.database.models import AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


# --


async def get_access_token_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_manager.get_session),
    ],
):
    """
    Dependency function that yields an access token database adapter.

    Args:
        session (AsyncSession): An async SQLAlchemy session provided via dependency injection.

    Yields:
        SQLAlchemyAccessTokenDatabase: Adapter for working with access tokens in the DB strategy.
    """

    yield AccessToken.get_db(session=session)

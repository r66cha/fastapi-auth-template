"""JWT Refresh Token for FastAPI Users."""

# -- Imports

import secrets
from enum import Enum
from datetime import timedelta, datetime, timezone

from fastapi import APIRouter, HTTPException, Response, Query, status, Depends, Cookie
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from src.core.database.manager import db_manager
from src.core.database.models import RefreshToken, User
from src.api._0_fau._0_fastapi_users import current_active_user_jwt
from src.api._0_fau.security.token import create_access_token
from src.core.config import settings


# -- Router


refresh_router = APIRouter(
    prefix="/auth/refresh",
    tags=["Auth-JWT-Refresh"],
)


# --


@refresh_router.post("/issue", summary="Issue refresh token")
async def issue_refresh_token(
    response: Response,
    user: User = Depends(current_active_user_jwt),
    session: AsyncSession = Depends(db_manager.get_session),
):
    """
    Issues a secure refresh token after successful login.
    Stores token in DB and sets it in HTTP-only cookie.
    """

    refresh_token = secrets.token_urlsafe(64)
    expires_at = datetime.now(tz=timezone.utc) + timedelta(days=30)  # Set in settings

    token_db = RefreshToken(
        token=refresh_token,
        user_id=user.id,
        expires_at=expires_at,
    )

    await session.execute(delete(RefreshToken).where(RefreshToken.user_id == user.id))
    session.add(token_db)
    await session.commit()

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        max_age=30 * 24 * 60 * 60,
        samesite="lax",
        secure=False,  # Set True in production
    )

    return {"msg": "Refresh token issued"}


class TokenTransport(str, Enum):
    cookie = "cookie"
    bearer = "bearer"


@refresh_router.post("/access", summary="Get new access token using refresh token")
async def get_new_access_token(
    response: Response,
    refresh_token: str = Cookie(default=None),
    transport: TokenTransport = Query(default=TokenTransport.cookie),
    session: AsyncSession = Depends(db_manager.get_session),
):
    """Generates a new access token using a valid refresh token from cookies."""

    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token missing",
        )

    query = await session.execute(
        select(RefreshToken).where(RefreshToken.token == refresh_token)
    )

    token_row = query.first()

    if not token_row:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    token_data: RefreshToken = token_row[0]

    if datetime.now(tz=timezone.utc) > token_data.expires_at:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token expired",
        )

    user_query = await session.execute(
        select(User)
        .join(
            RefreshToken,
            User.id == RefreshToken.user_id,
        )
        .where(RefreshToken.token == refresh_token)
    )
    user = user_query.scalar_one_or_none()

    new_access_token = await create_access_token(user=user)

    if transport == TokenTransport.cookie:

        response.set_cookie(
            key="access_token",
            value=new_access_token,
            httponly=True,
            max_age=settings.access_token.lifetime_second,
            secure=False,  # Set True in production
        )

        return {
            "message": "Access token set in HttpOnly cookie",
            "token_type": "cookie",
        }

    elif transport == TokenTransport.bearer:
        response.headers["Authorization"] = f"Bearer {new_access_token}"

        return {
            "access_token": new_access_token,
            "token_type": "bearer",
        }

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid transport type",
        )


@refresh_router.post("/revoke", summary="Logout and delete refresh token")
async def revoke_refresh_token(
    response: Response,
    refresh_token: str = Cookie(default=None),
    session: AsyncSession = Depends(db_manager.get_session),
):
    """Deletes the refresh token from DB and removes cookie."""

    if refresh_token:
        result = await session.execute(
            select(RefreshToken).where(RefreshToken.token == refresh_token)
        )
        db_refresh_token = result.scalar_one_or_none()

        if db_refresh_token:
            await session.execute(
                delete(RefreshToken).where(RefreshToken.token == refresh_token)
            )
            await session.commit()

    response.delete_cookie("refresh_token")

    return {"msg": "Refresh token revoked"}

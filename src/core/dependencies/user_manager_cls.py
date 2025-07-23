from typing import Optional, TYPE_CHECKING

from fastapi_users import BaseUserManager, IntegerIDMixin

from src.core.database.models import User
from src.core.settings.log_conf import log

if TYPE_CHECKING:
    from fastapi import Request


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = "SECRET"
    verification_token_secret = "SECRET"

    async def on_after_register(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        "After user registration func"

        log.info(f"User: {user.id} was registered")

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        "After user request verification func"

        log.info(f"Verification request from:\n\tUser: {user.id}\n\tToken: {token}")

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        "After user forgot password func"

        log.info(f"User {user.id} has forgot their password. Reset token: {token}")

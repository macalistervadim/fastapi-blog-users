from collections.abc import AsyncGenerator

from fastapi import Depends
from fastapi_users import BaseUserManager, IntegerIDMixin
from fastapi_users.db import SQLAlchemyUserDatabase

from src.core.config import settings
from src.db.session import get_user_db
from src.models.users import User


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    user_db_model = User
    reset_password_token_secret: str = settings.USERS_SECRET_KEY
    verification_token_secret: str = settings.USERS_SECRET_KEY


async def get_user_manager(
    user_db: SQLAlchemyUserDatabase = Depends(get_user_db),
) -> AsyncGenerator[UserManager]:
    yield UserManager(user_db)

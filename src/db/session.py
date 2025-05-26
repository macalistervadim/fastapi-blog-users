from collections.abc import AsyncGenerator
from typing import Any

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from models.users import User
from src.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, Any]:
    async with AsyncSessionLocal() as session:
        yield session


async def get_user_db(
    session: AsyncSession = Depends(get_db),
) -> SQLAlchemyUserDatabase:
    return SQLAlchemyUserDatabase(session, User)

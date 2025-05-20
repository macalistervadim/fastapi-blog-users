from typing import Any

from fastapi import APIRouter

from src.schemas.users import UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


def get_users_router(fastapi_users: Any) -> APIRouter:
    router.include_router(
        fastapi_users.get_users_router(UserRead, UserUpdate),
    )
    return router

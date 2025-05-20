from typing import Any

from fastapi import APIRouter

from src.schemas.users import UserCreate, UserRead

router = APIRouter(tags=["auth"])


def get_auth_router(fastapi_users: Any, auth_backend: Any) -> APIRouter:
    router.include_router(
        fastapi_users.get_auth_router(auth_backend),
    )
    router.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
    )
    return router

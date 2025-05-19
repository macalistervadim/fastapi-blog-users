from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)

from schemas.users import UserCreate, UserRead
from src.api.v1 import users
from src.models.users import User
from src.utils.get_user_manager import get_user_manager

app = FastAPI()


cookie_transport = CookieTransport(cookie_name="biscuit", cookie_max_age=3600)
auth_backend: AuthenticationBackend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=lambda: JWTStrategy(secret="SECRET", lifetime_seconds=3600),
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(users.router, prefix="/v1")

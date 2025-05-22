from fastapi_users import FastAPIUsers

from src.core.auth import get_auth_backend
from src.models.users import User
from src.utils.get_user_manager import get_user_manager


def get_fastapi_users() -> FastAPIUsers[User, int]:
    return FastAPIUsers[User, int](
        get_user_manager,
        [get_auth_backend()],
    )

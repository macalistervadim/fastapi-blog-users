from fastapi import FastAPI

from src.api.v1 import auth, users
from src.core.auth import get_auth_backend
from src.core.middleware import setup_middlewares
from src.core.users import get_fastapi_users

app = FastAPI()

# middlewares
setup_middlewares(app)

# components
fastapi_users = get_fastapi_users()
auth_backend = get_auth_backend()

# routers
app.include_router(
    auth.get_auth_router(fastapi_users, auth_backend),
    prefix="/auth",
)
app.include_router(
    users.get_users_router(fastapi_users),
    prefix="/users",
)

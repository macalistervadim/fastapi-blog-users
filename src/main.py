from fastapi import FastAPI

from src.api.v1 import users

app = FastAPI()


app.include_router(users.router, prefix="/v1")

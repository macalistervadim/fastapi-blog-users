import os
from typing import Annotated

from pydantic import PlainValidator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # database
    DATABASE_URL: str

    # auth
    USERS_SECRET_KEY: str
    JWT_LIFETIME_SECONDS: int = 3600
    COOKIE_NAME: str = "biscuit"
    COOKIE_MAX_AGE: int = 3600
    COOKIE_SECURE: bool = False
    COOKIE_HTTPONLY: bool = True
    COOKIE_SAMESITE: str = "lax"

    # cors
    CORS_ORIGINS: Annotated[
        list[str],
        PlainValidator(
            lambda v: [i.strip() for i in v.split(",")]
            if isinstance(v, str)
            else v,
        ),
    ]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: Annotated[
        list[str],
        PlainValidator(
            lambda v: [i.strip() for i in v.split(",")]
            if isinstance(v, str)
            else v,
        ),
    ] = ["*"]
    CORS_ALLOW_HEADERS: Annotated[
        list[str],
        PlainValidator(
            lambda v: [i.strip() for i in v.split(",")]
            if isinstance(v, str)
            else v,
        ),
    ] = ["*"]

    class Config:
        env_file = os.environ.get("ENV_FILE", ".env")
        extra = "ignore"


settings = Settings()  # type: ignore

import os

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
    CORS_ORIGINS: list[str]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str]
    CORS_ALLOW_HEADERS: list[str]

    class Config:
        env_file = os.environ.get("ENV_FILE", ".env")
        extra = "ignore"


settings = Settings()  # type: ignore

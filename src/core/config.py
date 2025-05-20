import os

from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # database
    DATABASE_URL: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = "database"
    POSTGRES_PORT: int = 5432

    # auth
    USERS_SECRET_KEY: str
    JWT_LIFETIME_SECONDS: int = 3600
    COOKIE_NAME: str = "biscuit"
    COOKIE_MAX_AGE: int = 3600
    COOKIE_SECURE: bool = False
    COOKIE_HTTPONLY: bool = True
    COOKIE_SAMESITE: str = "lax"

    # cors
    CORS_ORIGINS: list[str] = ["http://localhost:8000", "http://localhost"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ["*"]
    CORS_ALLOW_HEADERS: list[str] = ["*"]

    @field_validator(
        "CORS_ORIGINS",
        "CORS_ALLOW_METHODS",
        "CORS_ALLOW_HEADERS",
        mode="before",
    )
    def split_str_to_list(self: "Settings", v: str) -> list[str] | str:
        if isinstance(v, str):
            return [item.strip() for item in v.split(",")]
        return v

    class Config:
        env_file = os.environ.get("ENV_FILE", ".env.local")
        extra = "ignore"


settings = Settings()  # type: ignore

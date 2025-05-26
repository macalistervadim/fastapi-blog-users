from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)

from src.core.config import settings

cookie_transport = CookieTransport(
    cookie_name=settings.COOKIE_NAME,
    cookie_max_age=settings.COOKIE_MAX_AGE,
    cookie_secure=settings.COOKIE_SECURE,
    cookie_httponly=settings.COOKIE_HTTPONLY,
    cookie_samesite=settings.COOKIE_SAMESITE.lower(),  # type: ignore
)


def get_auth_backend() -> AuthenticationBackend:
    return AuthenticationBackend(
        name="jwt",
        transport=cookie_transport,
        get_strategy=lambda: JWTStrategy(
            secret=settings.USERS_SECRET_KEY,
            lifetime_seconds=settings.JWT_LIFETIME_SECONDS,
        ),
    )

from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from app.core.config import settings

APP_ENV = settings.APP_ENV

# disable if APP_ENV is development
IS_LIMITER_ENABLED = APP_ENV != "development"

limiter = Limiter(
    key_func=get_remote_address,
    enabled=IS_LIMITER_ENABLED
)

def init_limiter(app: FastAPI):
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

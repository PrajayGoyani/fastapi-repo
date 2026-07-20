import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta, timezone

from app.models.user import User

from app.core.exceptions import AppException
from app.core.config import settings

JWT_SECRET = settings.JWT_SECRET
JWT_ALG = settings.JWT_ALG
JWT_EXPIRE_MIN = settings.JWT_EXPIRE_MIN

def create_access_token(user: User) -> str:
    now = datetime.now(timezone.utc)
    # nbf = now + 3600 # not before
    exp = now + timedelta(minutes=JWT_EXPIRE_MIN)

    payload = {
        "sub": str(user.id),
        "username": user.username,
        "iat": int(now.timestamp()),
        "exp": int(exp.timestamp()),
        # "aud": "", # can be string or []string
        # "nbf": int(nbf.timestamp()),
    }

    return jwt.encode(
        payload,
        key=JWT_SECRET,
        algorithm=JWT_ALG,
    )

def validate_access_token(token: str):
    try:
        return jwt.decode(
            token,
            key=JWT_SECRET,
            algorithms=[JWT_ALG],
        )
    except ExpiredSignatureError:
        raise AppException.unauthorised("Token has expired")
    except InvalidTokenError:
        raise AppException.unauthorised("Token invalid")
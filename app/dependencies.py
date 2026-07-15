from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.exceptions import AppException
from app.core.security import validate_access_token
# from app.services.user_service import get_user_by_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = validate_access_token(token)

    # Optional: fetch user from DB
    # user = user_service.get_by_id(payload["sub"])
    # if not user:
    #     raise AppException.unauthorized("Invalid access token")

    return payload
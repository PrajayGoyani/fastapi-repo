import logging
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.core.exceptions import AppException
from app.core.security import create_access_token

logger = logging.getLogger(__name__)

def register(username: str, password: str):
    db: Session = next(get_db())
    # check if user already exist with username
    user: User = db.scalar(select(User).where(User.username == username))
    if user:
        raise AppException.conflict("User already exists.")

    # save user data
    db_user = User(
        username=username
    )
    db_user.hash_password(password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    jwt: str = issue_jwt(db_user)

    return {
        "message": "User registered!",
        "data": {
            "access_token": jwt,
            "user": {
                "id": user.id,
                "username": user.username,
            }
        }
    }
    
    return { "message": "User registered!", "data": { "username": db_user.username } }


def login(username: str, password: str):
    db: Session = next(get_db())
    user: User = db.scalar(select(User).where(User.username == username))

    if not user or not user.verify_password(password):
        logger.warning(
            "Authentication failed",
            extra={"username_attempted": username, "reason": "invalid_credentials"}
        )
        raise AppException.unauthorised("Invalid username or password")
    
    jwt: str = issue_jwt(user)

    logger.info("User authenticated successfully", extra={"user_id": user.id})

    return {
        "message": "User logged in!",
        "data": {
            "access_token": jwt,
            "user": {
                "id": user.id,
                "username": user.username,
            }
        }
    }

def issue_jwt(user: User):
    # issue jwt token
    jwt: str = create_access_token(user)
    return jwt






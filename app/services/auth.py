from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.core.exceptions import AppException
from app.core.security import create_access_token

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
    
    return { "message": "User registered!", "data": { "username": db_user.username } }


def login(username: str, password: str):
    db: Session = next(get_db())
    user: User = db.scalar(select(User).where(User.username == username))

    if not user:
        raise AppException.unauthorised("Invalid username or password")

    if not user.verify_password(password):
        raise AppException.unauthorised("Invalid username or password")
    
    # issue jwt token
    jwt: str = create_access_token(user)

    return {
        "message": "User login successfully!",
        "data": {
            "access_token": jwt,
            "user": {
                "id": user.id,
                "username": user.username,
            }
        }
    }






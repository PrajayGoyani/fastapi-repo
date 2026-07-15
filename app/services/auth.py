

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from datetime import datetime, timedelta, timezone


def register(username: str, password: str, db: Session = Depends(get_db)):
    # check if user already exist with username
    user: User = db.scalar(select(User).where(User.username == username))
    if user:
        raise Exception("User already exists.")

    # save user data
    db_user = User(
        username=username
    )
    db_user.save_password_hash(password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return { "message": "User registered!", "data": { "user": db_user } }

JWT_SECRET = "hagggw752"
JWT_ALG = "HS256"
JWT_EXPIRE_MIN = 60

def create_access_token(subject: str) -> str:
    now = datetime.now(timezone.utc)
    exp = now + timedelta(minutes=JWT_EXPIRE_MIN)
    payload = {"sub": subject, "iat": int(now.timestamp()), "exp": int(exp.timestamp())}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)

def login(username: str, password: str, db: Session = Depends(get_db)):
    user: User = db.scalar(select(User).where(User.username == username))

    if not user:
        raise Exception("Invalid user name or password")

    if not user.verify_password(password):
        raise Exception("Invalid user name or password")
    
    # issue jwt token
    jwt = ""

    return {
        "access_token": jwt,
        "message": "User login successfully!", "data": { "user": user }
    }






from app.models.user import User
from sqlalchemy import select
from app.database import get_db

def get_by_id(id: str):
    db = next(get_db())
    user = db.execute(
        select(User.id, User.username).where(User.id == int(id))
    ).mappings().one_or_none()
    return user
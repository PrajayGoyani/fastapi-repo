
from typing_extensions import deprecated

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@deprecated("Now managed by alembic migration")
def init_db():
    # Create database tables (if they don't exist)
    Base.metadata.create_all(bind=engine)

# DB injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

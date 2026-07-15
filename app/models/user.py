from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended() #argon2

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=True, server_default=func.now())

    def verify_password(self, plain_password: str) -> bool:
        """Verifies a plain-text password against a stored hash."""
        try:
            return password_hash.verify(plain_password, self.hashed_password)
        except Exception:
            return False
    
    def hash_password(self, plain_password: str) -> None:
        """Generates a secure hash from a plain-text password."""
        self.hashed_password = password_hash.hash(plain_password)
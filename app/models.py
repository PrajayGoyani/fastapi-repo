from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, func
from app.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    is_offer = Column(Boolean, default=None, nullable=True)
    created_at = Column(DateTime, nullable=True, server_default=func.now()) # default=func.now()

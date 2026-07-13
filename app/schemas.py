from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ItemBase(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    name: str | None = None
    price: float | None = None

class ItemResponse(ItemBase):
    id: int
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

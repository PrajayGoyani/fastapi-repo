from pydantic import BaseModel, ConfigDict

class ItemBase(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Any
from enum import Enum

class ItemBase(BaseModel):
    name: str
    price: float = Field(gt=0, description="Must be positive")
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

class JobStatus(str, Enum):
    QUEUED = "queued"
    PROCESSING = "processing"
    DONE = "done"

class IngestResponse(BaseModel):
    job_id: str
    status: JobStatus

class ResultResponse(BaseModel):
    job_id: str
    status: JobStatus
    result: Any

class Event(BaseModel):
    user_id: int
    value: float

class User(BaseModel):
    username: str
    hashed_password: str
    created_at: datetime | None = None
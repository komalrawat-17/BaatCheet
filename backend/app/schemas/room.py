from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional


class RoomBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_private: bool = False


class RoomCreate(RoomBase):
    pass


class RoomResponse(RoomBase):
    id: UUID
    created_by: Optional[UUID] = None
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

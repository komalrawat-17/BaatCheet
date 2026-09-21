from uuid import UUID
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.user import UserResponse


class MessageBase(BaseModel):
    content: str


class MessageCreate(MessageBase):
    room_id: UUID


class MessageResponse(MessageBase):
    id: UUID
    room_id: UUID
    sender_id: UUID
    created_at: datetime
    sender: Optional[UserResponse] = None

    model_config = ConfigDict(from_attributes=True)

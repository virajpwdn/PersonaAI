from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class MessageInput(BaseModel):
    """Schema for user message input"""
    user_id: UUID
    pesona_id: UUID
    message: str
    role: str

class MessageResponse(BaseModel):
    """Schema for graph response"""
    # thread_id: str
    # connection_id: UUID
    # user_id: UUID
    response: str = ""
    enhanched: str = ""
    memory: str = ""
    checkpoint_id: Optional[str] = None
        
class ConnectResponse(BaseModel):
    id: UUID
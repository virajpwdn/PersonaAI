from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    password: str

class UserResponse(BaseModel):
    id: UUID
    # email: str
    username: str
    first_name: str
    last_name: str
    is_active: Optional[bool] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    # email: EmailStr
    username: str
    password: str
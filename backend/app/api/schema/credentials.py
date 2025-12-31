from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCredentials(BaseModel):
    email: str
    password_hash: str
    created_at: datetime
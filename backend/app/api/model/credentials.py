from sqlalchemy import Column, String, func, DateTime, ForeignKey
from api.database.db import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Credentials(Base):
    __tablename__ = "credentials"
    
    id = Column(UUID(as_uuid=True), unique=True, primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    authorId = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
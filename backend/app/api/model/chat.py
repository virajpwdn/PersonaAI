from sqlalchemy import String, DateTime, Column, UUID, ForeignKey, func
from api.database.db import Base
import uuid
# from sqlalchemy.dialects.postgresql import UUID

class Chat(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    connection_id = Column(String, ForeignKey('personna.connection_id', ondelete='CASCADE'), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
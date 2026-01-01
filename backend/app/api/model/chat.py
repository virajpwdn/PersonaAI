from sqlalchemy import String, DateTime, Column, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from api.database.db import Base
import uuid
# from sqlalchemy.dialects.postgresql import UUID

class Chat(Base):
    __tablename__ = "chats"
    
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    connection_id = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    role = Column(String, nullable=False)  # "user" | "ai" | "system"
    content = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
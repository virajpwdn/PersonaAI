from sqlalchemy import String, func, DateTime, Column, ForeignKey
import uuid
from sqlalchemy.dialects.postgresql import UUID
from api.database.db import Base

class Persona(Base):
    __tablename__ =  'persona'
    
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    # connection_id = Column(String) # user Id + persona Id
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    persona_name = Column(String, nullable=False)
    
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
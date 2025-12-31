from sqlalchemy import String, func, DateTime, Column
import uuid
from sqlalchemy.dialects.postgresql import UUID
from api.database.db import Base

class Personna(Base):
    __tablename__ =  'personna'
    
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    connection_id = Column(String) # user Id and persona Id
    user_id = Column(String)
    personna_id = Column(String)
    personna_name = Column(String)
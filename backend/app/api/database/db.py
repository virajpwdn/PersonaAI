import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import QueuePool
from dotenv import load_dotenv
import redis

load_dotenv()

"""Postgres Connection Setup"""
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Database url not found in env")

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_recycle=3600,
    pool_pre_ping=True,
    echo=False,
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

Base = declarative_base()

def init_db():
    """Creates all tables in database"""
    Base.metadata.create_all(bind=engine)
    

def drop_all_tables():
    """Drop all tables from the database"""
    Base.metadata.drop_all(bind=engine)

def get_db():
    """This Function provides a database session
            It ensures the session is properly closed after the request.
    """
    init_db()
    # drop_all_tables()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        


# Redis Connection Setup
class RedisClient:
    """Redis Connection Manager"""
    _instance = None
    
    @classmethod
    def get_client(cls) -> redis.Redis:
        """
        Get or create Redis Client
        """
        if cls._instance is None:
            cls._instance = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            username="default",
            password=os.getenv("REDIS_DB"),
            decode_responses=True,
            socket_connect_timeout=5,
            socket_keepalive=True
        )
        
        return cls._instance
    
    @classmethod
    # This function belongs to the class, not objects. Since we are using classmethods
    def connect(cls) -> redis.Redis:
        """Test Redis Connection"""
        try:
            client = cls.get_client()
            client.ping()
            print("Redis connected successfully")

            return client
        except Exception as e:
            print(f"Redis connection failed: {str(e)}")
            raise
        
    
    @classmethod
    # This function belongs to the class, not objects. Since we are using classmethods
    def disconnect(cls) -> None:
        """close redis connection"""
        if cls._instance:
            cls._instance.close()
            cls._instance = None
            print("Redis disconnected")
            
redis_client = RedisClient.get_client()
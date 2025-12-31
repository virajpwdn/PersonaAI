import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import QueuePool
from dotenv import load_dotenv

load_dotenv()

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
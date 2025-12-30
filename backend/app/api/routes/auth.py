from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.schema.user import UserResponse, UserCreate
from api.database.db import get_db
from api.model.user import User

class SignupRequest(BaseModel):
    email: str
    password: str

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/login")
def login():
    return {"data": "You are logged in"}

@router.post("/signup", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    The 'db: Session = Depends(get_db)' part injects the database session.
    """
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    db_user = User(
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        password_hash=user.password,  # In real app, hash this!
        is_active=True
    )
    
    # Add to database and commit
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
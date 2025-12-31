from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.schema.user import UserResponse, UserCreate, UserLogin
from api.database.db import get_db
from api.model.user import User
from api.model.credentials import Credentials
from api.controllers.user import UserCRUD


class SignupRequest(BaseModel):
    email: str
    password: str

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(user: UserLogin, db:Session = Depends(get_db)):
    if not user:
        raise HTTPException(status_code=400, detail="All fields are required")
    
    isUserExist = db.query(User).filter(User.username == user.username).first()
    
    if not isUserExist:
        raise HTTPException(status_code=404, detail="No account found, please sign up")
    return {"data": "You are successfully logged in"}

@router.post("/signup", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Abstract this validation layer in different dierctory
    if not user:
        raise HTTPException(status_code=400, detail="All fields are required")
    
    # Check if email already exists
    existing_user = db.query(Credentials).filter(Credentials.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    user_crud = UserCRUD()
    db_user = user_crud.create(db, user)
    return db_user
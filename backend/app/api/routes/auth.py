from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.schema.user import UserResponse, UserCreate, UserLogin
from api.database.db import get_db
from api.model.user import User
from api.model.credentials import Credentials
from api.controllers.user import UserCRUD
from api.utils.create_token import create_access_token
from fastapi import Response
import jwt
import bcrypt


class SignupRequest(BaseModel):
    email: str
    password: str

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(user: UserLogin, response: Response, db:Session = Depends(get_db)):
    if not user:
        raise HTTPException(status_code=400, detail="All fields are required")
    
    db_user = db.query(User).filter(User.username == user.username).first()
    
    if not db_user:
        raise HTTPException(status_code=404, detail="Invalid Credientials!")
    
    user_db_password = db.query(Credentials).filter(Credentials.authorId == db_user.id).first()
    print("HASH DB PASSWORD -> ", user_db_password.password_hash)
    if not user_db_password:
        raise HTTPException(status_code=404, detail="Invalid Credientials!")
    
    verify_password = bcrypt.checkpw(
            password=user.password.encode('utf-8'),  # Plain password
            hashed_password=user_db_password.password_hash.encode('utf-8')  # Hashed password
        )
    if not verify_password:
        raise HTTPException(status_code=404, detail="Invalid username or password!")
    
    token = create_access_token(user_id=db_user.id)
    # Setting cookies in response
    response.set_cookie(
        httponly=True,
        key="access_token",
        value=token,
        expires=24*60*60,
        samesite="lax"
        # secure=True,
    )
    print("SIGN_IN TOKEN -> ", token)
    return {"data": "You are successfully logged in"}

@router.post("/signup", response_model=UserResponse)
def create_user(user: UserCreate, response: Response, db: Session = Depends(get_db)):
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
    
    token = create_access_token(db_user.id)
    
    # Setting cookies in response
    response.set_cookie(
        httponly=True,
        key="access_token",
        value=token,
        expires=24*60*60,
        samesite="lax"
        # secure=True,
    )
    print("SIGN_UP TOKEN -> ", token)
    return db_user
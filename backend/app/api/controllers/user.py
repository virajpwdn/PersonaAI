from api.database.db import get_db  # This get_db method makes connection with postgres
from api.model.user import User     # This is database schema of user
from api.model.credentials import Credentials  # This is credentials schema
from api.schema.user import UserCreate         # This is the response which is sent in json to client
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserCRUD:
    """
    Create a new user.
    The 'db: Session = Depends(get_db)' part injects the database session.
    """
    def create(self, db: Session, user: UserCreate):
        hash_password = pwd_context.hash(user.password)
        print("Hashed_Password", hash_password)
        
        db_user = User(
            username = user.username,
            first_name = user.first_name,
            last_name = user.last_name,
            is_active = True
        )
        
            # Add to database and commit
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        creds = Credentials(
            email = user.email,
            password_hash = hash_password,
            authorId = db_user.id
        )
        
        db.add(creds)
        db.commit()
        db.refresh(creds)
        return db_user
    
import jwt
import os
from datetime import datetime, timedelta, timezone

def create_access_token(user_id: str, expires_delta: timedelta = None):
    """
    Generate JWT Token
    
    :param user_id: User ID to encode in token
    :type user_id: str
    :type expires_delta: optional
    returns token string
    """
    if not user_id:
        ValueError("user id is missing")
    
    expire = datetime.now(timezone.utc) + expires_delta
    
    payload = {
        "sub": user_id,
        "iat":  datetime.now(timezone.utc),
        "exp":  expire,
    }
    
    token = jwt.encode(payload, os.getenv("SECRET_KEY"), os.getenv("ALGORITHM"))
    
    return token


# def verify_token(token: str) -> str:
#     if not token:
#         ValueError("token is missing to decode")
    
#     payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithm=[os.getenv("ALGORITHM")])
#     user_id = payload.user_id
#     return user_id
    
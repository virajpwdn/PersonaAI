import json
from fastapi import Request, HTTPException, status
import jwt
import os
from api.database.db import redis_client, SessionLocal
from api.model.user import User

async def verify_and_attach_user(request: Request) -> Request:
    """
    Auth middleware - which decodes jwt token and attch users data and sends forward.
    """
    
    # Extracting token from cookies
    
    token = request.cookies.get("access_token")
    
    if not token:
        auth_header = request.headers.get("Authorization")
        
        if not auth_header:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing"
        )
        
        try:
            schema, token = auth_header.split()
            if schema.lower() != "bearer":
                raise ValueError("Invalid auth schema")
        except ValueError:
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid auth header format. user 'Bearer'."
        )
    
    
        
    # Decoding JWT token
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        print("PAYLOAD - ", payload)
        user_id = payload.get("sub")
        
        if not user_id:
            raise jwt.InvalidTokenError("No user Id in token")
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )
    
    except jwt.InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {str(e)}"
        )
        
    redis_key = f"user_session: {user_id}"
    
    try:
        # Check Redis Cache First
        cached_user = redis_client.get(redis_key)
        
        if cached_user:
            #if user exist then forwarding it with request
            user_data = json.loads(cached_user)
        else:
            # finding in db
            db = SessionLocal()
            try:
                user = db.query(User).filter(user_id == user_id).first()
                
                if not user:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="user not found"
                    )
                
                user_data = {
                    "id": str(user.id),
                    "username": user.username,
                    "firstName": user.first_name,
                    "lastName": user.last_name,
                    "isActive": user.is_active,
                }
            
                redis_client.setex(
                    redis_key,
                    os.getenv("REDIS_SESSION_EXPIRY"),
                    json.dumps(user_data)
                )
            
            finally:
                db.close()
                
        request.state.user = user_data
        request.state.user_id = user_id
    
        return request
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Auth error: {str(e)}"
        )

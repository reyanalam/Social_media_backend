import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from . import schemas
from jose import JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .config import Settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#secret key for signing JWT tokens
#algorithm used for signing JWT tokens
#expiration time for JWT tokens

SECRET_KEY = f"{Settings.SECRET_KEY}" 
ALGORITHM = f"{Settings.ALGORITHM}"
ACCESS_TOKEN_EXPIRE_MINUTES = f"{Settings.ACCESS_TOKEN_EXPIRE_MINUTES}"

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) #decode the JWT token
        # Accessing user_id to ensure it's in the payload
        id:str = payload.get('user_id') #acces the id from the decoded token

        if id is None:
            raise credentials_exception 
        
        token_data = schemas.TokenData(id=id)
    except JWTError:
        return credentials_exception
    
    return token_data
    

def get_current_user(token: str = Depends(oauth2_scheme)): #get the current user from the token
        
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_access_token(token, credentials_exception)
    
    
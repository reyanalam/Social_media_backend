from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas, utils
from .. import oauth2

router = APIRouter(tags=["Authentication"])

@router.post("/login",response_model=schemas.Token)
def login(user_credentials:schemas.UserLogin, db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    hashed_password = utils.hash(user_credentials.password)

    if not utils.verify(user_credentials.password, hashed_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    #creating a token
    #return token
    access_token = oauth2.create_access_token(data={"user_id": user.id})


    return {"access_token": access_token, "token_type": "bearer"}
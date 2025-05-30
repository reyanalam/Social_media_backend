from pydantic import BaseModel
from pydantic.networks import EmailStr
from typing import Optional, Union
from datetime import datetime
from pydantic import conint

class CreatePost(BaseModel):
    title: str
    content: str
    published: bool = True

class UpdatePost(BaseModel):
    title: str
    content: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
        
class Response(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    published: bool
    owner_id:int
    owner: UserOut

    class Config:
        orm_mode = True  

class postout(BaseModel):
    Post: Response
    votes: int

    class Config:
        orm_mode = True  

class UserCreate(BaseModel):
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Union[int, str]


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # type: ignore # 1 for like, 0 for unlike
    # dir: conint(le=1)  # This ensures dir can only be 0 or 1
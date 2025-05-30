from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #this is specifing the passlib that we are using bcrypt for hashing the password

def hash(password: str):
    return pwd_context.hash(password) 


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password) #this is used to verify the password when user login
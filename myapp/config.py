from pydantic_settings import BaseSettings

class Settings(BaseSettings): # This helps in validating environment variables
    DATABASE_HOSTNAME: str  
    DATABASE_PORT: str 
    DATABASE_PASSWORD: str 
    DATABASE_NAME: str 
    DATABASE_USERNAME: str
    SECRET_KEY: str #for JWT token
    ALGORITHM: str # Default algorithm for JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int # Expiration time for access token in minutes

    class Config:
        env_file = ".env"

Settings = Settings()
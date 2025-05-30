from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import Settings

#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:reyan@localhost/fastapi "
SQLALCHEMY_DATABASE_URL = f"postgresql://{Settings.DATABASE_USERNAME}:{Settings.DATABASE_PASSWORD}@{Settings.DATABASE_HOSTNAME}:{Settings.DATABASE_PORT}/{Settings.DATABASE_NAME} "

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''
while True:
    try:
        conn = psycopg2.connect(host="localhost", database="fastapi ", user="postgres", password="reyan", cursor_factory=RealDictCursor) #cursor_name gives the column name 
        cursor = conn.cursor()
        print("Database connection successful")
        break

    except Exception as e:
        print("Connection to database failed")
        print(e)
        time.sleep(2)

''' 
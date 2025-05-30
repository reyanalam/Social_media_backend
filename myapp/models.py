#models represent a table in the database
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from . database import Base
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)  

    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),nullable=False)  # Foreign key to link to User table

    #IF THE TABLE HAS ALREADY BEEN CREATED, WE CANNOT ADD NEW COLUMNS TO IT. SQLALCHEMY DO NOT WORK THIS WAY.
    owner = relationship("User")  # This creates a relationship to the User model, allowing access to the user who created the post

class User(Base):
    __tablename__ = "users"

    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Vote(Base):
    __tablename__ = "votes"

    post_id = Column(Integer, ForeignKey("post.id", ondelete="CASCADE"), primary_key=True)  # Foreign key to link to Post table
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)  # Foreign key to link to User table
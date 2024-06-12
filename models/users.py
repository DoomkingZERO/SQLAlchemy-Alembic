from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)  # Adjusted primary key name
    name = Column(String)
    email = Column(String)
    
    posts = relationship("Post", back_populates="author")

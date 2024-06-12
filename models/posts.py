from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Post(Base):
    __tablename__ = 'posts'
    post_id = Column(Integer, primary_key=True, autoincrement=True)  # Adjusted primary key name
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.user_id'))  # Adjusted foreign key name
    
    author = relationship("User", back_populates="posts")

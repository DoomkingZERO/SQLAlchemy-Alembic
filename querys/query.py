import sys
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.posts import Post
from models.users import User

engine = create_engine('sqlite:///demo.db') # Update the path to your demo.db file
Session = sessionmaker(bind=engine)
session = Session()

# Query all users
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.email)

# Query all posts
posts = session.query(Post).all()
for post in posts:
    print(post.id, post.title, post.content)

from app.database import Base
from sqlalchemy import Column, Integer, String
from passlib.apps import custom_app_context as pwd_context
ROLE_USER = 0
ROLE_ADMIN = 1

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    username = Column(String(120), index = True, unique = True)
    email = Column(String(120), index = True, unique = True)
    password_hash = Column(String(128))
    avatar = Column(String(120), index=True)

    def __init__(self, username=None, email=None):
        self.username = username
        self.email =  email
    #=================================================#
    #         LOGIN MANAGER REQUIRED FIELDS           #
    #=================================================#

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return unicode(self.id)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

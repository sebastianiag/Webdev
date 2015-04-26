from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from database import Base


FRESHMAN = "Prepa"
ERUDITE = "Erudite"
LEGENDARY = "Legendary"
DINO = "Dino"
MOD = "Moddy"

class Professor(Base):
    __tablename__ = "professors"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    department = Column(String)
    overall = Column(Float)
    class_quality = Column(Integer)
    personality = Column(Integer)
    grading = Column(Integer)
    responsibility = Column(Integer)
    comments = relationship("Comment", order_by="Comment.id", backref="professors")

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s', department='%s', overall='%.2f)', aprendisaje='%d'" %(self.first_name, self.last_name, self.department, self.overall, self.aprendisaje)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    rank = Column(String)
    comments = relationship("Comment", order_by="Comment.id", backref="users")
'''
class Creator(Base):
    __tablename__="comments"
    id = Column(Integer, primary_key=True)
    name = Column(String)
'''
    
class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    user = relationship("User", backref=backref("comment", order_by=id))
    user_id = Column(Integer, ForeignKey("users.id"))
    comment = Column(String)
    date = Column(DateTime)
    rating = Column(Integer)
    professor = relationship("Professor", backref=backref("comment", order_by=id))
    professor_id = Column(Integer, ForeignKey("professors.id"))
    def __repr__(self):
        return "<Comments(comments='%s')>" % self.comment

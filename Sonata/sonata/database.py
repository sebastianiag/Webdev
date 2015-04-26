from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, "app.db"))

Base = declarative_base()
Session = sessionmaker(bind=engine)

def init_db():
    import models
    Base.metadata.create_all(bind=engine)

#from flask_sqlalchemy import 
from sqlalchemy.orm import declarative_base, Session, sessionmaker, scoped_session
from sqlalchemy import create_engine

Base = None
engine = None
session = None


def registerDatabase(app):
    global Base, engine, session
    
    engine = create_engine(app.config.get('DATABASE_URL'))
    
    session = scoped_session(sessionmaker(bind=engine))
    
    Base = declarative_base()

def createTables():
    from App.Models.User import User
    Base.metadata.create_all(bind=engine)
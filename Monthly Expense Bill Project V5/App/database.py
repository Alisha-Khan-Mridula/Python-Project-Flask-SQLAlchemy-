from sqlalchemy.orm import scoped_session, Session, declarative_base, sessionmaker
from sqlalchemy import create_engine 


Base = None
session = None
engine = None

def registerDatabase(app):
    global Base, session, engine
    
    engine = create_engine(app.config.get('DATABASE_URL'))
    session = scoped_session(sessionmaker(bind=engine))
    
    Base = declarative_base()
    
    
def createTables():
    from App.Models.User import User
    Base.metadata.create_all(bind=engine)
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker, scoped_session, declarative_base

Base = None
engine = None
Session = None

def registerDatabase(app) -> None:
    global Base, engine, Session
    
    engine = create_engine(app.config.get('DATABASE_URL'))
    
    Session = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit = False))
    
    Base = declarative_base()
    
    
def createTables():
    Base.metadata.create_all(bind=engine)
                
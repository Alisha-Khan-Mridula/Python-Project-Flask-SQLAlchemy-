from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker, scoped_session, declarative_base

engine = None
Session = None
Base = declarative_base()

def registerDatabase(app) -> None:
    global  engine, Session
    
    engine = create_engine(app.config.get('DATABASE_URL'))
    
    Session = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit = False))

    
    
def createTables():
    Base.metadata.create_all(bind=engine)
                
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker, scoped_session, declarative_base

engine = None
Session = None
Base = None
#Base = declarative_base()

def registerDatabase(app) -> None:
    global  Base, engine, Session
    
    engine = create_engine(app.config.get('DATABASE_URL'))
    
    Session = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit = False))

    Base = declarative_base()
    
def createTables():
    from .Models.User import User
    Base.metadata.create_all(bind=engine)
                
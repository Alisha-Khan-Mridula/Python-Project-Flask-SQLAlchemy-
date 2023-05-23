from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session


Base = None
engine = None
session = None



def registerDatabase(app) -> None: 
    global Base, engine, session
    

    engine = create_engine(app.config.get("DATABASE_URI"))
    
    session = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit= False))
    
    Base = declarative_base()
    
    
    
def createTables():
    Base.metadata.create_all(bind=engine)
    
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

engine = None
session = None
Base = None
#Base = declarative_base()

def registerDatabase(app) -> None:
    global  Base, engine, session
    
    engine = create_engine(app.config.get('DATABASE_URL'))
    
    session = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit = False))

    Base = declarative_base()
    
def createTables():
    from .Models.User import User
    Base.metadata.create_all(bind=engine)
    
    from .Repositories.UserRepository import UserRepository
    # newUser = User("Alisha","123456")
    # UserRepository().save(newUser)
                
from sqlalchemy import String, Boolean, Integer, DateTime, Column
from datetime import datetime
from sqlalchemy.orm import session, sessionmaker, scoped_session, declarative_base
#from App.database import engine
from marshmallow import Schema, fields


class BaseModel():
    IsActive = Column(Boolean, default=True)
    CreatedByID = Column(String(10), nullable= False)
    CreatedOn = Column(DateTime, default=datetime.now)
    UpdatedByID = Column(String(10))
    UpdatedOn = Column(DateTime, onupdate=datetime.now)
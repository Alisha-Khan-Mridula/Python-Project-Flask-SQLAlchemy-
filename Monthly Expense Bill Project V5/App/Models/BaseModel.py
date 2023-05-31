from sqlalchemy import String, Integer, DateTime, Column, Boolean
from datetime import datetime


class BaseModel():
    
    IsActive = Column(Boolean, default=True)
    CreatedByID = Column(String(10), default = True)
    CreatedOn = Column(DateTime, default=datetime.now)
    UpdatedByID = Column(String(10))
    UpdatedOn = Column(DateTime, onupdate=datetime.now)
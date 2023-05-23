from sqlalchemy import String, Boolean, Integer, DateTime, Column
from datetime import datetime

class BaseModel():
    IsActive = Column(Boolean, default=True)
    CreatedByID = Column(String(10), nullable=False)
    CreatedOn = Column(DateTime, default=datetime.now)
    UpdatedByID = Column(String(10))
    UpdatedOn = Column(DateTime, onupdate=datetime.now)
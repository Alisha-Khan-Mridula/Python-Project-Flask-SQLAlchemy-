print("From Employee")

from ..database import Base
from .BaseModel import BaseModel

from sqlalchemy import String, Boolean, Integer, DateTime, Column
from datetime import datetime

class Employee(Base, BaseModel):
    __tablename__ = 'Employees'
    
    ID = Column(Integer, primary_key=True, autoincrement=True)
    employeename = Column(String(50), unique=True)
    designation = Column(String(50))
    
    
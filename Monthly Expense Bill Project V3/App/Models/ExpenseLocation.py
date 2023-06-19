from .BaseModel import BaseModel
from App.database import Base
from sqlalchemy import String, Boolean, Integer, DateTime, Column, ForeignKey
from datetime import datetime

class ExpenseLocation(Base,BaseModel):
    __tablename__ = 'ExpenseLocation'
    ID = Column(String(10), primary_key=True)
    LocationName = Column(String(50), nullable=True)
    ShortName = Column(String(50), nullable=True)
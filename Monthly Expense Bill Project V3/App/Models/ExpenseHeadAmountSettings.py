from .BaseModel import BaseModel
from App.database import Base
from sqlalchemy import String, Boolean, Integer, DateTime, Column, ForeignKey
from datetime import datetime


class ExpenseHeadAmountSettings(Base,BaseModel):
    __tablename__ = 'ExpenseHeadAmountSettings'  
    ID = Column(String(10), primary_key=True)
    ExpenseHeadID = Column(String(10), ForeignKey('ExpenseHead.ID'))
    ExpenseLocationID = Column(String(10), ForeignKey('ExpenseLocation.ID'))
    Designation = Column(String(50), nullable=False)
    Amount = Column(Integer, nullable=False)
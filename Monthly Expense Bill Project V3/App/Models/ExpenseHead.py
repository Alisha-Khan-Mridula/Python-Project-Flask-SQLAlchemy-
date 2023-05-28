#============= Importing from Context.py =====================#
from .BaseModel import BaseModel
from App.database import Base
from sqlalchemy import String, Boolean, Integer, DateTime, Column
from datetime import datetime


#============ ExpenseHead Model Creation ================#
class ExpenseHead(Base,BaseModel):
    __tablename__ = 'ExpenseHead'
    ID = Column(String(10), primary_key= True)
    HeadName = Column(String(20), nullable= True)
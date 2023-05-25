from .BaseModel import BaseModel
#from Models.BaseModel import Base
from App.database import Base
from sqlalchemy import String, Boolean, Integer, DateTime, Column
from datetime import datetime





class User(Base, BaseModel):
    __tablename__ = 'User'
    
    ID = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    passward = Column(String(50))
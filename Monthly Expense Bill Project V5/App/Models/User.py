from sqlalchemy import String, Integer, DateTime, Column
from datetime import datetime
from App.Models.BaseModel import BaseModel
from App.database import Base


class User(Base, BaseModel):
    
    __tablename__ = 'User'
    
    ID = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique= True)
    password = Column(String(50))


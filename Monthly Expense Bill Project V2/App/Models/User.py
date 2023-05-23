from BaseModel import BaseModel
from App.database import Base
from sqlalchemy import Column, Boolean, String, DateTime, Integer


class User(Base, BaseModel):
    __tablename__ = "User"
    
    ID = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    passward = Column(String(20), nullable=False)
    
    
    
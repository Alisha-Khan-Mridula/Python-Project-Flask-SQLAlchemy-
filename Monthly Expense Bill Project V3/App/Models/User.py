from .BaseModel import BaseModel
#from Models.BaseModel import Base
from App.database import Base
from sqlalchemy import String, Boolean, Integer, DateTime, Column
from datetime import datetime
from App.Models.BaseModel import Schema, fields


print("From User")


class User(Base, BaseModel):
    __tablename__ = 'User'
    
    ID = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))
    
    
class UserSchema(Schema):
    ID = fields.Int()
    username = fields.Str()
    password = fields.Str()
    IsActive = fields.Bool()
    CreatedByID = fields.Str()
    CreatedOn = fields.DateTime()
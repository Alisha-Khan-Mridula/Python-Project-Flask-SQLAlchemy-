from App.database import Base
from App.Models.BaseModel import BaseModel
from sqlalchemy import Column, Boolean, String, DateTime, Integer
from marshmallow import Schema, fields


class User(Base, BaseModel):
    
    __tablename__ = 'User'
    
    ID = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique= True)
    password = Column(String(50))
    
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.CreatedByID = "System"
        return self
    
    
class UserSchema(Schema):
    ID = fields.Int()
    username = fields.Str()
    password = fields.Str()
    CreatedByID = fields.Str()
    
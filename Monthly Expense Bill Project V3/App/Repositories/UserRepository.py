from .GenericRepository import GenericRepository 
from App.Models.User import User, UserSchema
from App.database import Session
from App.Models.BaseModel import Schema

class UserRepository(GenericRepository):
    def __init__(self, db: Session):
        super().__init__(db, User, UserSchema())

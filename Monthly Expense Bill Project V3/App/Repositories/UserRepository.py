from .GenericRepository import GenericRepository 
from Models.User import User
from database import Session

class UserRepository(GenericRepository):
    def __init__(self, db: Session):
        super().__init__(db, User)

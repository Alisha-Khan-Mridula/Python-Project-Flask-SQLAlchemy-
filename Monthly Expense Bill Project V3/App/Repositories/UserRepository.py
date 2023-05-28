from .GenericRepository import GenericRepository 
from App.Models.User import User
from App.database import Session

class UserRepository(GenericRepository):
    def __init__(self, db: Session):
        super().__init__(db, User)

from .GenericRepository import GenericRepository 
from App.Models.User import User
from App.database import session

class UserRepository(GenericRepository):
    
    
    def __init__(self):
        super().__init__(User)
        
        
    def getusernameByID(self, username):
        return session.query(User).filter_by(username=username).first()

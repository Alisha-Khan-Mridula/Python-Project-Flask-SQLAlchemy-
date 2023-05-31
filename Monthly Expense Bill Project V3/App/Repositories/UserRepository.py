from .GenericRepository import GenericRepository 
from App.Models.User import User

class UserRepository(GenericRepository):
    
    
    def __init__(self):
        super().__init__(User)

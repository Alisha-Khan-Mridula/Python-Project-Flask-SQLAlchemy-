from App.Repositories.GenericRepository import GenericRepositort
from App.database import Session
from App.Models.User import User

class UserRepository(GenericRepositort):
    
    def __init__(self):
        super().__init__(User)
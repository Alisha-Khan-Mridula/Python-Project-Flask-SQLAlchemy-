from .Repositories.UserRepository import UserRepository


def authenticate(username: str, password: str):
    user = UserRepository().getusernameByID(username)
    if user and user.password == password:
        return user
    
    
def indetity(playload):
    userid = playload['identity']
    return UserRepository().getusernameByID(userid)
    

from flask import Blueprint, request
from App.database import Base, Session
from App.Models.User import User
from App.Repositories.UserRepository import UserRepository

user = Blueprint('user', __name__)

@user.route('/user/save', methods = ['POST'])
def saveUser():
    data = User()
    UserRepository(Session).save(data)
    return "Successfully Saved"

@user.route('/user/getAll', methods=['GET'])
def get():
    return UserRepository(Session()).getAll()

    
    
    
    
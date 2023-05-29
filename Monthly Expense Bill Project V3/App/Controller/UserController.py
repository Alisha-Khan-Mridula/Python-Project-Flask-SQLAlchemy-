from flask import Blueprint, request
from App.database import Base, Session
from App.Models.User import User
from App.Repositories.UserRepository import UserRepository

user = Blueprint('user', __name__)

@user.route('/user/save', methods = ['POST'])
def saveUser():
    data = User(**request.json)
    UserRepository(Session).save(data)
    return "Successfully Saved"

@user.route('/user/getAll', methods=['GET'])
def getAll():
    return UserRepository(Session()).getAll()

@user.route('/user/get/ID/<ID>', methods = ['GET'])
def getByID(ID):
    return UserRepository(Session()).getByID(ID)

@user.route('/user/update/Info', methods = ['PUT'])
def updateInfo():
    data = User(**request.json)
    UserRepository(Session()).update(data)
    return "Update data successfully"

@user.route('/user/delete/Info/<ID>', methods = ['DELETE'])
def deleteUser(ID : int):
    UserRepository(Session()).deleteData(ID)
    return "Delete data successfully"
    
    
    
    
from flask import Blueprint, request
from App.database import Base, session
from App.Models.User import User, UserSchema
from App.Repositories.UserRepository import UserRepository

user = Blueprint('user', __name__)

@user.route('/user/save', methods = ['POST'])
def saveUser():
    data = User(**request.json)
    return UserSchema().dump(UserRepository().save(data))
    #return "Successfully Saved"

@user.route('/user/getAll', methods=['GET'])
def getAll():
    return UserSchema(many=True).dump(UserRepository().getAll())

@user.route('/user/get/ID/<ID>', methods = ['GET'])
def getByID(ID):
    return UserSchema().dump(UserRepository().getByID(ID))

@user.route('/user/update/Info', methods = ['PUT'])
def updateInfo():
    data = User(**request.json)
    UserSchema().dump(UserRepository().update(data))
    return "Update data successfully"

@user.route('/user/delete/Info/<ID>', methods = ['DELETE'])
def deleteUser(ID : int):
    UserSchema().dump(UserRepository().deleteData(ID))
    return "Delete data successfully"
    
    
    
    
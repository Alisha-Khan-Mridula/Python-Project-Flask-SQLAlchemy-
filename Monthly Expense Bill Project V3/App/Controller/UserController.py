from flask import Blueprint, request, jsonify
from App.database import Base, session
from App.Models.User import User, UserSchema
from App.Repositories.UserRepository import UserRepository
from App.securityJWT import token_required, secret_key
import jwt
from app import app
user = Blueprint('user', __name__)






@app.route('/auth/<ID>', methods = ['GET'])
def auth(ID):
    token = jwt.encode({'ID': ID}, secret_key)
    

    return token




@user.route('/user/save', methods = ['POST'])
def saveUser():
    data = User(**request.json)
    return UserSchema().dump(UserRepository().save(data))
    #return "Successfully Saved"

@user.route('/user/getAll', methods=['GET'])
@token_required
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
    
    
    
    
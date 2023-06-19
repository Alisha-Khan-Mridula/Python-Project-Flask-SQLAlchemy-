from flask import Blueprint, request, jsonify
from App.database import Base, session
from App.Models.User import User, UserSchema
from App.Reposotories.UserRepository import UserRepository
#from app import app
control = Blueprint('control', __name__)

user = Blueprint('user', __name__)


# #token = None
# secret_key = '57de392eaf3c4c1fa6a6333ba95eb57f68'
# def token_required(func):
#     @wraps(func)
#     def decorated(*args, **kwargs):
#         token = request.args.get('token') #Build the token
#         print(token)
#         if not token:
            
#            return jsonify({'Alert!' : 'Token is missing!'})
#         try:
#           data = jwt.decode(token, secret_key, algorithms="HS256" )
          
#         except Exception as e:
#             traceback.print_exc()
#             return jsonify({'Alert!': 'Invalid Token'})
#         return func(*args, **kwargs)
#     return decorated 



# @app.route('/auth/<ID>', methods = ['GET'])
# def auth(ID):
#     token = jwt.encode({'ID': ID}, secret_key)
    

#     return jsonify({'token': token})




@user.route('/user/save', methods = ['POST'])
def saveUser():
    data = User(**request.json)
    return UserSchema().dump(UserRepository().save(data))
    #return "Successfully Saved"

@user.route('/user/getAll', methods=['GET'])
#@jwt_required
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
    
    
    
    
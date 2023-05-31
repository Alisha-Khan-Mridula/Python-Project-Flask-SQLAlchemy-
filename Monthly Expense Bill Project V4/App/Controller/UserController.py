from flask import Blueprint, request
from App.Models.User import User, UserSchema
from App.Repositories.UserRepositoty import UserRepository

user = Blueprint('user', __name__)


@user.route('/user/save', methods = ['POST'])
def save():
    newUser = User(request.json['username'], request.json['password'])
    return UserSchema().dump(UserRepository().save(newUser)), 201
    
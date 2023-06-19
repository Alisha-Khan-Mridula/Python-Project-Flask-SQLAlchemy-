from functools import wraps
import jwt
from flask import Blueprint, request, jsonify


    
secret_key = '57de392eaf3c4c1fa6a6333ba95eb57f68'
def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token') #Build the token
        print(token)
        if not token:
            
            return jsonify({'Alert!' : 'Token is missing!'})
        try:
            data = jwt.decode(token, secret_key, algorithms="HS256" )
        
        except Exception as e:
            #traceback.print_exc()
            return jsonify({'Alert!': 'Invalid Token'})
        return func(*args, **kwargs)
    return decorated 
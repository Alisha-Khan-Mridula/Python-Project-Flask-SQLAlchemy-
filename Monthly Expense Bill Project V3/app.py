from flask import Flask, request, jsonify
import os
from App.database import registerDatabase, createTables
#from flask_jwt import JWT



app = Flask(__name__)

def createApp() -> Flask:


    ## Register Configuration
    registerConfiguration(app)
    
    
    
    
    
    ## Register Database
    registerDatabase(app)
    
    
    
    ## Register JWT
    #registerJWT(app)
    
    
    ## Register CORS
    
    ## Register logger
    
    ## Register Swagger
    
    
    
    registerBlueprint(app)
    
    # ## Route for create database 
    @app.route('/create/db', methods = ['GET'])
    def createDB():
        createTables()
        
        return{"Message":"Database created successfully"},200
    
    
    
    
    
    
    return app



def registerBlueprint(app):
    from App.Controller.UserController import user 
    app.register_blueprint(user)


def registerConfiguration(app) -> Flask:
    configInfo = os.environ.get('CONFIG')
    
    if configInfo is None:
        print("Predefined config has been found. Loading the default development config")
        configInfo = "App.config.DevelopmentConfig"
        
        
    app.config.from_object(configInfo)
    #print(f"Debug: {app.config.get('DEBUG')}")
    
# def registerJWT(app: Flask) -> None:
#     from App.authentication import authenticate, indetity
    
#     app.secret_key = app.config.get("SECRET_KEY")
    
#     app.config.update(
#         jwt = JWT(app, authenticate, indetity)
#     )

    
   
    
    
createApp()







from flask import Flask, request, jsonify
import os
from App.database import registerDatabase, createTables

app = Flask(__name__)

def createApp() -> Flask:


    ## Register Configuration
    registerConfiguration(app)
    
    
    
    
    
    ## Register Database
    registerDatabase(app)
    
    
    
    ## Register JWT
   
    
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
    from App.Controller.UserControll import user
    app.register_blueprint(user)



def registerConfiguration(app) -> Flask:
    configInfo = os.environ.get('CONFIG')
    
    if configInfo is None:
        print("Predefined config has been found. Loading the default development config")
        configInfo = "App.config.DevelopmentConfig"
        
        
    app.config.from_object(configInfo)    
    
    


createApp()
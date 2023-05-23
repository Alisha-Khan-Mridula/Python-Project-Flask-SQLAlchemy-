from flask import Flask

import os
from App.database import registerDatabase, createTables



def createApp() -> Flask:
    app = Flask(__name__)
    
    ## Register Configuration
    registerConfiguration(app)
    
    
    
    
    
    ## Register Database
    registerDatabase(app)
    
    
    
    ## Register JWT
    
    ## Register CORS
    
    ## Register logger
    
    ## Register Swagger
    
    
    
    
    ## Route for create database 
    @app.route('/create/db', methods = ['GET'])
    def createDB():
        createTables()
        
        return{"Message":"Database created successfully"},200
         
    
    return app



def registerConfiguration(app) -> Flask:
    configInfo = os.environ.get('CONFIG')
    
    if configInfo is None:
        print("Predefined config has been found. Loading the default development config")
        configInfo = "App.config.DevelopmentConfig"
        
        
    app.config.from_object(configInfo)
    #print(f"Debug: {app.config.get('DEBUG')}")
    
    
    
    
app = createApp()
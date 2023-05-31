from flask import Flask
import os
from App.database import registerDatabase, createTables

def createApp() -> Flask:
    
    app = Flask(__name__)
    
    
    ### Register configuration
    
    registerConfig(app)
    
    ### Register Database
    
    registerDatabase(app)
    
    
    ### Register JWT
    
    
    ### Register CORS
    
    
    ### Register Swagger
    
    
    @app.route('/create', methods = ['GET'])
    def create():
       createTables()
        
       return "Success"
    
    
    
    
    return app


def registerConfig(app):
    configInfo = os.environ.get('CONFIG')
    
    if configInfo is None:
        print("Loading default development environment")
        configInfo = "App.config.DevelopmentConfig"
        
    app.config.from_object(configInfo)
    print(f'DATABASE_URL:{app.config.get("DATABASE_URL")}')
    

app = createApp()
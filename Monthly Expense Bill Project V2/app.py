from flask import Flask 

# importing os module for providing a wat to intereact with the operating system
import os   
from App.database import registerDatabase,createTables



def createApp() -> Flask:
    app = Flask(__name__)
    
    
    # Register Configuration
    registerConfig(app)
    
    
    
    # Register Database 
    registerDatabase(app)
    
    
    
    # Register Logger
    
    
    # Register JWT
    
    
    # Register CORS
    
    
    
    # Register Swagger
    
    
    
    ## Special Routes
    @app.route("/", methods=['GET'])
    def index():
        return {"message":"Welcome to flask api"},200
    
    
    @app.route("/create/db", methods=['GET'])
    def createDB():
        createTables()
        return {"Message": "Successfully created Database"},200
    
    
    
    return app




#### Confuguration Setup ###

def registerConfig(app) -> Flask:
    configInfo = os.environ.get('CONFIG')
    
    if configInfo is None:
        print("No predefined config found. Loading development default config")
        configInfo = "App.config.DevelopmentConfig"
        
    app.config.from_object(configInfo)
    #print(f"Debug: {app.config.get('DEBUG')}")
        
        



app = createApp()
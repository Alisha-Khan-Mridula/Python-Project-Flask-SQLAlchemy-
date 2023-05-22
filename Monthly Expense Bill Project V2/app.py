from flask import Flask 

# importing os module for providing a wat to intereact with the operating system
import os   



def createApp() -> Flask:
    app = Flask(__name__)
    
    
    # Register Configuration
    registerConfig(app)
    
    
    
    # Register Databse
    
    
    
    # Register Logger
    
    
    # Register JWT
    
    
    # Register CORS
    
    
    
    # Register Swagger
    
    
    return app




#### Confuguration Setup ###

def registerConfig(app) -> Flask:
    configInfo = os.environ.get('CONFIG')
    
    if configInfo is None:
        print("No predefined config found. Loading default config")
        configInfo = "App.config.DevelopmentConfig"
        
    app.config.from_object(configInfo)
    print(f"Debug: {app.config.get('DEBUG')}")
        
        



app = createApp()
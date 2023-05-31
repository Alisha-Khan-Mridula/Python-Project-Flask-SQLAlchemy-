from flask import Flask
import os
from App.database import registerDatabase, createTables
def createApp() -> Flask:
    
    app = Flask(__name__)
    
    ### Register Configuration
    registerConfiguration(app)
    
    
    ### Register Database
    registerDatabase(app)
    
    registerBlueprint(app)
    ### Register JWT
    
    
    ### Register Logger
    
    
    ### Register Swagger
    
    @app.route('/database/creation')
    def create():
        createTables()
        
        return "Database created successfully"
    
    
    

    
   

    return app


def registerBlueprint(app):
    from App.Controller.UserController import user
    app.register_blueprint(user)
    

def registerConfiguration(app):
    configInfo = os.environ.get('CONFIG')
    
    if configInfo is None:
        print("NO Config Found. Loading default development config")
        configInfo = "App.Config.DevelopmentConfig"
        
    app.config.from_object(configInfo)
    
    #print(f"DEBUG:{configInfo}")


app = createApp()



    
    


    
    
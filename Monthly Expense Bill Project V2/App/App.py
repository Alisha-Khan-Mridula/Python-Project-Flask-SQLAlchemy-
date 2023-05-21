from flask import Flask
import logging
from Models.Context import Session
#from database import createDB

import database

session = Session()

app = Flask(__name__)

database.createDB()

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)


# info_handler = logging.FileHandler('info.log')
# warning_handler = logging.FileHandler('warning.log')
# error_handler = logging.FileHandler('error.log')



# info_handler.setLevel(logging.INFO)
# warning_handler.setLevel(logging.WARNING)
# error_handler.setLevel(logging.ERROR)



# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')



# info_handler.setFormatter(formatter)
# warning_handler.setFormatter(formatter)
# error_handler.setFormatter(formatter)



# logger.addHandler(info_handler)
# logger.addHandler(warning_handler)
# logger.addHandler(error_handler)



# @app.route('/great/<name>')
# def great(name):
#     #logger.warning('This is a warning message')
#     return f'Hello {name}'


####### Runtime Error handle #######
# @app.route('/divide/number/<number1>/<number2>')
# def index(number1:int , number2:int):
#     #logger.error("This is an error")
#     return str(int(number1)/int(number2))


# @app.teardown_request
# def teardownRequest(exception):
#     if exception is not None:
#         logger.error( "RUNTIME ERROR :: " + str(exception))
        
        
 
# def logging_middleware(next_handler):
#     def middleware(request):
#         # Log the request details
#         app.logger.info(f'Request: {request.method} {request.path} from {request.remote_addr} with data {request.data}')
#         # Call the next handler in the chain
#         response = next_handler(request)
#         # Log the response details
#         app.logger.info(f'Response: {response.status} {response.data}')
#         # Return the response
#     return middleware         



import os
#from config import DevelopmentConfig, ProductionConfig, TestingConfig, Config

# def createBD() -> Flask:
#     os.environ.get('CONFIGURATION_SETUP')
    
#     app.config.from_object(os.environ['CONFIGURATION_SETUP'])
#     print(f"Debug: {app.config.get('DEBUG')}")
#     print(f"Testing: {app.config.get('TESTING')}")
#     print(f"Database: {app.config.get('DATABASE_URI')}")
    
#     return app
# app = createBD()

if __name__ == '__main__':
    app.run(debug=True)
class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URL = ' '
    

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URL = 'sqlite:///Database/dev.db'
    
class TestingConfig(Config):
    TESTING = True
    DATABASE_URL = 'sqlite:///Database/teat.db'
        
    
class ProductionConfig(Config):
    DATABASE_URL = 'sqlite:///Database/data.db'
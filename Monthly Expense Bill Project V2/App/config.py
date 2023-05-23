class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''
    
class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = "sqlite:///database/dev.db"

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = "sqlite:///database/test.db"
    
class ProductionConfig(Config):
    DATABASE_URI = "sqlite:///database/data.db"
        
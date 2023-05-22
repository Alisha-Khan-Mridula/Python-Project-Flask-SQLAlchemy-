class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''
    
class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = "sqlite://dev.db"

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = "sqlite://testing.db"
    
class ProductionConfig(Config):
    DATABASE_URI = "sqlite://data.db"
        
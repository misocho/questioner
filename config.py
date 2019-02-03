import os


class Config():
    DEBUG = False
    TESTING = False
    CSRF_ENABLE = True
    SECRET_KEY = os.getenv('SECRET_KEY')


class Development(Config):
    DEBUG = True
    TESTING = False
    DB_URL = os.getenv('DB_URL')


class Production(Config):
    DEBUG = False
    TESTING = False
    DB_URL = os.environ['DATABASE_URL']


class Testing(Config):
    DEBUG = True
    TESTING = True
    DB_URL = os.getenv('TEST_DB_URL')


app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}

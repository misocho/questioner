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
    DB_URL = "postgres://vmywlvzmqzipkn:f63cc30ffc8ceb424ad31fdee4d5a358397bb8cdb44c096c09527872a04ef8af@ec2-54-235-67-106.compute-1.amazonaws.com:5432/de9nm0u7qtkkkj
"


class Testing(Config):
    DEBUG = True
    TESTING = True
    DB_URL = os.getenv('TEST_DB_URL')


app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}

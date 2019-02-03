import os


class Config():
    DEBUG = False
    TESTING = False
    CSRF_ENABLE = True
    SECRET_KEY = os.getenv('SECRET_KEY')


class Development(Config):
    DEBUG = True
    TESTING = False
    DATABASE_URL = os.getenv('DATABASE_URL')


class Production(Config):
    DEBUG = False
    TESTING = False
    DATABASE_URL = "dbname='d1rl3g8596kh7m' user='qlzqbdvkiettzv' port='5432' host='ec2-23-21-244-254.compute-1.amazonaws.com' password='a6a43d2550377fb9932fe640fe517ef2d2937cc6d6ddc5897e539a9a16ebdd89"


class Testing(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv('TEST_DB_URL')


app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}

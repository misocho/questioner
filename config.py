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
    DB_URL = os.environ['DATABASE_URL'] = "postgres://qlzqbdvkiettzv:a6a43d2550377fb9932fe640fe517ef2d2937cc6d6ddc5897e539a9a16ebdd89@ec2-23-21-244-254.compute-1.amazonaws.com:5432/d1rl3g8596kh7m"


class Testing(Config):
    DEBUG = True
    TESTING = True
    DB_URL = os.getenv('TEST_DB_URL')


app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}

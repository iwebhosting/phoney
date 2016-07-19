class Settings(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/phoney.db'
    SECRET_KEY = 'CHANGEME'
    DEBUG = True
    TESTING = False
    REQUIRE_LOGIN = True
    DB_SECRET_KEY = 'INSECURE_DEFAULT'

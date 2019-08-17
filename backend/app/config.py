import os

import dotenv

'''
Configure the several environments where this application can run.

If deployed in heroku, note that everytime a deployment from github
happens, the directory where the app sits gets deleted, therefore `.env` file
disappears. All in one the `.env` files has to copied every time the app is
deployed. For this reason, if the `.env` file does not exist `os.getenv` has
a second argument as default: `os.getenv(<env variable>, <default>)`
'''

dotenv.load_dotenv()


class Config:
    pass


class ProductionConfig(Config):
    FLASK_DEBUG = False
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        r";v:<6KVX^(zprT>/SC8#)w(Pn8W`RbBTH-pqGA;u(,tGF95vXduyUy(p7rB@H:")


class DevelopmentConfig(Config):
    FLASK_DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY", "Rx7mrFRZkzUVyXtZusWCYSs88RsQpVam")
    DEBUG = True
    TESTING = False


class TestingConfig(DevelopmentConfig):
    TESTING = True

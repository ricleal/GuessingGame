import os

import dotenv

'''
Configure the several enviroments where this application can run.
Note that heroku doesn't like `.env` files. They have to copied every time
the app is deployed.
For test purposes use:
`os.getenv(<env variable>, <default>)`
with a default value
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

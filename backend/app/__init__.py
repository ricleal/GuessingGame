import logging

from flask import Flask

from .config import Config

from.api import api
'''
This module fires up the application.
All methods that should be called before at initialization should go into
`create_app`
'''


logger = logging.getLogger(__name__)


def create_app(config_class=Config):
    """Construct the core application.
    The static files will be in static in root of the project"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(api)

    setup_logging(app)

    return app


def setup_logging(app):
    ''' Sets the debug logging '''
    if app.debug:
        logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(name)s :: %(filename)s:%(lineno)d (%(funcName)s) : '
            '%(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

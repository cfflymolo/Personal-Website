""" Application configuration """

import os


class Config:
    """ Base Configuration """

    APP_DIR = os.path.abspath(os.path.dirname(__file__))    # this directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        'alsdkjfoqw90eurjojasvnqu9ehrotj'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SSL_DISABLE = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """ Development Configuration """

    DEBUG = True
    DB_NAME = 'data-dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)


class TestConfig(Config):
    """ Test Configuration """

    TESTING = True
    DB_NAME = 'data-test.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)


class ProductionConfig(Config):
    """ Production Configuration """

    DEBUG = False

    if os.environ.get('DATABASE_URL') is None:
        DB_NAME = 'db.sqlite'
        DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
        SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)
    else:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

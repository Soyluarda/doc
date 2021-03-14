import os

CONFIG = {
   'postgresUrl': 'doc-db.ctvkjnpaido7.us-east-2.rds.amazonaws.com',
   'postgresUser': 'docuser',
   'postgresPass': 'docpassw',
   'postgresDb': 'docdb',
}

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"
    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False
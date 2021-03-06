#!/usr/bin/env python
# coding=utf-8


import os
import logging
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dns.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
pkey = '/Users/didi/.ssh/id_rsa'
user = 'root'


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                     datefmt='%m-%d %H:%M',
                     filename='log/myapp.log',
                     filemode='w')
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
            '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

class Config:
    SECRET_KEY = 'You-will-never-give-up'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DARABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'dns.db')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DARABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'dns.db')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DARABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'dns.db')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

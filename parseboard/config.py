import os
import json
import urllib3

basedir = os.path.abspath(os.path.dirname(__file__))
with open('/etc/config.json') as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

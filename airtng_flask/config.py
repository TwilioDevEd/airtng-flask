import os

basedir = os.path.abspath(os.path.dirname(__file__))

from dotenv import load_dotenv
load_dotenv()

class DefaultConfig(object):
    SECRET_KEY = 'secret-key'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')


class TestConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True
    TESTING = True
    LOGIN_DISABLED = True
    WTF_CSRF_ENABLED = False


config_env_files = {
    'test': 'airtng_flask.config.TestConfig',
    'development': 'airtng_flask.config.DevelopmentConfig',
}

class DefaultConfig(object):
    SECRET_KEY = '%^!@@*!&$8xdfdirunb52438#(&^874@#^&*($@*(@&^@)(&*)Y_)((+'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
    TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
    TWILIO_NUMBER = 'your_twilio_number'


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


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

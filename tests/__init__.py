from airtng_flask.bootstrap import get_app
from airtng_flask.database import get_db

twilio_settings = {
    'app': None,
    'db': None,
}


def init_test_environment():
    twilio_settings['app'] = get_app('test')
    twilio_settings['db'] = get_db('test')


def test_app():
    return twilio_settings['app']


def test_db():
    return twilio_settings['db']

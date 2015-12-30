from airtng_flask.bootstrap import get_app
from airtng_flask.database import get_db

test_settings = {
    'app': None,
    'db': None,
}


def init_test_environment():
    test_settings['app'] = get_app('test')
    test_settings['db'] = get_db('test')


def test_app():
    return test_settings['app']


def test_db():
    return test_settings['db']

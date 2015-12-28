from flask.ext.testing import TestCase
from tests import init_test_environment, test_app, test_db

init_test_environment()


class BaseTestCase(TestCase):
    render_templates = False

    def create_app(self):
        return test_app()

    def setUp(self):
        test_db().create_all()

    def tearDown(self):
        test_db().session.remove()
        test_db().drop_all()

    def assert_flashes(self, expected_message, expected_category='message'):
        with self.client.session_transaction() as session:
            try:
                category, message = session['_flashes'][0]
            except KeyError:
                raise AssertionError('nothing flashed')
            assert expected_message in message
            assert expected_category == category

from flask.ext.testing import TestCase

from airtng_flask import app, config_app


class BaseTestCase(TestCase):
    render_templates = False

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LOGIN_DISABLED'] = True
        app.config['WTF_CSRF_ENABLED'] = True

        return app

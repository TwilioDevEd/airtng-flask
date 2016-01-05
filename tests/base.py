from flask.ext.testing import TestCase
from airtng_flask import app, config_app
from airtng_flask.models import init_models_module
from tests import init_test_environment, test_app, test_db, test_bcrypt

from airtng_flask.models.reservation import Reservation
from airtng_flask.models.user import User
from airtng_flask.models.vacation_property import VacationProperty

from airtng_flask.models.reservation import Reservation
from airtng_flask.models.user import User
from airtng_flask.models.vacation_property import VacationProperty


class BaseTestCase(TestCase):
    render_templates = False

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LOGIN_DISABLED'] = True
        app.config['WTF_CSRF_ENABLED'] = True
        return app

    def setUp(self):
        test_db().create_all()
        self._populate_database()

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

    def _populate_database(self):
        host = User(
                name="Host",
                email="host@email.com",
                password="1234567",
                phone_number="+1111111",
                area_code="111"
        )
        guest = User(
                name="Guest",
                email="guest@email.com",
                password="1234567",
                phone_number="+5555555",
                area_code="555"
        )
        vacation_property = VacationProperty("Property", "http://image.com/image.png", host)
        reservation = Reservation("Reserved", vacation_property, guest)
        reservation.anonymous_phone_number = "+8888888"
        db.session.add(host)
        db.session.add(guest)
        db.session.add(vacation_property)
        db.session.add(reservation)
        db.session.commit()

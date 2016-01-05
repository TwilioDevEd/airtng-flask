import unittest
import xml.etree.ElementTree as ElementTree

from base import BaseTestCase
from tests import test_db

class ViewsTests(BaseTestCase):
    def get_to_home_route_should_render_default_view(self):
        self.client.get('/home')

        self.assert_template_used('home.html')

    def test_get_to_test_root_route_should_render_register_view(self):
        self.client.get('/')

        self.assert_template_used('register.html')

    def test_get_to_login_route_should_render_default_view(self):
        self.client.get('/login')

        self.assert_template_used('login.html')

    def test_get_to_register_route_should_render_default_view(self):
        self.client.get('/register')

        self.assert_template_used('register.html')

    def test_get_to_new_property_route_should_render_default_view(self):
        self.client.get('/properties/new')

        self.assert_template_used('property_new.html')

    def test_get_to_properties_route_should_render_default_view(self):
        self.client.get('/properties')

        self.assert_template_used('properties.html')

    def test_get_to_new_reservation_route_should_render_default_view(self):
        self.client.get('/reservations/new')

        self.assert_template_used('reservation.html')

    def test_post_to_exchange_sms_should_serve_twiml_with_message(self):
        response = self.client.post('/exchange/sms', data=dict(From="+1111111", To="+8888888", Body="Hi"))
        twiml = ElementTree.fromstring(response.data)

        assert twiml.findall("./Sms")[0].text == "Hi"
        assert twiml.findall("./Sms")[0].attrib["to"] == "+5555555"

    def test_post_to_exchange_voice_should_serve_twiml_with_message(self):
        response = self.client.post('/exchange/voice', data=dict(From="+1111111", To="+8888888", Body="Hi"))
        twiml = ElementTree.fromstring(response.data)

        assert not twiml.findall("./Play") is None
        assert twiml.findall("./Dial")[0].text == "+5555555"

if __name__ == '__main__':
    unittest.main()

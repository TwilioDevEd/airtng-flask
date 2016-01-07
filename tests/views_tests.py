import unittest
import xml.etree.ElementTree as ElementTree

from base import BaseTestCase


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
        self.client.get('/reservations/1')

        self.assert_template_used('reservation.html')


if __name__ == '__main__':
    unittest.main()

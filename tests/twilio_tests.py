import unittest
from xml.etree import ElementTree

from airtng_flask.twilio.sms_sender import SmsSender
from base import BaseTestCase


class TwilioServicesTests(BaseTestCase):
    # Ensures respond a message will contain a response with a message back
    def test_respond_message_contains_message_element(self):
        # arrange
        twilio_services = SmsSender()
        # act
        message = "Message"
        response = str(twilio_services.respond_message(message))
        twiml = ElementTree.fromstring(response)

        # assert
        assert twiml.findall("./Message/Body")[0].text == message


if __name__ == '__main__':
    unittest.main()

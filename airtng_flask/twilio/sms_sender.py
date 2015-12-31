from airtng_flask.twilio import account_sid, auth_token, phone_number
from twilio import twiml
from twilio.rest import TwilioRestClient


class SmsSender:
    twilio_client = None

    def __init__(self):
        if SmsSender.twilio_client is None:
            SmsSender.twilio_client = TwilioRestClient(account_sid(), auth_token())

    def send_message(self, to, message):
        SmsSender.twilio_client.messages.create(
                to=to,
                from_=phone_number(),
                body=message,
        )

from airtng_flask.phone import account_sid, auth_token, application_sid
from twilio.rest import TwilioRestClient



class Purchaser:
    twilio_client = None

    def __init__(self):
        if Purchaser.twilio_client is None:
            Purchaser.twilio_client = TwilioRestClient(account_sid(), auth_token())

    def buy_number(self, area_code):
        numbers = Purchaser.twilio_client.phone_numbers.search(country="US",
                                                               type="local",
                                                               area_code=area_code,
                                                               sms_enabled=True,
                                                               voice_enabled=True)

        if numbers:
            number = self._purchase_number(numbers[0])
            return number
        else:
            numbers = Purchaser.twilio_client.phone_numbers.search(country="US",
                                                                   type="local",
                                                                   sms_enabled=True,
                                                                   voice_enabled=True)

            if numbers:
                number = self._purchase_number(numbers[0])
                return number

        return None

    def _purchase_number(self, number):
        return number.purchase(sms_aplication_sid=application_sid(), voice_application_sid=application_sid())

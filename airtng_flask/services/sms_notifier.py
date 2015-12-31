from airtng_flask.lib.string_builder import StringBuilder
from airtng_flask.twilio.sms_sender import SmsSender


class SmsNotifier:
    sms_sender = None

    def __init__(self):
        if SmsNotifier.sms_sender is None:
            SmsNotifier.twilio_client = SmsSender()

    def notify_host(self, reservation):
        message_builder = StringBuilder()
        message_builder \
            .append("You have a new reservation request from %s for %s:\n"
                    .format(reservation.host.name, reservation.vacation_property.description))

        message_builder.append("%s \n".format(reservation.message))
        message_builder.append("Reply [accept] or [reject]")

        SmsNotifier.sms_sender.send_message(reservation.vacation_property.host.phone_number, message_builder.__str__())

    def notify_guest(self, reservation):
        message_builder = StringBuilder()
        message_builder \
            .append("Your recent request to stay at %s was %s\n"
                    .format(reservation.vacation_property.description, reservation.status))

        SmsNotifier.sms_sender.send_message(reservation.hots.phone_number, message_builder.__str__())

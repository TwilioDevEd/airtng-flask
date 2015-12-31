from airtng_flask.sms.sms_sender import SmsSender
from airtng_flask.utilities.string_builder import StringBuilder


class SmsNotifier:
    sms_sender = None

    def __init__(self):
        if SmsNotifier.sms_sender is None:
            SmsNotifier.sms_sender = SmsSender()

    def notify_host(self, reservation):
        message_builder = StringBuilder()
        message_builder \
            .append("You have a new reservation request from {0} for {1}:\n"
                    .format(reservation.vacation_property.host.name, reservation.vacation_property.description))

        message_builder.append("{0} \n".format(reservation.message))
        message_builder.append("Reply [accept] or [reject]")

        SmsNotifier.sms_sender.send_message(reservation.vacation_property.host.phone_number, message_builder.__str__())

    def notify_guest(self, reservation):
        message_builder = StringBuilder()
        message_builder \
            .append("Your recent request to stay at {0} was {1}\n"
                    .format(reservation.vacation_property.description, reservation.status))

        SmsNotifier.sms_sender.send_message(reservation.guest.phone_number, message_builder.__str__())

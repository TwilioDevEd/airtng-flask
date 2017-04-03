from airtng_flask.models import app_db, auth_token, account_sid, phone_number, application_sid
from flask import render_template
from twilio.rest import Client

DB = app_db()


class Reservation(DB.Model):
    __tablename__ = "reservations"

    id = DB.Column(DB.Integer, primary_key=True)
    message = DB.Column(DB.String, nullable=False)
    status = DB.Column(DB.Enum('pending', 'confirmed', 'rejected', name='reservation_status_enum'),
                       default='pending')
    anonymous_phone_number = DB.Column(DB.String, nullable=True)
    guest_id = DB.Column(DB.Integer, DB.ForeignKey('users.id'))
    vacation_property_id = DB.Column(DB.Integer, DB.ForeignKey('vacation_properties.id'))
    guest = DB.relationship("User", back_populates="reservations")
    vacation_property = DB.relationship("VacationProperty", back_populates="reservations")

    def __init__(self, message, vacation_property, guest):
        self.message = message
        self.guest = guest
        self.vacation_property = vacation_property
        self.status = 'pending'

    def confirm(self):
        self.status = 'confirmed'

    def reject(self):
        self.status = 'rejected'

    def __repr__(self):
        return '<Reservation {0}>'.format(self.id)

    def notify_host(self):
        self._send_message(self.vacation_property.host.phone_number,
                           render_template('messages/sms_host.txt',
                                           name=self.guest.name,
                                           description=self.vacation_property.description,
                                           message=self.message))

    def notify_guest(self):
        self._send_message(self.guest.phone_number,
                           render_template('messages/sms_guest.txt',
                                           description=self.vacation_property.description,
                                           status=self.status))

    def buy_number(self, area_code):
        numbers = self._get_twilio_client().available_phone_numbers("US") \
                                           .local \
                                           .list(area_code=area_code,
                                                 sms_enabled=True,
                                                 voice_enabled=True)

        if numbers:
            number = self._purchase_number(numbers[0])
            self.anonymous_phone_number = number
            return number
        else:
            numbers = self._get_twilio_client().available_phone_numbers("US") \
                                               .local \
                                               .list(sms_enabled=True, voice_enabled=True)

            if numbers:
                number = self._purchase_number(numbers[0])
                self.anonymous_phone_number = number
                return number

        return None

    def _purchase_number(self, number):
        return self._get_twilio_client().incoming_phone_numbers \
                                        .create(sms_application_sid=application_sid(),
                                                voice_application_sid=application_sid(),
                                                phone_number=number) \
                                        .phone_number

    def _get_twilio_client(self):
        return Client(account_sid(), auth_token())

    def _send_message(self, to, message):
        self._get_twilio_client().messages \
                                 .create(to,
                                         from_=phone_number(),
                                         body=message)

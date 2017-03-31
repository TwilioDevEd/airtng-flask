from airtng_flask.models import app_db, auth_token, account_sid, phone_number
from flask import render_template
from twilio.rest import Client

db = app_db()


class Reservation(db.Model):
    __tablename__ = "reservations"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    status = db.Column(db.Enum('pending', 'confirmed', 'rejected', name='reservation_status_enum'), default='pending')

    guest_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    vacation_property_id = db.Column(db.Integer, db.ForeignKey('vacation_properties.id'))
    guest = db.relationship("User", back_populates="reservations")
    vacation_property = db.relationship("VacationProperty", back_populates="reservations")

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
        return '<VacationProperty %r %r>' % self.id, self.name

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

    def _get_twilio_client(self):
        return Client(account_sid(), auth_token())

    def _send_message(self, to, message):
        self._get_twilio_client().messages.create(
                to=to,
                from_=phone_number(),
                body=message)

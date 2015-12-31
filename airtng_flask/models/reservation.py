from airtng_flask.models import app_db

db = app_db()


class ReservationStatus(object):
    Pending = 'pending'
    Confirmed = 'confirmed'
    Rejected = 'rejected'


class Reservation(db.Model):
    __tablename__ = "reservations"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    vacation_property_id = db.Column(db.Integer, db.ForeignKey('vacation_properties.id'))
    guest = db.relationship("User", back_populates="reservations")
    vacation_property = db.relationship("VacationProperty", back_populates="reservations")

    def __init__(self, message, vacation_property, guest):
        self.message = message
        self.guest = guest
        self.vacation_property = vacation_property
        self.status = ReservationStatus.Pending

    def confirm(self):
        self.status = ReservationStatus.Confirmed

    def reject(self):
        self.status = ReservationStatus.Rejected

    def __repr__(self):
        return '<VacationProperty %r %r>' % self.id, self.name

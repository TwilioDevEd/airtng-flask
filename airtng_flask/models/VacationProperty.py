from airtng_flask.models import app_db

db = app_db()


class VacationProperty(db.Model):
    __tablename__ = "subscribers"

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Subscriber %r %r>' % self.phone_number, self.subscribed

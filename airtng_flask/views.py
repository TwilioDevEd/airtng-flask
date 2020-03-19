from airtng_flask import db, bcrypt, app, login_manager
from flask import session, g, request, flash, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from twilio.twiml.voice_response import VoiceResponse

from airtng_flask.forms import RegisterForm, LoginForm, VacationPropertyForm, ReservationForm, \
    ReservationConfirmationForm
from airtng_flask.view_helpers import twiml, view, redirect_to, view_with_params
from airtng_flask.models import init_models_module

init_models_module(db, bcrypt, app)

from airtng_flask.models.user import User
from airtng_flask.models.vacation_property import VacationProperty
from airtng_flask.models.reservation import Reservation


@app.route('/', methods=["GET", "POST"])
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():

            if User.query.filter(User.email == form.email.data).count() > 0:
                form.email.errors.append("Email address already in use.")
                return view('register', form)

            user = User(
                    name=form.name.data,
                    email=form.email.data,
                    password=form.password.data,
                    phone_number="+{0}{1}".format(form.country_code.data, form.phone_number.data)
            )
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)

            return redirect_to('home')
        else:
            return view('register', form)

    return view('register', form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            candidate_user = User.query.filter(User.email == form.email.data).first()

            if candidate_user is None or not bcrypt.check_password_hash(candidate_user.password,
                                                                        form.password.data):
                form.password.errors.append("Invalid credentials.")
                return view('login', form)

            login_user(candidate_user, remember=True)
            return redirect_to('home')
    return view('login', form)


@app.route('/logout', methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect_to('home')


@app.route('/home', methods=["GET"])
@login_required
def home():
    return view('home')


@app.route('/properties', methods=["GET"])
@login_required
def properties():
    vacation_properties = VacationProperty.query.all()
    return view_with_params('properties', vacation_properties=vacation_properties)


@app.route('/properties/new', methods=["GET", "POST"])
@login_required
def new_property():
    form = VacationPropertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            host = User.query.get(current_user.get_id())

            property = VacationProperty(form.description.data, form.image_url.data, host)
            db.session.add(property)
            db.session.commit()
            return redirect_to('properties')

    return view('property_new', form)


@app.route('/reservations/', methods=["POST"], defaults={'property_id': None})
@app.route('/reservations/<property_id>', methods=["GET", "POST"])
@login_required
def new_reservation(property_id):
    vacation_property = None
    form = ReservationForm()
    form.property_id.data = property_id

    if request.method == 'POST':
        if form.validate_on_submit():
            guest = User.query.get(current_user.get_id())

            vacation_property = VacationProperty.query.get(form.property_id.data)
            reservation = Reservation(form.message.data, vacation_property, guest)
            db.session.add(reservation)
            db.session.commit()

            reservation.notify_host()

            return redirect_to('properties')

    if property_id is not None:
        vacation_property = VacationProperty.query.get(property_id)

    return view_with_params('reservation', vacation_property=vacation_property, form=form)


@app.route('/confirm', methods=["POST"])
def confirm_reservation():
    form = ReservationConfirmationForm()
    sms_response_text = "Sorry, it looks like you don't have any reservations to respond to."

    user = User.query.filter(User.phone_number == form.From.data).first()
    reservation = Reservation \
        .query \
        .filter(Reservation.status == 'pending'
                and Reservation.vacation_property.host.id == user.id) \
        .first()

    if reservation is not None:

        if 'yes' in form.Body.data or 'accept' in form.Body.data:
            reservation.confirm()
        else:
            reservation.reject()

        db.session.commit()

        sms_response_text = "You have successfully {0} the reservation".format(reservation.status)
        reservation.notify_guest()

    return twiml(_respond_message(sms_response_text))


# controller utils
@app.before_request
def before_request():
    g.user = current_user
    uri_pattern = request.url_rule
    if current_user.is_authenticated and (
                        uri_pattern == '/' or uri_pattern == '/login' or uri_pattern == '/register'):
        redirect_to('home')


@login_manager.user_loader
def load_user(id):
    try:
        return User.query.get(id)
    except:
        return None


def _respond_message(message):
    response = VoiceResponse()
    response.message(message)
    return response

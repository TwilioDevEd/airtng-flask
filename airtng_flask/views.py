from airtng_flask.models import init_models_module
from flask import request, flash
from airtng_flask.view_helpers import twiml, view
from flask import Blueprint


def construct_view_blueprint(app, db, bcrypt):
    views = Blueprint("views", __name__)

    init_models_module(db, bcrypt)
    from airtng_flask.models.User import User
    from airtng_flask.models.VacationProperty import VacationProperty
    from airtng_flask.models.Reservation import Reservation

    @views.route('/', methods=["GET", "POST"])
    @views.route('/index', methods=["GET", "POST"])
    def index():
        return view('index')

    return views

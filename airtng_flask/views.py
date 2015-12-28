from flask import request, flash
from airtng_flask.view_helpers import twiml, view
from flask import Blueprint


def construct_view_blueprint(app, db):
    views = Blueprint("views", __name__)

    @views.route('/', methods=["GET", "POST"])
    @views.route('/index', methods=["GET", "POST"])
    def index():
        return view('index')

    return views

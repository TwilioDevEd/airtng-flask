import os
from airtng_flask.config import config_env_files
from flask import Flask

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(config_name='development', p_db=db, p_bcrypt=bcrypt, p_login_manager=login_manager):
    new_app = Flask(__name__)
    config_app(config_name, new_app)
    new_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    p_db.init_app(new_app)
    p_bcrypt.init_app(new_app)
    p_login_manager.init_app(new_app)
    p_login_manager.login_view = 'register'
    return new_app


def config_app(config_name, new_app):
    new_app.config.from_object(config_env_files[config_name])


app = create_app()

import airtng_flask.views

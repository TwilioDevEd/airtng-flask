twilio_settings = {
    'app': None,
}


def init_twilio_module(flask_app):
    twilio_settings['app'] = flask_app


def auth_token():
    return twilio_settings['app'].config['TWILIO_AUTH_TOKEN']


def phone_number():
    return twilio_settings['app'].config['TWILIO_NUMBER']


def account_sid():
    return twilio_settings['app'].config['TWILIO_ACCOUNT_SID']

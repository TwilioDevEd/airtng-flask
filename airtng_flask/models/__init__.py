model_settings = {
    'db': None,
}


def init_models_module(db):
    model_settings['db'] = db


def app_db():
    return model_settings['db']

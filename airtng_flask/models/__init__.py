model_settings = {
    'db': None,
    'bcrypt': None,
}


def init_models_module(db, bcrypt):
    model_settings['db'] = db
    model_settings['bcript'] = bcrypt


def app_db():
    return model_settings['db']


def bcrypt():
    return model_settings['bcript']

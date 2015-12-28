from airtng_flask import get_env

dbs = {
    'test': None,
    'development': None,
}


def get_db(config_name=None):
    if config_name is None:
        config_name = get_env()

    return dbs[config_name]


def set_db(db, config_name=None):
    if config_name is None:
        config_name = get_env()

    dbs[config_name] = db

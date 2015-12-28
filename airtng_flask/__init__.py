import os


def get_env():
    return os.getenv('ENV', 'development')

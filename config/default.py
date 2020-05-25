from os.path import abspath, dirname, join

BASE_DIR = dirname(dirname(abspath(__file__)))

SQLALCHEMY_TRACK_MODIFICATIONS = False

APP_ENV_LOCAL = 'local'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''
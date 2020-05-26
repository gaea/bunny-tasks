from .default import *
from os.path import abspath, dirname, join

BASE_DIR = dirname(dirname(abspath(__file__)))

APP_ENV = APP_ENV_LOCAL
FLASK_ENV = "development"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgresql://btasks_user:btasks_pw@localhost:5433/btasks_db'

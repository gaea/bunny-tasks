from .default import *
from os.path import abspath, dirname, join

BASE_DIR = dirname(dirname(abspath(__file__)))
APP_ENV = APP_ENV_PRODUCTION
FLASK_ENV= APP_ENV
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgres://ejjpmahjwwncwy:3ad92aadb0bfa11326e61094609b0fdb01ef8e18dc8c20b88795905f492268c6@ec2-54-175-117-212.compute-1.amazonaws.com:5432/d76oase0ep70pq'
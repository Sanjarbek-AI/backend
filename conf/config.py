import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('DB_PORT')
DB_PASS = os.environ.get('DB_PASS')
DB_USER = os.environ.get('DB_USER')

API_URL = os.environ.get('API_URL')
LOGIN = os.environ.get('LOGIN')
PASSWORD = os.environ.get('PASSWORD')
PREFIX = os.environ.get('PREFIX')
ORIGINATOR = os.environ.get('ORIGINATOR')

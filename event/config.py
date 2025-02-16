import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_super_secret_key'
SQLALCHEMY_TRACK_MODIFICATIONS = False

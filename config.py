import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'my_super_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'personal.db')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or "postgresql://postgres:password@localhost/personal"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSIN_LIFETIME = datetime.timedelta(days=30)
    TEMPLATES_AUTO_RELOAD = True
    BOOTSTRAP_BOOTSWATCH_THEME = 'flatly'
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = False

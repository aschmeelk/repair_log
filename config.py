import os

CSRF_ENABLED = True
SECRET_KEY = '1001001001'


# Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'repair.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
DEBUG = True
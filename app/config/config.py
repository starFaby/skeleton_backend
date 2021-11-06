import os
class Config:
    SECRET_KEY = os.urandom(32)
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../ideas.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


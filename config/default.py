# coding: utf-8
import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "whatiswrong"
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7
    SESSION_COOKIE_NAME = "sunshine"


    TOKEN_EXPIRATION = 3600*24
    SECURITY_PASSWORD_SALT = "sunshineabcedf"

    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


    SQLALCHEMY_DATABASE_URI = "sqlite:////%s/db/user.db"%PROJECT_PATH


    # Flask-DebugToolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "baichuanfm@163.com"
    MAIL_PASSWORD = "vtwdriivsqvfrhlp"

    REDIS_HOST = "192.168.6.109"
    REDIS_PORT = "6379"
    REDIS_DB = "0"


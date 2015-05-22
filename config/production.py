# coding: utf-8
from .default import Config

class ProductionConfig(Config):
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7
    SESSION_COOKIE_NAME = 'baichuan_session'

    SQLALCHEMY_DATABASE_URI = "sqlite:////%s/db/user.db"%Config.PROJECT_PATH


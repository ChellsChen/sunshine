# coding: utf-8
from .default import Config


class DevelopmentConfig(Config):
    # App config
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:////%s/db/user.db"%Config.PROJECT_PATH



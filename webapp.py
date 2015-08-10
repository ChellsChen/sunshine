#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-08-05 18:48:36
# @Author  : 陈小雪 (shell_chen@yeah.net)
# @Version : $Id$

import os
import logging
import logging.handlers
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from config import load_config
from flaskexts import Sunshine


BASEPATH = os.path.dirname(os.path.realpath(__file__))
SHARE_PATH = os.path.join(BASEPATH, "share")


LOG_FILE = "web.log"
LOG_FORMAT = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
LOG_MAX = 1024*1024*10
BACKUP_COUNT = 5

logger = logging.getLogger()
loghandler = logging.handlers.RotatingFileHandler(
    LOG_FILE,
    maxBytes = LOG_MAX,
    backupCount = BACKUP_COUNT
    )

loghandler.setFormatter(LOG_FORMAT)
logger.addHandler(loghandler)
logger.setLevel(logging.INFO)


APP = Flask(__name__)

def init_app():
    APP.config.from_object(load_config())

    load_dir = os.path.join(BASEPATH, "actions/restfulapi")
    blueprints_dir = os.path.join(BASEPATH, "actions/blueprints")
    sunshine = Sunshine(APP, load_dir, blueprints_dir)


if __name__ == '__main__':
    pass








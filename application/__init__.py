#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-05-05 11:26:30
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import os
import sys

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from flask import Flask, g, render_template
from flask.ext.login import current_user
from config import load_config
import os
import logging

try:
    from imp import reload
    reload(sys)
    sys.setdefaultencoding('utf8')
except (AttributeError, NameError):
    pass

logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filename="log/log.log",
    filemode='a')


def create_app():
    app = Flask(__name__)
    config = load_config()
    app.config.from_object(config)

    register_db(app)
    register_lm(app)
    register_routes(app)
    register_api(app)
    register_email(app)
    register_hooks(app)
    register_error_handle(app)
    return app


def register_db(app):
    from .models import db
    db.init_app(app)

def register_routes(app):
    from .controllers import site, account

    app.register_blueprint(site.bp)
    app.register_blueprint(account.bp)

def register_lm(app):
    from .controllers import lm
    lm.init_app(app)
    lm.login_view = 'account.login'

def register_api(app):
    from .controllers.api import api
    api.init_app(app)

def register_email(app):
    from .emails import mail
    mail.init_app(app)

def register_error_handle(app):
    @app.errorhandler(403)
    def page_403(error):
        return render_template('403.html'), 403

    @app.errorhandler(404)
    def page_404(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def page_500(error):
        return render_template('500.html'), 500


def register_hooks(app):
    @app.before_request
    def before_request():
        g.user = current_user

    @app.after_request
    def after_request(response):
        return response

app = create_app()

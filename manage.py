#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-05-05 17:45:13
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import os
from flask.ext.script import Manager
from application import app
from application.models import db,User

manager = Manager(app)

@manager.command
def run():
    app.run(host="0.0.0.0",port=5050,threaded=True)

@manager.command
def createdb():
    """Create database."""
    db.create_all()
    u = User("admin","admin@fm.cn","123456")
    u.confirmed = True
    u.role = "0"
    db.session.add(u)
    db.session.commit()

if __name__ == "__main__":
    manager.run()

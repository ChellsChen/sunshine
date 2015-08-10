#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2015-08-06 10:42:15
# Author  : 陈小雪
# E-mail  : shell_chen@yeah.net
# Version : v1.0.1

import os
import sys

curdir = os.path.dirname(os.path.realpath(__file__))
sys_path = [ ]
sys_path.append(os.path.join(curdir, "packages"))
for p in sys_path:
    sys.path.insert(0,p)

reload(sys)
sys.setdefaultencoding('utf8')

from flask.ext.script import Manager

from webapp import logger, init_app
from webapp import APP

manager = Manager(APP)

def run_application():
    APP.run(host="0.0.0.0", port=8080, threaded=True, debug=True)

def run_wsgi():
    from flup.server.fcgi import WSGIServer
    WSGIServer(APP, bindAddress=('0.0.0.0', 8080), debug=False, multithreaded=True).run()

def web_start():
    init_app()
    run_application()


@manager.command
def run():
    web_start()

if __name__ == "__main__":
    manager.run()

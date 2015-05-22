#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-05-21 15:28:01
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import os
import sys

curdir = os.path.dirname(os.path.realpath(__file__))
sys_path = [ ]

sys_path.append(os.path.join(curdir, "site_packages/flasks"))
sys_path.append(os.path.join(curdir, "site-packages"))

for p in sys_path:
    sys.path.insert(0,p)


print sys.path



import flask
from flask import Flask, render_template
from sunshine.sunshine import App


application = App( )
app = application.app

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8081, debug=True)

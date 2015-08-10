#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2015-08-06 14:14:07
# Author  : 陈小雪
# E-mail  : shell_chen@yeah.net
# Version : v1.0.1

import os

from flask.ext.login import login_required
from flask import render_template, redirect, url_for, request,Blueprint

app_bp = Blueprint("site", __name__)

@app_bp.route("/")
@app_bp.route("/index/")
@login_required
def index():
    return render_template("index.html")

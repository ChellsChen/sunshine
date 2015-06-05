#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-06-04 16:33:38
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import os

from flask import Blueprint, render_template

name = "blog"
bp = Blueprint("blog", __name__)

@bp.route("/")
@bp.route("/index")
@bp.route("/me")
def blogindex():
    return render_template("blog/index.html")

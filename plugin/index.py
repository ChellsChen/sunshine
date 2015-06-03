#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-06-03 16:06:40
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1


from flask import Blueprint, render_template

name = "index"
bp = Blueprint("index", __name__)

@bp.route("/")
@bp.route("/index")
def page_index():
    return render_template("index.html")


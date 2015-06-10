#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-06-04 16:33:38
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import os

from flask import render_template, request

from flaskext import MyMethodView
from setting import STOREPATH
from publish import BlogData

name = "blog"
bp = "this is bp"

class Blog(MyMethodView):
    def GET(self, key):
        if not key:
            return render_template("blog/index.html")
        return "haha"

class Article(MyMethodView):
    def get(self, key):
        if not key:
            return render_template("blog/add.html")
        return "haha"

    def post(self):
        form = request.form
        title = form.get("title")
        tags = form.get("tags")
        if tags:
            tags = tags.split(",")
        else:
            tags = [ ]

        cls = form.get("cls","undefine")
        context = form.get("context")
        publish = form.get("publish", False)

        bd = BlogData(STOREPATH)
        bd.add(title, context, tags, cls, publish)

        return "sucess!"

def Articles(MyMethodView):
    def get(self):
        bd = BlogData(STOREPATH)
        return




urls = (
        "/",           Blog,
        "/article/",   Article,
        "/articles/",  Articles,
    )



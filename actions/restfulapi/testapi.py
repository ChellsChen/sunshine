#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-08-14 16:58:36
# @Author  : 陈小雪 (shell_chen@yeah.net)
# @Version : $Id$

import os
from flask.ext.restful import Resource


urls = (
    "/api/test/",           "Tests",
    "/api/testing/<key>",   "ApiTest",
)


class Tests(Resource):
    def get(self):
        return {"test":"haha"}


class ApiTest(Resource):
    def get(self, key):
        return {"key":key}



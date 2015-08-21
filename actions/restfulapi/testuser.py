#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-08-21 14:29:01
# @Author  : 陈小雪 (shell_chen@yeah.net)
# @Version : $Id$


from flask.ext.restful import Resource
from flask.ext.restful import fields, marshal_with, reqparse

urls = (
    "/api/user",    "User",
)


post_parser = reqparse.RequestParser()     # 参数解析
post_parser.add_argument(
    'username', dest='username',
    type=str, location='form',
    required=True, help='The user\'s username',
)
post_parser.add_argument(
    'email', dest='email',
    type=str, location='form',
    required=True, help='The user\'s email',
)


user_fields = {
    'username': fields.String,
    'email': fields.String,
}

class User(Resource):

    @marshal_with(user_fields)           # 按user_fields的格式，整理post的返回值
    def post(self):
        args = post_parser.parse_args()
        return args


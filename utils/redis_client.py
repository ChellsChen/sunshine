#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-05-15 09:44:33
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import os

from flask import current_app
from helper.redisclient import RedisClient

def get_redis_connection():
    REDIS_HOST = current_app.config.get("REDIS_HOST")
    REDIS_PORT = current_app.config.get("REDIS_PORT")
    REDIS_DB = current_app.config.get("REDIS_DB")
    return RedisClient(REDIS_HOST, REDIS_PORT, REDIS_DB).connection


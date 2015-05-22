#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-05-05 12:49:39
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import os
import json
import time

def BackgroundSuccess(data):
    try:
        data = json.loads(data)
    except:
        pass

    tmp = {
        "status":"success",
        "datetime":time.time(),
        "data":data
    }
    return tmp

def BackgroundError(message):
    try:
        message = json.loads(message)
    except:
        pass

    tmp = {
        "status": "error",
        "datetime": time.time(),
        "message":message
    }
    return tmp

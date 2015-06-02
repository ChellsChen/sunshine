# -*- coding: utf-8 -*-
import json
import time
import os
import logging
from flask import Blueprint, render_template, request, Response

from emailrule import EmailRule
from utils.checkip import CheckIP
from caches import KvCache
from setting import curdir


name = "email"
bp = Blueprint("emailgrade", __name__)


time_cache = os.path.join(curdir, "share/.cache/time.log")
score_cache = os.path.join(curdir, "share/.cache/score.log")
EmailCheck = EmailRule()
ScoreCache = KvCache(score_cache, 60*10, 60*60*2)
TimeCache = KvCache(time_cache, 60*10, 0.5)

@bp.route('/')
@bp.route("/email")
@bp.route("/index")
def labs_index():
    return render_template("index.html")


@bp.route("/check/<email>")
def check_email(email):
    addr = request.remote_addr
    secrets_key = request.cookies.get("reputation")

    checkip = CheckIP()

    response = Response()
    response.set_cookie("reputation", checkip.secrets)

    if not checkip.checks(secrets_key):
        response.data = json.dumps({"status":"1"})
        return response

    score = ScoreCache.get(email)
    if score:
        response.data = json.dumps({"status":"0","data":score})
        return response

    timecache = TimeCache.get(addr)
    if timecache:
        response.data = json.dumps({"status":"1"})
        return response

    try:
        res = EmailCheck.get_email_result(email)
    except:
        logging.exception("get_email_result error")
        response.data = json.dumps({"status":"3"})
        return response

    if not res:
        response.data = json.dumps({"status":"2"})
    else:

        logging.info("{ip:%s, email:%s, score:%s}"%(addr, email, res[0]))

        data = {"grade":res[0],"decision":res[1]}

        ScoreCache.set(email, data)
        TimeCache.set(addr, time.time())

        response.data = json.dumps({"status":"0","data":data})

    return response

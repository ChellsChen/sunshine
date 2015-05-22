#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-04-30 18:02:33
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import os
import json
import time


from itsdangerous import URLSafeTimedSerializer
from flask import render_template, url_for
from flask import current_app as app

from ..emails.emails import send_email
from ..models import User,db
from utils import get_ip_address


TOKEN_EXPIRATION = 3600*24

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config.get("SECRET_KEY"))
    return serializer.dumps(email, salt = app.config.get("SECURITY_PASSWORD_SALT"))


def confirm_token(token, expiration = TOKEN_EXPIRATION):
    serializer = URLSafeTimedSerializer(app.config.get("SECRET_KEY"))
    try:
        email = serializer.loads(
            token,
            salt = app.config.get("SECURITY_PASSWORD_SALT"),
            max_age = expiration
        )
    except:
        return False
    return email

def get_all_user():
    users = User.query.all()
    tmp = [ ]
    for user in users:
        t = {"email":user.email,"name":user.name,"role":user.role,"active":user.active}
        tmp.append(t)
    return tmp

def store_in_rdbms(signup_data):
    db.session.add(User(**signup_data))
    db.session.commit()


def send_confirm_email(email):
    token = generate_confirmation_token(email)
    confirm_url = url_for("account.confirm_email", token = token, _external = True)

    try:
        local_ip = get_ip_address("eth1")
    except:
        local_ip = get_ip_address("eth0")

    tmp = confirm_url.split("/")
    port = tmp[2].split(":")[1];
    host = "%s:%s"%(local_ip, port)
    tmp[2] = host
    url = "/".join(tmp)

    html = render_template("account/email.html", confirm_url = url)

    subject = "test"
    send_email(subject,[email],html)











# -*- coding: utf-8 -*-
import json
import time
import os
import logging
from flask import Blueprint, render_template, request, Response

from setting import curdir


name = "email"
bp = Blueprint("emailgrade", __name__)

@bp.route('/')
def index():
    return render_template("index.html")

# -*- coding: utf-8 -*-
import json
import time
import os
import logging
from flask import Blueprint, render_template, request, Response

from setting import curdir


name = "email"
bp = Blueprint("email", __name__)

@bp.route("/")
def index():
    return "shell"

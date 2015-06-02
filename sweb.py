#-coding:utf-8


import os
import sys
import json
import logging
from flask import Flask, render_template

curdir = os.path.dirname(os.path.realpath(__file__))
sys_path = [ ]
sys_path.append(os.path.join(curdir, "site-packages"))
for p in sys_path:
    sys.path.insert(0,p)

from plugins import load
from config import load_config


logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    #filename=".log",
    )


app = Flask(__name__)

def init_model(app):
    config = load_config()
    app.config.from_object(config)

    plugin_dir = os.path.join(curdir, "plugin")
    mode_infos = load(plugin_dir)
    for mode_info in mode_infos.values():
        _, bps, name = mode_info
        url_prefix = "/" + name
        app.register_blueprint(bps, url_prefix = url_prefix)

def run_application():
    init_model(app)
    app.run(host="0.0.0.0", port=8000, threaded=True)

def run_wsgi():
    from flup.server.fcgi import WSGIServer
    init_model(app)
    WSGIServer(app, bindAddress=('0.0.0.0', 8000), debug=True, multithreaded=True).run()


if __name__ == "__main__":
    run_application()

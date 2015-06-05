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
    filename=".log",
    )


def init_app():
    app = Flask(__name__)
    init_model(app)
    return app

def init_model(app):
    config = load_config()
    app.config.from_object(config)

    plugin_dir = os.path.join(curdir, "plugin")
    mode_infos = load(plugin_dir)
    for mode_info in mode_infos.values():
        _, bps, name = mode_info
        if name == "index":
            app.register_blueprint(bps)
            continue
        url_prefix = "/" + name
        app.register_blueprint(bps, url_prefix = url_prefix)

def run_application():
    app.run(host="0.0.0.0", port=8001, threaded=True)

def run_wsgi():
    from flup.server.fcgi import WSGIServer
    WSGIServer(app, bindAddress=('0.0.0.0', 8001), debug=True, multithreaded=True).run()

app = init_app()


if __name__ == "__main__":
    run_wsgi()

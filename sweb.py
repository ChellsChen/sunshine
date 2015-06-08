#-coding:utf-8


import os
import sys
import json
import logging

curdir = os.path.dirname(os.path.realpath(__file__))
sys_path = [ ]
sys_path.append(os.path.join(curdir, "site-packages"))
for p in sys_path:
    sys.path.insert(0,p)

from flask import Flask, render_template
import flask
from plugins import load
from config import load_config


logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    #filename=".log",
    )


class Sunshine(object):
    plugin_dir = os.path.join(curdir, "plugin")
    URLS = [ ]
    PLUGINS = [ ]

    def __init__(self, app):
        self.app = app
        self.load_plugin()
        self.logurls()

    def load_plugin(self):
        mode_infos = load(self.plugin_dir)

        for model, bps, name, urls in mode_infos.values():
            self.init_mode(model, bps, name, urls)

        self.__add_url()

    def groups(self, urls):
        i = 0
        t = []
        while i < len(urls):
            t.append((urls[i], urls[i+1]))
            i = i + 2
        return t

    def init_mode(self, model, bps, name, urls):
        for url, fun in self.groups(urls):
            if url.startswith("/"):
                url = "/%s%s"%(name, url)
            else:
                url = os.path.join("/", name, url)

            if isinstance(fun, basestring):
                if not hasattr(model, fun):
                    logging.error("plugin %s not hasattr [%s]"%(model, fun))
                    continue
                fun = getattr(model, fun)
            self.URLS.append((url, fun))

        self.PLUGINS.append((name, model))

    def logurls(self):
        l = 0
        for u,c in self.URLS:
            if len(u) > l:
                l = len(u)

        lines = ['']
        for u,c in self.URLS:
            lines.append("%s  ===>  %s" % (u.ljust(l),c))
        logging.info('\n'.join(lines))

    def __add_url(self):
        for url, fun in self.URLS:
            self.app.add_url_rule(url, None,fun)

    def register_api(view, endpoint, url, pk='id', pk_type='int'):
        view_func = view.as_view(endpoint)
        app.add_url_rule(url, defaults={pk: None},
                         view_func=view_func, methods=['GET',])
        app.add_url_rule(url, view_func=view_func, methods=['POST',])
        app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                         methods=['GET', 'PUT', 'DELETE'])


def init_app():
    print flask.__file__
    app = Flask(__name__)
    init_model(app)
    return app




def run_application(app):
    app.run(host="0.0.0.0", port=8001, threaded=True, debug=True)

def run_wsgi():
    from flup.server.fcgi import WSGIServer
    WSGIServer(app, bindAddress=('0.0.0.0', 8001), debug=True, multithreaded=True).run()

# app = init_app()

def sunshine_test():
    app = Flask(__name__)
    sunshine = Sunshine(app)
    run_application(app)


if __name__ == "__main__":
    sunshine_test()


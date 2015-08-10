#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-06-10 12:23:52
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import os
import logging
from flask import Blueprint, render_template, request
from flask.views import MethodView
from plugins import load
import urllib


class Sunshine(object):
    URLS = [ ]
    PLUGINS = [ ]

    def __init__(self, app, plugin_dir, blueprints_dir=None):
        self.app = app
        self.plugin_dir = plugin_dir
        self.blueprints_dir = blueprints_dir
        self.load_plugin()
        self.logurls()

        self.load_blueprint()

    def load_blueprint(self):
        if self.blueprints_dir is None:
            return

        bps_infos = load(self.blueprints_dir, 'app_bp')
        for name, bps in bps_infos.items():
            bp = bps[1]
            self.app.register_blueprint(bp)

        output = [" "]
        for rule in self.app.url_map.iter_rules():
            methods = ','.join(rule.methods)
            if rule.rule == rule.endpoint:
                continue
            line = urllib.unquote("{:30s} {:30s} {}".format(rule, methods, rule.endpoint))
            output.append(line)

        output = sorted(output)
        logging.info("\n".join(output))


    def load_plugin(self):
        mode_infos = load(self.plugin_dir, 'name', 'urls')

        for model, name, urls in mode_infos.values():
            self.init_mode(model, name, urls)

        self.__add_url()

    def groups(self, urls):
        i = 0
        t = []
        while i < len(urls):
            t.append((urls[i], urls[i+1]))
            i = i + 2
        return t

    def init_mode(self, model, name, urls):
        for url, fun in self.groups(urls):
            if url.startswith("/"):
                url = "/%s%s"%(name, url)
            else:
                url = os.path.join("/", name, url)

            if isinstance(fun, basestring):
                if not hasattr(model, fun):
                    logger.error("plugin %s not hasattr [%s]"%(model, fun))
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
            self.register_api(fun, url)

    def register_api(self,view, url):
        view_func = view.as_view(url)
        self.app.add_url_rule(url, view_func=view_func,
                         methods=['GET','PUT', 'DELETE','POST'])


class ClassViews(MethodView):
    """
    重构dispatch_request方法, 使其兼容视图函数中方法的大小写

    """
    def dispatch_request(self, *args, **kwargs):
        method = request.method.lower()

        if not hasattr(self, method):
            meth = getattr(self, method.upper(), None)
        else:
            meth = getattr(self, method, None)

        # if the request method is HEAD and we don't have a handler for it
        # retry with GET
        if meth is None and request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        assert meth is not None, 'Unimplemented method %r' % request.method
        return meth(*args, **kwargs)

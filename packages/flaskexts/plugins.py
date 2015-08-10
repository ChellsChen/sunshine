#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-05-26 11:26:30
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import sys
import os
import re
import logging
import imp

__MODULES = {}
__INDEX = 0

def load(path, *attrs):
    infos = {}
    modes = os.listdir(path)

    for m in modes:
        if not m.endswith('.py'):
            continue

        if m == "__init__.py":
            continue

        p = os.path.join(path, m)
        tm = imp.load_source(p[0:-3], p)

        info = __mode_init(tm, attrs)
        if info:
            infos[m[0:-3]] = info

    return infos

def __mode_init(mode, attrs):
    info = [mode]
    for attr in attrs:
        if not hasattr(mode, attr):
            logging.error("mode init:%s not hasattr [%s]" % (mode, attr))
            return []
        info.append(getattr(mode, attr))
    return info

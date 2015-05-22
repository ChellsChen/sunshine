#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-05-05 18:09:04
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import os
from setting import *

def load_config():
    """Load config."""
    mode = os.environ.get('MODE')
    try:
        if mode == 'PRODUCTION':
            from .production import ProductionConfig
            return ProductionConfig
        elif mode == 'TESTING':
            from .testing import TestingConfig
            return TestingConfig
        else:
            from .development import DevelopmentConfig
            return DevelopmentConfig
    except ImportError:
        from .default import Config
        return Config


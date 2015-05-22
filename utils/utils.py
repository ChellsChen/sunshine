#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-05-19 17:17:09
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import os

import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15]))[20:24])

# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: throttle.py
@time: 2020/10/22 13:10
@desc:
"""
from rest_framework.throttling import SimpleRateThrottle


class VisitThrottle(SimpleRateThrottle):
    rate = "5/m"

    # scope = "anonymous"

    def get_cache_key(self, request, view):
        return self.get_ident(request)

# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: authentication.py
@time: 2020/10/22 10:10
@desc:
"""

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


class MyAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN', None)
        user = 'abel'
        # print(user)
        # print(token)
        if token:
            return user, token
        raise exceptions.AuthenticationFailed(detail={'code': -1, 'info': '认证失败哦'})

    def authenticate_header(self, request):
        super().authenticate_header(request)

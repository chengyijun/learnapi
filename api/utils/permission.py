# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: MyPermission.py
@time: 2020/10/22 12:58
@desc:
"""
from rest_framework import exceptions
from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):

    def has_permission(self, request, view):
        params = request.query_params
        user_type = params.get('user_type', None)
        if user_type == '1':
            return True
        raise exceptions.PermissionDenied(detail={'code': -1, 'msg': '您没有权限哦'})

# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: version.py
@time: 2020/10/22 13:41
@desc:
"""
from rest_framework import exceptions
from rest_framework.versioning import BaseVersioning


class MyVersion(BaseVersioning):
    default_version = 'v1'
    allowed_versions = ['v1', 'v2']
    version_param = 'version'

    def is_allowed_version(self, version):
        print(111)
        print(version)
        print(self.allowed_versions)
        if version in self.allowed_versions:
            return True
        raise exceptions.APIException(detail={'code': -1, 'msg': '错误的版本号'})

    def determine_version(self, request, *args, **kwargs):
        version = request.query_params.get('version', None)
        self.is_allowed_version(version=version)
        return version, self.__class__

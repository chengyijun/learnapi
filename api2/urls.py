# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: urls.py
@time: 2020/10/19 10:36
@desc:
"""
from django.urls import path

from api2.views import TestView

app_name = 'api2'
urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
]

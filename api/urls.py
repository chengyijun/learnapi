# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: urls.py
@time: 2020/10/19 10:36
@desc:
"""
from django.urls import path

from api.views import TestView, BookView, BookDetailView, BookUpdateView, BookDeleteView

app_name = 'api'
urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path('books/', BookView.as_view(), name='books'),
    # re_path(r'^book/(?P<book_id>\d+)/$', BookView.as_view(), name='book')
    path('book/<int:id>/', BookDetailView.as_view(), name='book'),
    path('update/<int:id>/', BookUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', BookDeleteView.as_view(), name='delete'),
]

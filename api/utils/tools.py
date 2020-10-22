# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: tools.py
@time: 2020/10/22 10:55
@desc:
"""
import hashlib


def md5(data):
    return hashlib.md5(bytes(data, encoding='utf-8')).hexdigest()


def main():
    pass


if __name__ == '__main__':
    main()

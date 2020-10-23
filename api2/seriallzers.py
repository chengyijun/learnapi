# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: seriallzers.py
@time: 2020/10/23 11:15
@desc:
"""
from rest_framework import serializers

from api2.models import UserInfo


class UserSerializer(serializers.Serializer):
    # source 指定了与数据库中字段的对应关系   默认不指明的情况下 字段名起的必须和数据库字段名一致， 通过source就可以把字段起别名
    type = serializers.IntegerField(source='user_type')
    user_type = serializers.CharField(source='get_user_type_display')  # choices字段显示
    username = serializers.CharField()
    pwd = serializers.CharField(source='password')  # 自定义serializer中的key值
    group_title = serializers.CharField(source='group.title')  # 关联对象属性
    roles = serializers.CharField(source='roles.all')  # 多对多关系
    roles_info = serializers.SerializerMethodField()  # 表示自定义方法，显示querytset对象详情

    def get_roles_info(self, row):
        roles = row.roles.all()
        ret = []
        for item in roles:
            ret.append(
                {
                    'id': item.id,
                    'title': item.title
                }
            )
        return ret


class UserModelSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(source='get_user_type_display')
    roles = serializers.CharField(source='roles.all')  # 外键关联
    roles_info = serializers.SerializerMethodField()  # 表示自定义方法，显示外键关联详情
    group_title = serializers.CharField(source='group.title')

    def get_roles_info(self, row):
        roles = row.roles.all()
        ret = []
        for item in roles:
            ret.append(
                {
                    'id': item.id,
                    'title': item.title
                }
            )
        return ret

    class Meta:
        model = UserInfo
        # fields = '__all__'  # 为全部的字段做匹配
        # 这里的字段过滤  只能过滤数据库里的字段  序列化类里定义的自定义字段是过滤不了的
        fields = ['id', 'user_type', 'username', 'password', 'group', 'group_title', 'roles',
                  'roles_info']  # 自定义需要展示的字段
        # extra_kwargs = {'group': {'source': 'group_id'}}
        # depth = 1 默认是0  只对表字段有效 对自定义字段无效

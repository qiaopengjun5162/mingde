"""
@Project  : mingdeapi
@Author   : QiaoPengjun
@Time     : 2023/6/26 11:49
@Software : PyCharm
@File     : serializers.py
"""
from rest_framework import serializers
from .models import Nav


class NavModelSerializer(serializers.ModelSerializer):
    """
    导航菜单的序列化器
    """
    class Meta:
        model = Nav
        fields = ["name", "link", "is_http"]

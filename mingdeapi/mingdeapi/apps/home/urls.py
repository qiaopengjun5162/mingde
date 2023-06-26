"""
@Project  : mingdeapi
@Author   : QiaoPengjun
@Time     : 2023/4/18 10:02
@Software : PyCharm
@File     : urls.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path("nav/header/", views.HeaderNavListAPIView.as_view()),
    path("nav/footer/", views.FooterNavListAPIView.as_view()),
]

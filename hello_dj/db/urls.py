#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:zhongxin 
#datetime:2018/11/10 9:02 AM 
# coding=utf-8
# Auth:zx
# Time:2018/10/30 0030 22:12
from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.test),
    path('test22/',views.test22),
    path('test3/',views.test3),
]

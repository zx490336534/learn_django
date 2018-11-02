# coding=utf-8
# Auth:zx
# Time:2018/11/2 0002 21:20

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),

]

# coding=utf-8
# Auth:zx
# Time:2018/11/18 0018 20:39

from django.urls import path
from . import views

urlpatterns = [
    path('get_test/', views.get_test),
    path('post_test/', views.post_test),
    path('upload_test/', views.upload_test),
    path('set_ck/', views.set_ck),
    path('get_ck/', views.get_ck),
    path('delete_ck/', views.delete_ck),
]

# coding=utf-8
# Auth:zx
# Time:2018/11/18 0018 20:39

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login_test, name='login_test'),
    path('logout/', views.logout_test, name='logout_test'),
    path('register/', views.register, name='register'),
]

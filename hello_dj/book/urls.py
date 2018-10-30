# coding=utf-8
# Auth:zx
# Time:2018/10/30 0030 22:12
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.book_index),
    path('test/', views.book_test),
    path('article/', views.article),
    path('article_new/', views.article_new,name='new_article'),
]

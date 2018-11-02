# coding=utf-8
# Auth:zx
# Time:2018/10/30 0030 22:12
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='book_index'),
    path('test/<book_name>/', views.book_test, name='book_test'),
    path('article/', views.article),
    path('article_new/', views.article_new, name='new_article'),
    path('static_test/', views.static_test),
    path('tag_test/', views.tag_test),
]

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
    path('add/',views.add_user),
    path('add1/',views.add_user1),
    path('add2/',views.add_user2),
    path('add3/',views.add_user3),
    path('search/',views.search_user),
    path('delete/',views.delete_user),
    path('update/',views.update_user),
    path('f_test/',views.f_test),
]

# coding=utf-8
# Auth:zx
# Time:2018/11/13 0013 22:05

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='blog_index'),
    path('add/', views.add, name='blog_add'),
    path('list/', views.list, name='blog_list'),
    path('detail/<blog_id>', views.detail, name='blog_detail'),
    path('edit/<blog_id>', views.edit, name='blog_edit'),
    path('delete/<blog_id>', views.delete, name='blog_delete'),
]

# coding=utf-8
# Auth:zx
# Time:2018/11/13 0013 22:05

from django.urls import path
from . import views
from . import cls_views

urlpatterns = [
    path('index/', views.index, name='blog_index'),
    path('add/', views.add, name='blog_add'),
    path('list/', views.list, name='blog_list'),
    path('detail/<blog_id>', views.detail, name='blog_detail'),
    path('edit/<blog_id>', views.edit, name='blog_edit'),
    path('delete/<blog_id>', views.delete, name='blog_delete'),

    # 类视图
    path('cls_add/', cls_views.Blog_add.as_view(), name='cls_add'),
    path('cls_index/', cls_views.Blog_index.as_view(), name='cls_index'),
    path('cls_list/', cls_views.Blog_list.as_view(), name='cls_list'),
    path('cls_detail/<blog_id>', cls_views.Blog_detail.as_view(), name='cls_detail'),
]

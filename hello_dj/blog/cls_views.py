# coding=utf-8
# Auth:zx
# Time:2018/11/18 0018 21:36

from django.views import View
from django.shortcuts import render, redirect, reverse
from .models import BlogModel
from django.views.generic import TemplateView, ListView, DetailView


class Blog_add(View):
    def get(self, request):
        return render(request, 'blog/demo_add.html')

    def post(self, request):
        print(request.POST)
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog = BlogModel(title=title, content=content)
        blog.save()
        return redirect(reverse('cls_add'))  # 重定向到原页面


class Blog_index(TemplateView):
    template_name = 'blog/demo_index.html'


class Blog_list(ListView):
    template_name = 'blog/demo_list.html'  # 模板路径
    context_object_name = 'blog_list'  # 上下文传给模板变量
    model = BlogModel  # 对应模型类


class Blog_detail(DetailView):
    template_name = 'blog/demo_detail.html'
    context_object_name = 'blog'
    model = BlogModel
    pk_url_kwarg = 'blog_id'  # url传进来的id

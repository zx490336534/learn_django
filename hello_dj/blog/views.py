from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import BlogModel
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.

@login_required
def index(request):
    return render(request, 'blog/demo_index.html')

@permission_required('blog.add_blogmodel')
def add(request):
    if request.method == 'GET':
        return render(request, 'blog/demo_add.html')
    elif request.method == 'POST':
        print(request.POST)
        # <QueryDict: {'csrfmiddlewaretoken': ['alZY98GpyeMsjggSbUO0EL5Guynd6WW8wtXlxvE10lYmBCNw1J2A9IJQzQ26LZbY'], 'title': ['我是钟鑫'], 'content': ['啊啊啊啊']}>
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog = BlogModel(title=title, content=content)
        blog.save()
        return redirect(reverse('blog_add'))  # 重定向到原页面


def list(request):
    blog_list = BlogModel.objects.all()
    return render(request, 'blog/demo_list.html', context={'blog_list': blog_list})


def detail(request, blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    return render(request, 'blog/demo_detail.html', context={'blog': blog})


def edit(request, blog_id):
    blog = BlogModel.objects.filter(id=blog_id)[0]
    if request.method == 'POST':
        if blog:
            title = request.POST.get('title')
            content = request.POST.get('content')
            blog.title = title
            blog.content = content
            blog.save()
            return render(request, 'blog/demo_detail.html', context={'blog': blog})
    return render(request, 'blog/demo_edit.html', context={'blog': blog})


def delete(request, blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    if blog:
        blog.delete()
        return redirect(reverse('blog_list'))
    else:
        return HttpResponse('没有这篇博客')

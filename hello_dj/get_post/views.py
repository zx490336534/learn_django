import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from hello_dj.settings import MEDIA_ROOT


def post_test(request):
    print(request.POST)
    if request.method == 'GET':
        return render(request, 'get_post/get_post_test.html')
    elif request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        x = a + b
        return HttpResponse(x)


def get_test(request):
    print(request.GET)
    a = request.GET.get('a')
    # a = request.GET.getlist('a') #同个名字多个
    b = request.GET.get('b')
    print(a, b)
    return render(request, 'get_post/get_post_test2.html')


def upload_test(request):
    if request.method == 'GET':
        return render(request, 'get_post/upload.html')
    elif request.method == 'POST':
        print(request.FILES)
        f = request.FILES['file']
        print(f.name)
        f_name = os.path.join(MEDIA_ROOT, f.name)
        with open(f_name, 'wb') as ff:
            for c in f.chunks():
                ff.write(c)
        return HttpResponse('XXX')


def response_test(request):
    rs = HttpResponse('HAHAHAHA')
    return rs


def set_ck(request):
    response = HttpResponse('设置cookie')
    response.set_cookie('name','zhongxin') #默认浏览器关闭过期
    response.set_cookie('name1','zhongxin1',max_age=200) #多少秒
    response.set_cookie('name2','zhongxin2',expires=datetime.datetime(2018,11,20))
    return response

def get_ck(request):
    cookie = request.COOKIES
    print(cookie)
    print(cookie.get('name1'))
    return HttpResponse('获取cookie')

def delete_ck(request):
    rs = HttpResponse('删除Cookie')
    rs.delete_cookie('name')
    return rs
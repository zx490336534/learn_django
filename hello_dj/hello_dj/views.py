# coding=utf-8
# Auth:zx
# Time:2018/10/30 0030 22:02
from django.http import HttpResponse


def hello(request):
    return HttpResponse('hello django!')


def hello_taka(request):
    return HttpResponse('hello taka')


def hello_test(request, name, age):
    return HttpResponse('hello %s , 今年%s' % (name, age))

def re_test(request):
    return HttpResponse('测试re_test')
# MTV
# model template views
# MVC
# model template Contrl

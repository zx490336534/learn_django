from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.
import datetime


def book_index(requests, **kwargs):
    if kwargs.get('switch') == 'true':
        print(datetime.datetime.now())
    return HttpResponse('这是book的主页')


from django.template.loader import get_template


def book_test(request, **kwargs):
    t = get_template('book/index.html')
    html = t.render()
    return HttpResponse(html)
    # return HttpResponse('hhhhh')


ls = [1, 2, 3]
dt = {'a': 11, 'b': 22, 'c': 33}
tp = 4, 5, 6


def xx():
    return 'hello django'


class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def say(self):
        return '哈哈哈哈'


ap = Fruits('Apple', 'red')


def index(request, **kwargs):
    name = 'taka'
    return render(request, 'book/book_index.html', context={'name': name,
                                                            'age': 18,
                                                            'ls': ls,
                                                            'dict': dt,
                                                            'ap': ap,
                                                            'str': 'THIS IS A LIST!',
                                                            'html':'<h1>Hello django</h1>',
                                                            'float':3.1415926,
                                                            'now':datetime.datetime.now,#加括号现在调用，不加括号在模板里调用
                                                            })


def article(request, **kwargs):
    if kwargs.get('switch') == 'true':
        # return redirect('/book/article_new')
        return redirect(reverse('new_article'))
    return HttpResponse('这是老页面')


def article_new(request, **kwargs):
    return HttpResponse('这是新页面')

def static_test(request,**kwargs):
    return render(request,'book/static_test.html')
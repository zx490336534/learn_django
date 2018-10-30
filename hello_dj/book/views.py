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


def index(request, **kwargs):
    name = 'taka'
    return render(request, 'book/index.html', context={'name': name})


def article(request, **kwargs):
    if kwargs.get('switch') == 'true':
        # return redirect('/book/article_new')
        return redirect(reverse('new_article'))
    return HttpResponse('这是老页面')


def article_new(request, **kwargs):
    return HttpResponse('这是新页面')

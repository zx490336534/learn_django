from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime
def book_index(requests,**kwargs):
    if kwargs.get('switch') == 'true':
        print(datetime.datetime.now())
    return HttpResponse('这是book的主页')

def book_test(request):
    return HttpResponse('hhhhh')
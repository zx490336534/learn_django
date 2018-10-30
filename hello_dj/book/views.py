from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def book_index(requests):
    return HttpResponse('这是book的主页')

def book_test(request):
    return HttpResponse('hhhhh')
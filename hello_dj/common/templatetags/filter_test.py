# coding=utf-8
# Auth:zx
# Time:2018/11/2 0002 21:51
from django import template

register = template.Library()


@register.filter
def my_lower(value):
    return value.lower()


@register.filter
def my_cut(value, arg):
    return value.replace(arg, '')

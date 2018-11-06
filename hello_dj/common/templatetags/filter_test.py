# coding=utf-8
# Auth:zx
# Time:2018/11/2 0002 21:51
import datetime
from django import template

register = template.Library()


@register.filter
def my_lower(value):
    return value.lower()


@register.filter
def my_cut(value, arg):
    return value.replace(arg, '')


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag(takes_context=True)
def current_time2(context):
    format_string = context.get('format_string')
    return datetime.datetime.now().strftime(format_string)

@register.inclusion_tag('music/show_tag.html')
def show_results1():
    xx = ['taka','xiaopo','feifei']
    return {'choices':xx}

@register.inclusion_tag('music/show_tag.html')
def show_results2(xx):
    return {'choices':xx}

@register.inclusion_tag('music/show_tag.html',takes_context=True)
def show_results3(context):
    xx = context.get('ls')
    return {'choices':xx}
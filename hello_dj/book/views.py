from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.
import datetime
from .models import User
from django.http import HttpResponse


def book_index(requests, **kwargs):
    if kwargs.get('switch') == 'true':
        print(datetime.datetime.now())
    return HttpResponse('这是book的主页')


from django.template.loader import get_template


def book_test(request, book_name, **kwargs):
    t = get_template('book/index.html')
    html = t.render({'book_name': book_name})
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
                                                            'name2': None,

                                                            'age': 18,
                                                            'num1': 12,
                                                            'num2': 13,
                                                            'ls': ls,
                                                            'dict': dt,
                                                            'ap': ap,
                                                            'str': 'THIS IS A LIST!',
                                                            'html': '<h1>Hello django</h1>',
                                                            'float': 3.1415926,
                                                            'now': datetime.datetime.now,  # 加括号现在调用，不加括号在模板里调用
                                                            })


def article(request, **kwargs):
    if kwargs.get('switch') == 'true':
        # return redirect('/book/article_new')
        return redirect(reverse('new_article'))
    return HttpResponse('这是老页面')


def article_new(request, **kwargs):
    return HttpResponse('这是新页面')


def static_test(request, **kwargs):
    return render(request, 'book/static_test.html')


def tag_test(request, **kwargs):
    return render(request, 'book/tag_test.html',
                  context={'ls': ls,
                           'tp': tp,
                           'name': 'taka',
                           'html': '<h1>Hello django</h1>',
                           'num1': 12,
                           'num2': 24,

                           })


def add_user(request, **kwargs):
    # 方法一
    taka = User(name='taka', age=18)
    taka.save()
    return HttpResponse('添加数据成功')


def add_user1(request, **kwargs):
    # 方法二
    moran = User()
    moran.name = '墨染'
    moran.age = 18
    moran.save()
    return HttpResponse('添加数据成功1')


def add_user2(request, **kwargs):
    # 方法三
    User.objects.create(name='句号', age=19)
    return HttpResponse('添加数据成功2')


def add_user3(request, **kwargs):
    # 方法四
    User.objects.get_or_create(name='句号1', age=20)  # 判断存在的时候不添加
    return HttpResponse('添加数据成功3')


def search_user(request, **kwargs):
    rs = User.objects.all()  # 防护queryset对象
    print(rs[0])  # 索引取值
    print('id:', rs[0].id)
    print('name:', rs[0].name)
    print('age:', rs[0].age)
    print(rs.filter())  # 第一条数值
    print(rs.last())  # 最后一条数值
    rs = User.objects.get(id=2)  # 类实例对象，表里面的一条数据
    # rs = User.objects.get(name='句号1') #有多个会报错
    print(rs)
    print(rs.name)

    rs = User.objects.filter(name='句号1')  # queryset对象
    print(rs)

    return HttpResponse('查询数据成功')


def delete_user(request, **kwargs):
    User.objects.filter(name='句号1').delete() #多个都会被删除
    User.objects.get(id=1).delete() #查询到了就可以删除
    return HttpResponse('删除数据成功')


def update_user(request, **kwargs):
    User.objects.filter(name='句号').update(name='皮皮')
    rs = User.objects.get(name='墨染')
    rs.name = '黑炭'
    rs.save()
    return HttpResponse('更新数据成功')
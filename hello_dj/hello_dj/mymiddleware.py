# coding=utf-8
# Auth:zx
# Time:2018/11/20 0020 22:16

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from form_test.models import UserModel


class MyException(MiddlewareMixin):
    def process_exception(self, request, exception):
        print('自定义的异常处理中间件')
        return HttpResponse(exception)

        # request 增加一个属性


class UserMiddleware:
    def __init__(self, get_request):
        self.get_response = get_request

    def __call__(self, request):
        name = request.session.get('username', '游客')
        user = UserModel.objects.filter(username=name).first()
        if user:
            setattr(request, 'myuser', user.username)  # 设置属性
        else:
            setattr(request, 'myuser', '未登录')
        # 上面是request到达视图之前的

        # 下面部分就是response到达用户浏览器之前执行的
        response = self.get_response(request)
        return response

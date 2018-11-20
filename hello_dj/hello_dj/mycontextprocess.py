# coding=utf-8
# Auth:zx
# Time:2018/11/20 0020 22:35
from form_test.models import UserModel


def myuser(request):
    name = request.session.get('username', '游客')
    user = UserModel.objects.filter(username=name).first()
    if user:
        return {'myuser': user.username}
    else:
        return {}

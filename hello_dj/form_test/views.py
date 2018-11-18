from django.shortcuts import render, redirect, reverse


# Create your views here.


def home(requset):
    # 显示谁登陆了
    # name = 'zhongxin'
    name = requset.session.get('username','游客')
    return render(requset, 'form_test/home.html', {'name': name})


def login_test(request):
    if request.method == 'GET':
        return render(request, 'form_test/login_test.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        request.session['username'] = username  # 状态保持
        return redirect(reverse('home'))


def logout_test(requset):
    requset.session.flush()
    return redirect(reverse('home'))

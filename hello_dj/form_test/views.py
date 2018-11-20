from django.shortcuts import render, redirect, reverse
from .forms import LoginForm, RegisterFrom
from .models import UserModel
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.


def home(requset):
    # 显示谁登陆了
    # name = 'zhongxin'
    print(requset.myuser)
    name = requset.session.get('username', '游客')
    return render(requset, 'form_test/home.html', {'name': name})


# def login_test(request):
#     if request.method == 'GET':
#         return render(request, 'form_test/login_test.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username')
#         request.session['username'] = username  # 状态保持
#         return redirect(reverse('home'))


def logout_test(requset):
    requset.session.flush()
    return redirect(reverse('home'))


def login_test(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user_login/login.html', context={'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = UserModel.objects.filter(username=username)
            if user:
                if check_password(password, user[0].password):
                    request.session['username'] = username
                    return redirect(reverse('home'))
                else:
                    return render(request, 'user_login/login.html', {'error': form.errors})
            else:
                return redirect(reverse('register'))
        else:
            return redirect(reverse('login_test'))


def register(request):
    if request.method == 'GET':
        form = RegisterFrom()
        return render(request, 'user_login/register.html', context={'form': form})
    elif request.method == 'POST':
        form = RegisterFrom(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            email = form.cleaned_data.get('email')
            if password == password_repeat:
                password = make_password(password)  # 加密
                UserModel.objects.create(username=username, password=password, email=email)
                return redirect(reverse('home'))
            else:
                return redirect(reverse('register'))
        else:
            return redirect(reverse('register'))

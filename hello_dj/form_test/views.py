from django.shortcuts import render, redirect, reverse
from .forms import LoginForm, RegisterFrom
from .models import UserModel
from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login, logout


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
    # requset.session.flush()
    logout(requset)
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
            # user = UserModel.objects.filter(username=username)
            user = authenticate(username=username, password=password)
            if user:
                # if check_password(password, user[0].password):
                #     request.session['username'] = username
                login(request, user)  # 保存状态
                next_url = request.GET.get('next')
                print(next_url)
                if next_url:
                    return redirect(next_url)
                else:
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
            # if password == password_repeat:
            #     password = make_password(password)  # 加密
            #     UserModel.objects.create(username=username, password=password, email=email)
            if password == password_repeat:
                User.objects.create_user(username=username, password=password, email=email)

                return redirect(reverse('login_test'))
            else:
                return redirect(reverse('register'))
        else:
            return redirect(reverse('register'))

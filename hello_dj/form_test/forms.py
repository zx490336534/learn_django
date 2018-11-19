# coding=utf-8
# Auth:zx
# Time:2018/11/18 0018 22:24
from django import forms


class RegisterFrom(forms.Form):
    username = forms.CharField(max_length=20, min_length=6)
    password = forms.CharField(max_length=8, min_length=6,
                               widget=forms.PasswordInput(attrs={'placeholder': '请输入密码'}),
                               error_messages={'min_length': '密码长度小于6',
                                               'max_length': '密码长度超过8了'})
    password_repeat = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()



class LoginForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=10)
    password = forms.CharField(max_length=8, min_length=6, widget=forms.PasswordInput())

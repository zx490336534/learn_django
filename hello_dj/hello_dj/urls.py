"""hello_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls'),{'switch':'true'})
    # path('hello/', views.hello),
    # path('hello_taka/', views.hello_taka),
    # path('hello/<name>/<int:age>/', views.hello_test),
    # re_path('^hello11/$',views.re_test),#正则匹配，http://123.56.13.233:8080/hello11/
    # path('book/', book_index),
]

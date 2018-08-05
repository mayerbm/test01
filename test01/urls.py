"""test01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    # project的初始化页面 http://ip:port/admin
    url(r'^admin/', include(admin.site.urls)),

    # 将app的urls添加到project的主urls,此处的namespace和视图函数的name可用作反向解析
    # 反向解析：链接由url的配置动态生成{% url 'namespace:name' p1 p2 %}
    # 优点：当变更url的正则匹配规则时,不需要手动更改应用里的链接,因为namespace和name并没有变
    url(r'^booktest/', include('booktest.urls', namespace='booktest'))
]

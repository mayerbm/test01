from django.conf.urls import url
from . import views

# 定义正则和对应的视图
urlpatterns = [

    # 正则表达式命名组：通过位置参数传递给视图
    url('^$', views.index, name='index'),
    # 正则表达式命名组：通过关键字参数 ?P<关键字> 传递给视图
    url('^(?P<id>\d+)/$', views.detail, name='detail'),

    # get请求
    url('^get01/$', views.get01, name='get01'),
    url('^get02/$', views.get02, name='get02'),
    url('^get03/$', views.get03, name='get03'),

    # post请求
    url('^post01/$', views.post01, name='post01'),
    url('^post02/$', views.post02, name='post02')
]
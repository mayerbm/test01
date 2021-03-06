from django.conf.urls import url
from . import views

# 定义正则和对应的视图
urlpatterns = [

    # 正则表达式命名组：通过位置参数传递给视图
    url('^$', views.index01, name='index01'),
    # 正则表达式命名组：通过关键字参数 ?P<关键字> 传递给视图
    url('^(?P<id>\d+)/$', views.detail01, name='detail01'),
    url('^(?P<id1>\d+)/(?P<id2>\d+)/$', views.detail02, name='detail02'),

    # get请求
    url('^get01/$', views.get01, name='get01'),
    url('^get02/$', views.get02, name='get02'),
    url('^get03/$', views.get03, name='get03'),

    # post请求
    url('^post01/$', views.post01, name='post01'),
    url('^post02$', views.post02, name='post02'),

    # cookie测试
    url('^cookie01/$', views.cookie01, name='cookie'),

    # 重定向测试
    url('^redirect01/$', views.redirect01, name='redirect01'),

    # session测试
    url('^homepage/$', views.homepage, name='homepage'),
    url('^loginpage$', views.loginpage, name='loginpage'),
    url('^login$', views.login, name='login'),
    url('^logout$', views.logout, name='logout'),

    # DTL测试
    url('^test01/$', views.test01, name='test01'),

    # 模板继承
    url('^user01/$', views.user01, name='user01'),
    url('^user02/$', views.user02, name='user02'),

    # html转义
    url('^html01/$', views.html01, name='html01'),

    # csrf跨域攻击
    url('^csrf01/$', views.csrf01, name='csrf01'),
    url('^csrf02$', views.csrf02, name='csrf02'),

    # 静态文件
    url('^static01/$', views.static01, name='static01'),

    # 中间件
    url('^myexc/$', views.myexc, name='myexc'),

    # 上传图片
    url('^uploadpage/$', views.uploadpage, name='uploadpage'),
    url('^upload$', views.upload, name='upload'),

    # 分页(此处匹配页码用的是\d*而不是\d+,一般不写页码的话默认是第一页)
    url('^paging/(?P<num>\d*)$', views.paging, name='paging'),

    # 文本编辑器
    url('^editor01$', views.editor01, name='editor01'),
    url('^editor02$', views.editor02, name='editor02'),

    # 缓存
    url('^cache01$', views.cache01, name='cache01'),
    url('^cache02$', views.cache02, name='cache02'),
    url('^cache03$', views.cache03, name='cache03'),
]
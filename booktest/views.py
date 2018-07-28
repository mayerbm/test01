"""
视图是MVT框架的核心部分,负责：接收请求-->获取数据-->返回结果
Django通过视图接收请求,通过模型获取数据,然后调用模板展示

views
1、视图是定义在views.py中的函数,接收request对象(包含请求信息)作为第一个参数
   Django提供了render()函数简化视图调用模板、构造上下文
2、定义完视图需要配置urlconf才能正常处理请求：
   urlconf包括正则表达式、视图两部分;Django使用正则匹配请求的URL,一旦匹配成功就会调用对应的视图
   注意：正则只匹配路径部分(即去除域名和参数的字符串)
   每个app都会有单独的urls.py文件,然后将各个app的urls添加到project的urls.py文件

templates
1、在project根目录下创建templates目录, 并在settings.py中设置TEMPLATES的DIRS值
2、在templates目录下创建booktest目录存放booktest应用各个视图的html页面, 并根据视图中传递的数据填充值
  {%执行代码段%}
  {{输出值：可以是变量,也可以是对象.属性}}

"""

from django.shortcuts import render
from .models import Book
from django.db.models.aggregates import *
from django.db.models import F, Q

# Create your views here.


# 创建视图
def index(request):

    # 该视图使用的模板名称
    template_name = 'booktest/index.html'

    # books = Book.manager1.all()
    # books = Book.manager1.filter(title__startswith="天")
    # books = Book.manager1.filter(reading__lt=F('comments'))
    books = Book.manager1.filter(Q(title__contains="龙") | Q(pub_time__year=1980))

    # contet(字典类型): 该视图展示的上下文
    context = {"books": books}

    # 渲染结果
    return render(request, template_name=template_name, context=context)


# 创建视图
def detail(request):

    # 该视图使用的模板名称
    template_name = 'booktest/detail.html'

    # 该视图展示的上下文
    context = {"heros": Book.manager1.get(pk=1).hero_set.all()}

    # 渲染结果
    return render(request, template_name=template_name, context=context)
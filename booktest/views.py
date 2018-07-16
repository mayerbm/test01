"""
视图是MVT框架的核心部分,负责：接收请求-->获取数据-->返回结果
Django通过视图接收请求,通过模型获取数据,然后调用模板展示

views
1、视图是定义在views.py中的函数,接收request对象(包含请求信息)作为第一个参数
   Django提供了render()函数简化视图调用模板、构造上下文
2、定义完视图需要配置urlconf才能正常处理请求：
   urlconf包括正则表达式、视图两部分;Django使用正则匹配请求的URL,一旦匹配成功就会调用对应的视图
   注意：正则只匹配路径部分(去除域名和参数的字符串)
   每个app都会有单独的urls.py文件,然后将各个app的urls添加到project的urls.py文件

templates
1、在project根目录下创建templates目录,然后在settings.py中设置TEMPLATES的DIRS
2、在templates目录下创建booktest目录存放各个视图的html页面,并根据视图中传递的数据填充值
  {%执行代码段%}
  {{输出值：可以是变量,也可以是对象.属性}}


自定义管理器作用：
1、更改默认查询结果
2、定义一个模型类创建方法

管理器和模型类的关系：
模型类相当于数据库表中的数据, 一个model对象就对应一条数据；
管理器用于Django中的对象与数据库表的交互映射

管理器作用就相当于MVC框架中的ORM, 
将管理器对象作为模型类的一个属性, 模型类的默认管理器是objects

先定义模型类, 再定义管理器, 然后将管理器作为模型类的属性
"""

from django.shortcuts import render
from .models import Book

# Create your views here.


# 创建视图
def index(request):

    # 该视图使用的模板名称
    template_name = 'booktest/index.html'

    # contet(字典类型): 该视图展示的上下文
    context = {"booklist": Book.objects.all()}

    # 渲染结果
    return render(request, template_name=template_name, context=context)


# 创建视图
def detail(request):

    # 该视图使用的模板名称
    template_name = 'booktest/detail.html'

    # 该视图展示的上下文
    context = {"herolist": Book.objects.get(pk=7).hero_set.all()}

    # 渲染结果
    return render(request, template_name=template_name, context=context)
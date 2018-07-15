"""
在django中, 视图对WEB请求进行回应
视图接收reqeust对象作为第一个参数, 包含了请求的信息
视图就是一个Python函数, 被定义在views.py中

通过视图接收请求，通过模型获取数据，然后调用模板展示

自定义管理器作用：
1、更改默认查询结果
2、定义一个模型类创建方法


管理器和模型类的关系：
模型类相当于数据库表中的数据，一个model对象就对应一条数据；
管理器用于Django中的对象与数据库表的交互映射

管理器作用就相当于MVC框架中的ORM，
将管理器对象作为模型类的一个属性，模型类的默认管理器是objects


先定义模型类，再定义管理器，然后将管理器作为模型类的属性
"""

from django.shortcuts import render
from .models import Book, Hero

# Create your views here.


# 创建视图
def index(request):

    # 该视图使用的模板名称
    template_name = 'booktest/index.html'

    # contet(字典类型): 该视图展示的上下文
    context = {"booklist": Book.objects.all()}

    # 渲染视图
    return render(request, template_name=template_name, context=context)


# 创建视图
def detail(request):

    # 该视图使用的模板名称
    template_name = 'booktest/detail.html'

    # 该视图展示的上下文
    context = {"herolist": Book.objects.get(pk=6).hero_set.all()}

    # 渲染视图
    return render(request, template_name=template_name, context=context)
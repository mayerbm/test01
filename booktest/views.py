"""
在django中, 视图对WEB请求进行回应
视图接收reqeust对象作为第一个参数, 包含了请求的信息
视图就是一个Python函数, 被定义在views.py中

通过视图接收请求，通过模型获取数据，然后调用模板展示
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
"""
视图是MVT框架的核心部分,负责：接收请求-->获取数据-->返回结果
Django通过视图接收请求,通过模型获取数据,然后调用模板展示结果

views
1、视图是定义在views.py中的函数,接收request对象(包含请求信息)作为第一个参数,Django提供了render()函数简化了视图调用模板、构造上下文
2、定义完视图需要配置对应的urlconf,每个app都会有单独的urls.py文件,然后将各个app的urls添加到project的urls.py文件
urlconf包括正则表达式和视图两部分 --> Django使用正则匹配请求的URL,一旦匹配成功就会调用对应的视图
注意：正则只匹配路径部分(即去除域名和参数的字符串)
http://192.168.233.11:7777/booktest/1/?i=1&j=2 --> 只匹配/booktest/1/部分
匹配过程：先与主URLconf匹配,成功后再用剩余部分与应用中的URLconf匹配
先拿'booktest/'匹配project中的urls.py, 再拿'1/'匹配app中的urls.py

HttpRequest对象
    服务器接收http协议的请求后,会根据报文创建HttpRequest对象,并将其作为视图函数的第一个参数
    GET属性: 一个类字典对象,包含get请求方式的所有参数
    POST属性: 一个类字典对象,包含post请求方式的所有参数
    COOKIES属性: 一个标准的Python字典,包含所有的cookie,键和值都为字符串
    session属性: 一个既可读又可写的类字典对象,表示当前的会话,只有当Django启用会话时才可用,详细内容见"状态保持"
    is_ajax()方法: 如果请求是通过XMLHttpRequest发起的,则返回True
QueryDict对象
    定义在django.http.QueryDict中,request对象的GET、POST属性都是QueryDict类型的对象,类似字典但是允许一键多值的情况
    get()：只能获取键的一个值,如果一个键同时拥有多个值则获取最后一个值
    getlist()：将键的多个值以列表返回
GET属性
    QueryDict类型的对象,包含get请求方式的所有参数,与url请求地址中的参数对应,位于?后面
    参数的格式是键值对: key1=value1,多个参数之间用&连接: key1=value1&key2=value2
    request.GET[key]/request.GET.get(key)、request.GET.getlist(key)
POST属性
    QueryDict类型的对象,包含post请求方式的所有参数,与form表单中的控件对应
    request.POST[key]/request.POST.get(key)、request.POST.getlist(key)
COOKIES属性
    python字典,服务器返回的存储在浏览器中的一小段文本文件
    response.set_cookie(key, value='', max_age=None)、request.COOKIES[key]、response.delete_cookie(key)

HttpResponse对象
    HttpRequest对象由Django自动创建,HttpResponse对象由开发人员创建
状态保持
    http协议是无状态的：客户端与服务器端的一次通信就是一次会话,每次请求都是一次新的请求而不会记得之前通信的状态
    实现状态保持的方式：在客户端(cookie)或服务器端(session)存储与会话有关的数据
    推荐使用session：所有数据存储在服务器端,在客户端cookie中存储session_id
    状态保持的目的是在一段时间内跟踪请求者的状态从而实现跨页面访问当前请求者的数据
    启用会话后，每个HttpRequest对象将具有一个session属性，它是一个类字典对象
使用session
    request.session.get(key, default=None)：根据指定键获取会话的值,若键不存在就给个默认值None
    request.session[key] = value：设置session值
    request.session.set_expiry(value)：设置session过期时间(s)--> 默认两个星期,value=0会话在浏览器关闭时失效,value=None会话永不过期
    request.session.has_key(key)：判断键是否存在
    del request.session[key]：指定键删除会话
    clear()：清除session_date的值
    flush()：删除当前的会话数据(连session_key一起删掉)并删除Cookie中的sessionid

templates
1、在project根目录下创建templates目录, 并在settings.py中设置TEMPLATES的DIRS值
2、在templates目录下创建booktest目录存放booktest应用各个视图的html页面, 并根据视图中传递的数据填充值
  {% 执行代码段 %}
  {{ 输出值：可以是变量,也可以是对象.属性 }}

步骤：定义视图函数-->配置urlconf-->设计html模板
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Book
from django.db.models import F, Q

# Create your views here.


def index(request):
    # 1、不调用模板直接返回
    # return HttpResponse("你好！")

    # 2、调用模板
    template_name = 'booktest/index.html'  # 模板名称
    books = Book.manager1.filter(Q(title__contains="龙") | Q(pub_time__year=1980) | Q(reading__gte=F("comments")))
    context = {"books": books}  # 构造字典类型的上下文(要往模板中传递的数据)

    # 先用loader加载模板再用render渲染模板
    # return HttpResponse(loader.get_template(template_name).render(context))

    # 可以用render函数简写
    return render(request, template_name, context)

# 包含关键字参数的请求
def detail01(request, id):
    # 构造上下文
    context = {"heros": Book.manager1.get(pk=id).hero_set.all()}
    # 渲染模板
    return render(request, "booktest/detail01.html", context)

# 包含多个关键字参数的请求
def detail02(request, id1, id2):
    # 构造上下文
    context = {"hero": Book.manager1.get(pk=id1).hero_set.get(pk=id2)}
    # 渲染模板
    return render(request, "booktest/detail02.html", context)


# GET请求
def get01(request):
    # 展示请求链接
    return render(request, "booktest/get01.html")

# 一键一值情况
def get02(request):
    # 根据键接收值
    a1 = request.GET["a"]  # 也可以写成request.GET.get("a")
    b1 = request.GET["b"]
    c1 = request.GET["c"]
    # 构造上下文
    context = {"a": a1, "b": b1, "c": c1}
    # 渲染模板
    return render(request, "booktest/get02.html", context)

# 一键多值情况
def get03(request):
    a1 = request.GET["a"]  # 3
    a2 = request.GET.getlist("a")  # ['1', '2', '3']
    context = {"a": a2}
    return render(request, "booktest/get03.html", context)


# POST请求
def post01(request):
    # 展示form表单
    return render(request, "booktest/post01.html")

def post02(request):
    # 根据键接收值
    name = request.POST["name"]
    pwd = request.POST["pwd"]
    age = request.POST["age"]
    gender = request.POST["gender"]
    hobby = request.POST.getlist("hobby")
    # 构造上下文
    context = {"name": name, "pwd": pwd, "age": age, "gender": gender, "hobby": hobby}
    # 渲染模板
    return render(request, "booktest/post02.html", context)


# COOKIE测试
def cookie01(request):
    # 创建HttpResponse对象
    response = HttpResponse()

    # 在响应头中添加cookie值,下次客户端再发请求的时候请求头中的Cookie就会包含该cookie值
    response.set_cookie("k", value="aaa", max_age=60)

    # 判断cookie值是否存在
    if 'k' in request.COOKIES:
        # 写在屏幕上
        response.write(request.COOKIES['k'])

    # 根据键删掉对应的cookie值
    # response.delete_cookie('k')

    # 返回响应结果
    return response


# redirect测试
def redirect01(request):
    # 重定向的地址要写绝对路径
    # return HttpResponseRedirect("/booktest/get01/")

    # 可以简写为redirect
    return redirect("/booktest/get01/")


# session测试
# 显示首页
def homepage(request):
    # uname = None  # 第一次访问时用户名为空
    uname = request.session.get('myname', default=None)  # 登录过后就应该有该用户的session信息了
    context = {"uname": uname}
    return render(request, "booktest/session01.html", context)

# 显示登录页
def loginpage(request):
    # 展示form表单
    return render(request, "booktest/session02.html")

# 登录
def login(request):
    # 接收post请求传入的参数uname
    uname = request.POST['uname']
    # 将uname存入session(django默认存放在数据库的django_session表中)
    request.session['myname'] = uname
    # 设置会话过期时间
    request.session.set_expiry(0)
    # 登录后转向初始页面
    return redirect("/booktest/homepage/")

# 退出
def logout(request):
    # 清除session_data
    # if request.session.has_key('myname'):
    #     del request.session['myname']  # 等价于request.session.clear()

    # 删除当前会话数据
    # request.session.flush()

    # 退出后转向初始页面
    return redirect("/booktest/homepage/")

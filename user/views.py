from django.shortcuts import render, redirect
from hashlib import sha1
from .models import UserInfo
# Create your views here.


# 注册
def register(request):
    # 展示注册页面
    return render(request, "user/register.html")

def register_handle(request):
    # 接收post请求传入的c参数
    post = request.POST
    name = post.get("user_name")
    pwd = post.get("pwd")
    cpwd = post.get("cpwd")
    email = post.get("email")

    # 判断两次密码是否一致
    if pwd != cpwd:
        # 重新注册
        return redirect("/user/register")
    else:
        # 给密码加密
        s1 = sha1()
        s1.update(pwd.encode('utf8'))
        pwd_new = s1.hexdigest()
        # 创建对象
        user = UserInfo()
        user.name = name
        user.pwd = pwd_new
        user.email = email
        user.save()
        # 注册成功,跳转到登录页面
        return redirect("/user/login")
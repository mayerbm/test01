#!/usr/bin/env python
"""
manage.py是一个命令行工具,可以使用多种方式和Django项目做交互

创建工程：django-admin startproject test01
创建应用：python manage.py startapp booktest
生成迁移文件：python manage.py makemigrations
执行迁移：python manage.py migrate
测试数据：python manage.py shell
启动服务器：python manage.py runserver ip:port
创建管理员用户：python manage.py createsuperuser
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test01.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

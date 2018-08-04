#!/usr/bin/env python
"""
manage.py是一个命令行工具,可以使用多种方式和Django项目做交互

创建工程：django-admin startproject test01
创建应用：python manage.py startapp booktest
生成迁移文件：python manage.py makemigrations
执行迁移：python manage.py migrate
测试数据：python manage.py shell
创建管理员用户：python manage.py createsuperuser
启动服务器：python manage.py runserver ip:port

常见错误：
1、django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb'(见models.py)
2、OSError: No translation files found for default language zh-CN
原因：新版本的django不支持zh-CN, 查看/home/.virtualenvs/django/lib/python3.6/site-packages/django/conf/locale目录下没有zh-CN
解决：修改settings.py --> LANGUAGE_CODE = 'zh-Hans'
3、DisallowedHost: Invalid HTTP_HOST header: '192.168.19.11:7777'. You may need to add '192.168.19.11' to ALLOWED_HOSTS.
解决：修改settings.py --> ALLOWED_HOSTS = ['*']
4、redis.exceptions.ConnectionError: Error -2 connecting to localhost:6379. Name or service not known.
解决：修改/etc/hosts --> 添加一行 127.0.0.1  localhost
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test01.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

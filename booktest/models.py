"""
model
有一个数据表就有一个模型类与之对应,模型类继承自models.Model类,输出对象时会调用对象的str方法

databases
错误：将数据库从sqlite3切换到mysql时：django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb'
原因：python2使用mysqldb连接mysql,python3使用pymysql连接mysql
解决：pip install pymysql,并在project的__init__.py文件添加
     import pymysql
     pymysql.install_as_MySQLdb()
1、修改settings.py文件的DATABASES
2、新建mysql库test01
3、删掉已经存在的迁移文件并重新执行迁移和生成迁移,此时test01库下会生成相关表
"""

from django.db import models


# Create your models here.

# 图书模型
class Book(models.Model):
    # 主键id是自增列会自动生成不用添加

    # 书名：varchar类型
    title = models.CharField(max_length=20)

    # 出版时间：DateTime类型
    pub_time = models.DateTimeField()

    # 自定义输出内容(此处更改并不影响数据表的字段映射,不需要重新生成数据表)
    def __str__(self):
        return '%s' % self.title


# 英雄模型
class Hero(models.Model):

    # 名字：varchar类型
    name = models.CharField(max_length=20)

    # 性别：boolean类型
    gender = models.BooleanField()

    # boolean值得显示结果是 '√' '×' ,可将其替换为中文或英文
    def sex(self):
        if self.gender:
            return '男'
        else:
            return '女'
    # sex.short_description = '性别'

    # 介绍：varchar类型
    introduce = models.CharField(max_length=50)

    # 所属书名：外键
    book = models.ForeignKey('Book')

    # 自定义输出内容
    def __str__(self):
        return '%s' % self.name

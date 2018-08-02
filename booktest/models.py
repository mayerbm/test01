"""
model
有一个数据表就有一个模型类与之对应,模型类继承自models.Model类,输出对象时会调用对象的str方法
一访问多 --> book.hero_set
一访问一 --> hero.book、hero.book_id

databases
错误：将数据库从sqlite3切换到mysql时：django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb'
原因：python2使用mysqldb连接mysql,python3使用pymysql连接mysql
解决：pip install pymysql,并在project的__init__.py文件添加
     import pymysql
     pymysql.install_as_MySQLdb()
1、修改settings.py文件的DATABASES
2、新建mysql库test01: create database test01 charset=utf8;
3、先删掉已经存在的迁移文件和数据库表,然后重新执行迁移和生成迁移,此时test01库下会重新生成相关表

manager
每个model都至少有一个管理器,管理器相当于MVC框架中的ORM,用来与数据库做交互
django默认管理器是objects,可以为模型类指定自定义管理器对象,此后objects将不存在
管理器作用：a、更改默认查询结果; b、定义一个模型类创建方法

步骤：定义模型类-->定义管理器-->将管理器作为模型类的属性
"""

from django.db import models


# Create your models here.

# 创建自定义管理器
class BookManager(models.Manager):

    # 1、修改默认查询集(通过filter等过滤器实现)
    def get_queryset(self):
        return super(BookManager, self).get_queryset().filter(isDelete=False)

    # 2、定义模型类对象创建方法(后续的RUD可由该对象实现)
    def create(self, title, pub_time):
        b = Book()
        b.title = title
        b.pub_time = pub_time
        b.reading = 0
        b.comments = 0
        b.isDelete = False
        return b


# 创建图书模型
class Book(models.Model):
    # 主键id是自增列, 自动生成不用添加

    # 书名：varchar类型
    title = models.CharField(max_length=20)
    # 出版时间：DateTime类型
    pub_time = models.DateTimeField()
    # 阅读量：Integer类型
    reading = models.IntegerField(default=0)
    # 评论数：Integer类型
    comments = models.IntegerField(default=0)
    # 逻辑删除：Boolean类型
    isDelete = models.BooleanField(default=False)

    # 定义元选项: 模型类在数据库中对应的表名默认是appname_modelname, 可以在Meta()类里面定义表的元数据信息
    class Meta():
        # 修改默认表名
        db_table = "book"

    # 自定义输出内容(此处更改并不影响数据表的字段映射,不需要重新生成数据表)
    def __str__(self):
        return '%s' % self.title

    # 将自定义管理器对象定义为对应模型类的属性
    # 管理器对象1
    manager1 = models.Manager()  # models.Manager()就等同于objects,返回的是默认的查询集
    # 管理器对象2
    manager2 = BookManager()


# 创建英雄模型
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
    # 逻辑删除：Boolean类型
    isDelete = models.BooleanField(default=False)
    # 所属书名：外键
    book = models.ForeignKey('Book')

    # 定义元选项
    class Meta():
        db_table = "hero"

    # 自定义输出内容
    def __str__(self):
        return '%s' % self.name

from django.db import models


# Create your models here.

# 图书模型
class Book(models.Model):
    # 主键id是个自增列会自动生成不用设置

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

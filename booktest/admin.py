"""
Django提供了admin.ModelAdmin类,通过定义其子类来自定义模型在admin界面的显示方式
"""

from django.contrib import admin
from .models import Book, Hero

# Register your models here.


# 关联对象
class HeroInline(admin.TabularInline):
    """
    StackedInline: 堆放型内嵌方式
    TabularInline: 表格型内嵌方式
    """

    # 指定模型
    model = Hero

    # 设定可额外添加的模型数量
    extra = 3


class BookAdmin(admin.ModelAdmin):

    # list_display：显示字段(可调整字段顺序且字段可排序)
    list_display = ['id', 'title', 'pub_time']

    # list_filter：过滤字段(右侧会出现过滤框)
    list_filter = ['title']

    # search_fields：搜索字段(上方会出现搜索框)
    search_fields = ['title']

    # list_per_page：设置分页
    list_per_page = 3

    # fieldsets：给字段分组
    fieldsets = [
        ('基础信息', {'fields': ['title']}),
        ('其它信息', {'fields': ['pub_time']}),
    ]

    # 在一对多模型的一方添加关联对象
    inlines = [HeroInline]


class HeroAdmin(admin.ModelAdmin):

    # list_display：显示字段(可调整字段顺序且字段可排序)
    list_display = ['id', 'name', 'sex', 'introduce']

    # list_filter：过滤字段(右侧会出现过滤框)
    list_filter = ['name']

    # search_fields：搜索字段(上方会出现搜索框)
    search_fields = ['name']

    # fieldsets：字段分组
    fieldsets = [
        ('基础信息', {'fields': ['name']}),
        ('其它信息', {'fields': ['gender', 'introduce']}),
    ]


# 注册模型到admin
admin.site.register(Book, BookAdmin)
admin.site.register(Hero, HeroAdmin)

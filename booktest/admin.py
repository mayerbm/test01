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

    # 设定可额外添加的数量
    extra = 3


# 自定义管理页面：定义模型在admin界面的展示方式
class BookAdmin(admin.ModelAdmin):

    # list_display：显示字段(可调整字段顺序且字段可排序)
    list_display = ['id', 'title', 'pub_time',]

    # list_filter：过滤字段(右侧会出现过滤框)
    list_filter = ['title']

    # search_fields：搜索字段(上方会出现搜索框)
    search_fields = ['title']

    # list_per_page：设置分页
    list_per_page = 3

    # fieldsets：字段分组
    fieldsets = [
        ('基础信息', {'fields': ['title']}),
        ('其它信息', {'fields': ['pub_time']}),
    ]

    # 添加关联对象
    inlines = [HeroInline]


# 注册模型到admin
admin.site.register(Book, BookAdmin)
admin.site.register(Hero)

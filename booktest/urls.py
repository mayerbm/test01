from django.conf.urls import url
from . import views

urlpatterns = [
    # 定义正则和对应的视图
    url('^$',views.index),
    url('\d+', views.detail)
]
from django.conf.urls import url
from . import views

urlpatterns = [
    # 注册
    url('^register$', views.register, name='register'),
    url('^register_handle$', views.register_handle, name='register_handle'),
]
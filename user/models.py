from django.db import models

# Create your models here.


from django.db import models

# Create your models here.

class UserInfo(models.Model):
    # 用户名
    name = models.CharField(max_length=20)
    # 密码
    pwd = models.CharField(max_length=40)  # SHA加密后长度为40
    # 邮箱
    email = models.CharField(max_length=20)
    # 手机号码
    mobile = models.CharField(max_length=11)
    # 收货地址
    address1 = models.CharField(max_length=20)
    # 详细地址
    address2 = models.CharField(max_length=50)
    # 邮编
    zipcode = models.CharField(max_length=6)

    class Meta():
        # 修改默认表名
        db_table = "userinfo"
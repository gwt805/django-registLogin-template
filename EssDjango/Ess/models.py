from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    powerGender = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))
    username = models.CharField(max_length=128, primary_key=True, verbose_name="用户名")
    zhuname = models.CharField(max_length=128, null=False, verbose_name="姓名",)
    password = models.CharField(max_length=128, null=False, verbose_name="密码")
    email = models.EmailField(max_length=256, null=False, verbose_name="邮箱", blank=True)
    power = models.CharField(max_length=1, choices=powerGender, default=4, verbose_name="权限", blank=True)
    createtime = models.DateTimeField(auto_created=True, auto_now=True, verbose_name="创建时间")
    updatetime = models.DateTimeField(auto_now=True, auto_created=True, verbose_name="修改时间")
    isactivate = models.BooleanField(default=0, verbose_name="激活状态", blank=True)

    class Meta:
        db_table = 'User'

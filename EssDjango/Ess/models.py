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


class AnnoCheckTask(models.Model):
    uname = models.CharField(max_length=128, verbose_name="用户名")  # 用户名
    pname = models.CharField(max_length=256, null=True, verbose_name="项目名字", blank=True)  # 项目类型
    waibao = models.CharField(max_length=256, null=True, verbose_name="数据标注方", blank=True)
    taskId = models.BigIntegerField(null=True, verbose_name="任务ID", blank=True)  # 任务ID
    dtime = models.DateField(max_length=20, verbose_name="当天日期")  # 当天日期
    tkinds = models.CharField(max_length=256, verbose_name="任务类型")  # 任务类型：标注，审核，其他
    pnums = models.IntegerField(null=False, verbose_name="图片数量", blank=True)  # 图片数量
    knums = models.IntegerField(null=True, verbose_name="框数", blank=True)  # 标注框数量
    ptimes = models.FloatField(null=False, verbose_name="工时")  # 工时

    class Meta:
        db_table = 'AnnoCheckTask'


class Project(models.Model):
    pname = models.CharField(max_length=256, unique=True, verbose_name="项目名字", blank=True)  # 项目类型

    def __str__(self):
        return self.pname
    
    class Meta:
        db_table = 'ProjectName'


class Tkinds(models.Model):
    tkinds = models.CharField(max_length=20, unique=True, verbose_name="任务类型")  # 任务类型：标注，审核，其他

    def __str__(self):
        return self.tkinds
    
    class Meta:
        db_table = 'TaskKinds'


class Supplier(models.Model):
    sname = models.CharField(max_length=128, verbose_name="外包名字")

    def __str__(self):
        return self.sname

    class Meta:
        db_table = 'SupplierName'


class SupplierData(models.Model):
    pname = models.CharField(null=False, max_length=256, verbose_name="项目名字", blank=True)  # 项目名字
    getTime = models.DateField(null=False, verbose_name="收到标注结果时间")  # 收到标注数据时间
    pnums = models.IntegerField(null=False, verbose_name="图片数量", blank=True)  # 图片/点云数量
    knums = models.IntegerField(null=False, verbose_name="框数", blank=True)  # 标注框数量
    method = models.CharField(null=False, max_length=256, verbose_name="结算方式", blank=True)  # 结算方式
    unitPrice = models.FloatField(null=False, verbose_name="单价", blank=True)  # 单价
    wbNname = models.CharField(null=False, max_length=256, verbose_name="外包名字", blank=True)  # 外包名字

    class Meta:
        db_table = 'SupplierData'
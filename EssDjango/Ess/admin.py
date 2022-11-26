from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header = "任务统计系统"
admin.site.site_title = "ESS Infor"
admin.site.index_title = "数据管理"


@admin.register(models.User)
class ControlUser(UserAdmin):
    list_display = ("username", "zhuname", "password", "email", "power", "createtime", "updatetime", "isactivate")
    list_editable = ["zhuname", "power", "isactivate"]

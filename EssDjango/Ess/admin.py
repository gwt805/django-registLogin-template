from django.utils.translation import gettext_lazy
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header = "任务统计系统"
admin.site.site_title = "ESS Infor"
admin.site.index_title = "数据管理"


@admin.register(models.User)
class ControlUser(UserAdmin):
    list_display = ("username", "zhuname", "password", "email",
                    "power", "createtime", "updatetime", "isactivate")
    list_editable = ["zhuname", "power", "isactivate"]

@admin.register(models.AnnoCheckTask)
class ControlTASK(admin.ModelAdmin):
    list_display = (
        "uname",
        "pname",
        "waibao",
        "taskId",
        "dtime",
        "tkinds",
        "pnums",
        "knums",
        "ptimes",
    )
    ordering = ("-dtime",)


@admin.register(models.Project)
class ControlPorject(admin.ModelAdmin):
    list_display = ("pname",)


@admin.register(models.Tkinds)
class ControlTkinds(admin.ModelAdmin):
    list_display = ("tkinds",)


@admin.register(models.Supplier)
class ControlWaibaos(admin.ModelAdmin):
    list_display = ("sname",)


@admin.register(models.SupplierData)
class ControlWaibao(admin.ModelAdmin):
    list_display = (
        "pname",
        "getTime",
        "pnums",
        "knums",
        "method",
        "unitPrice",
        "wbNname",
    )
    ordering = ("-getTime",)

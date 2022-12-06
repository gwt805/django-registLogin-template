<div align="center">
    <img src="EssDjango/static/imgs/logo_ess.png" style='margin:50px' height=50px>
</div>


# django-registLogin-template
Django 登录注册模板，管理员可在后台更改用户密码等信息；用户注册后，会将用户名及密码发送到用户邮箱

# 运行
```
项目目录为 EssDjango，Django版本：3.2.14

1. 先配置 EssDjango/config.json，修改数据库信息和邮箱地址及邮箱授权码

2. python manage.py makemigrations

3. python manage.py migrate

4. python manage.py runserver 地址:端口；eg: python manage.py runserver 0.0.0.0:80

在执行第四步之前，可以先创建一个超级/管理员账号: python manage.py createsuperuser, 然后根据提示填写即可

本项目示例登录地址为：地址:端口/ess/login , admin登录地址：地址:端口/admin

```
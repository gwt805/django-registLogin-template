from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from EssDjango import settings
from . import models
# from django.db.models import Q
import threading
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from loguru import logger
from django.http import QueryDict



'''
django  ajax put delete 请求, url 必须以 / 结尾
from django.http import QueryDict
@csrf_exempt
def regist(request):
    if request.method == "PUT":
        print("PUT请求")
        put = QueryDict(request.body)
        key = put.get('key')
        field = put.get('field')
        field_value = put.get('field-value')
        return JsonResponse({'data':"error"})
'''

# Create your views here.

# 密码加密
# def hash_code(pwd):  # 加点盐
    # return pbkdf2_sha256.encrypt(pwd)


def sendEmail(username: str, password: str, email: str):
    def thread_task():
        try:
            config = settings.CONFIG
            smtp_server = 'smtp.qq.com'
            message = f"尊敬的小主您好，\
                您的ESS系统账号是 {username}, 密码是 {password}, \
                您也可以用本邮箱作为账号登录。请一定保管好您的账号密码，切勿告知于他人！"
            msg = MIMEText(message, 'plain', 'utf-8')
            msg['From'] = Header("ESS系统")
            msg['To'] = Header(username)
            msg['Subject'] = Header("ESS 系统")

            server = smtplib.SMTP_SSL(smtp_server)
            server.connect(smtp_server, 465)
            server.login(config["send_email"], config["password"])
            server.sendmail(config["send_email"], email, msg.as_string())
            server.quit()

            logger.info(f"用户名和密码已发送到用户 {username} 邮箱")
        except:
            logger.error(f"用户 {username} 的邮箱可能不是真的!")
    task = threading.Thread(target=thread_task)
    task.start()


@csrf_exempt
def regist(request):
    if request.method == "POST":
        data = QueryDict(request.body)
        username = data.get("user")
        zhuname = data.get("zhuname")
        email = data.get("email")
        password = data.get("pwd")
        username_list = [u[0] for u in models.User.objects.values_list("username")]
        email_list = [e['email'] for e in models.User.objects.values("email")]
        zhuname_list = [zhn[0] for zhn in models.User.objects.values_list("zhuname")]

        if username in username_list and email in email_list and zhuname in zhuname_list:
            return JsonResponse({'data': '用户名和邮箱和姓名都已占用!'})
        elif username in username_list:
            return JsonResponse({'data': '用户名已占用!'})
        elif email in email_list:
            return JsonResponse({'data': '邮箱已占用!'})
        elif zhuname in zhuname_list:
            return JsonResponse({'data': '姓名已占用'})
        else:
            user_table = models.User()
            user_table.username = username
            user_table.zhuname = zhuname
            user_table.set_password(password)
            user_table.email = email
            user_table.save()
            logger.info(f"用户 {username}&{zhuname} 注册成功")
            sendEmail(username, password, email)
            return JsonResponse({'data': 'successful'})
    return render(request, "regist.html")


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = QueryDict(request.body)
        username = data.get("user")
        password = data.get("pwd")
        if len(models.User.objects.filter(username=username)) == True:
            pwd_flag = check_password(password,make_password(password))
            if pwd_flag:
                zhuname = models.User.objects.get(username=username).zhuname
                logger.info(f"用户 {username}&{zhuname} 登录成功")
                return JsonResponse({'data': 'successful', 'zhuname': zhuname})
        elif len(models.User.objects.filter(email=username)) == True:
            pwd_flag = check_password(password,make_password(password))
            if pwd_flag:
                zhuname = models.User.objects.get(username=username).zhuname
                logger.info(f"用户 {username}&{zhuname} 登录成功")
                return JsonResponse({'data': 'successful', 'zhuname': zhuname})
        else:
            return JsonResponse({'data': '账号或密码错误!'})
            
    return render(request, "login.html")


def index(request):

    return render(request, "index.html")

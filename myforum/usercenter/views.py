# coding: utf-8

import uuid
import datetime
import os

from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from PIL import Image

from models import ActivateCode

def register(request):
    if request.method == "GET":
        return render(request, "usercenter_register.html")
    else:
    	error = ''
        username = request.POST["username"].strip()
        password = request.POST["password"].strip()
        email = request.POST["email"].strip()
        re_password = request.POST["re_password"].strip()
        if password != re_password:
        	error = u'两次的密码不一致'
        if not request.POST["username"] or not request.POST["password"] or not request.POST["email"]:
            error = u'字段不能空'
        if error:
        	messages.add_message(request, messages.INFO, error)
        	return redirect(reverse('usercenter_register'))

        new_user = User.objects.create_user(username=username,password=password,email=email)
        new_user.is_active = False
        new_user.save()

        new_code = str(uuid.uuid4()).replace('-','')
        expire_time = datetime.datetime.now() + datetime.timedelta(days=2)
        code_record = ActivateCode(owner=new_user,code=new_code,expire_timestamp=expire_time)
        code_record.save()

        activate_url = "http://%s%s" % (request.get_host(),reverse("usercenter_activate",args=[new_code]))
        send_mail(u'激活邮件', u'你的激活链接为: %s'%activate_url, '592510474@qq.com' ,[email], fail_silently=False)
        return redirect(reverse('login'))

def activate(request,new_code):
	query = ActivateCode.objects.filter(code=new_code,expire_timestamp__gte=datetime.datetime.now())
	if query.count() > 0 :
		code_record = query[0]
		code_record.owner.is_active = True
		code_record.owner.save()
		return HttpResponse(u'激活成功，请登录')
	else:
		return HttpResponse(u'激活失败')

@login_required
def upload_avatar(request):
    if request.method == 'GET':
        return render(request, "upload_avatar.html")
    else:
        profile = request.user.userprofile
        avatar_file = request.FILES.get("avatar", None)
        print avatar_file.size
        file_path = os.path.join("/Users/chao/userres/avatar", avatar_file.name)

        # 避免头像重名，进行检测，如果冲突，改名
        i = 0
        while os.path.exists(file_path):
            file_path = os.path.join("/Users/chao/userres/avatar", str(i) + avatar_file.name)
            i += 1

        with open(file_path, "wb+") as avatar:
            for chunk in avatar_file.chunks():
                avatar.write(chunk)

        # 限制头像文件的大小，如果过大，用 pillow 压缩保存
        if avatar_file.size > 186025:
            THUMB_SIZE = 500,300
            image = Image.open(file_path)
            image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
            image.save(file_path)

        url = "http://0.0.0.0:9988/avatar/%s" % avatar_file.name
        profile.avatar = url
        profile.save()
        return redirect("/")


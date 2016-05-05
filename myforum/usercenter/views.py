# coding: utf-8

from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
import uuid
import datetime
from django.contrib.auth.models import User
from models import ActivateCode
from django.core.mail import send_mail

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
        	# return render(request, "usercenter_register.html", {'username':username,'email':email})
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
        # messages.add_message(request, messages.INFO, u'已发送激活邮件到您的注册邮箱，请点击进行激活')
        return redirect(reverse('login'))

def activate(request,new_code):
	query = ActivateCode.objects.filter(code=new_code,expire_timestamp__gte=datetime.datetime.now())
	if query.count() > 0 :
		code_record = query[0]
		code_record.owner.is_active = True
		code_record.owner.save()
		return HttpResponse(u'激活成功，请登录')
	# 	messages.add_message(request, messages.INFO, u'激活成功，请登录')
	# else:
	# 	messages.add_message(request, messages.INFO, u'激活失败')
	# return redirect(reverse('login'))



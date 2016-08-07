# coding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class ActivateCode(models.Model):
	owner = models.ForeignKey(User, verbose_name=u"用户")
	code = models.UUIDField(u'激活码', editable=False)
	expire_timestamp = models.DateTimeField(u'过期时间')

	create_timestamp = models.DateTimeField(u"创建时间", auto_now_add=True)
	last_update_timestamp = models.DateTimeField(u"最后更新时间", auto_now=True)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	sex = models.IntegerField(u"性别", choices=((0,u"男"),(-1,u"女")), default=0)
	birthday = models.DateTimeField(u"生日",null=True,blank=True)
	avatar = models.CharField(u"头像",max_length=300,blank=True)

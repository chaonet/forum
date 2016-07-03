# coding: utf-8

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class UserMessage(models.Model):
	owner = models.ForeignKey(User, verbose_name=u"拥有者")
	content = models.TextField(u"内容", max_length=10000)
	link = models.CharField(u"连接", max_length=400)
	status = models.IntegerField(u"状态", choices=((0,u"未读"), (1,u"已读")), default=0)

	create_timestamp = models.DateTimeField(u"创建时间", auto_now_add=True)
	last_update_timestamp = models.DateTimeField(u"最后更新时间", auto_now=True)

	def __unicode__(self):
		return self.content

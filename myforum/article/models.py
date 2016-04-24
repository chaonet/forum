# coding: utf-8

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from block.models import Block

class Article(models.Model):
	block = models.ForeignKey(Block, verbose_name=u"所属版块")
	owner = models.ForeignKey(User, verbose_name=u"作者")
	title = models.CharField(u"标题", max_length=100)
	content = models.CharField(u"内容", max_length=10000)
	status = models.IntegerField(u"状态", choices=((0,u"普通"),(-1,u"删除"),(1,u"精华")),default=0)

	create_timestamp = models.DateTimeField(u"创建时间", auto_now_add=True)
	last_update_timestamp = models.DateTimeField(u"最后更新时间", auto_now=True)

	def __unicode__(self):
		return self.title

	class Meta: # 表的元属性
		# verbose_name = u"文章"  # 在管理后台登进去后显示的名称
		verbose_name_plural = u"文章"  # 定义复数形式如何显示

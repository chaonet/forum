# coding: utf-8

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from block.models import Block
from article.models import Article

class Comment(models.Model):
	block = models.ForeignKey(Block, verbose_name=u"所属版块")
	article = models.ForeignKey(Article, verbose_name=u"所属文章")
	owner = models.ForeignKey(User, verbose_name=u"评论者")
	content = models.TextField(u"内容", max_length=10000)
	status = models.IntegerField(u"状态", choices=((0,u"普通"), (-1,u"删除")), default=0)
	to_comment_id = models.IntegerField(u'回复评论', default=0)

	create_timestamp = models.DateTimeField(u"创建时间", auto_now_add=True)
	last_update_timestamp = models.DateTimeField(u"最后更新时间", auto_now=True)

	def __unicode__(self):
		return self.content[:20]

	class Meta:
		verbose_name_plural = u"评论"

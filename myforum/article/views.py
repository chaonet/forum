# coding: utf-8

from django.shortcuts import render

# Create your views here.
from block.models import Block
from models import Article

def article_list(request,block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)
	# print block
	# 部落建设  版块名称
	articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")
	return render(request, "article_list.html", {"articles":articles,"block":block})

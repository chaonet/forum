# coding: utf-8

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from django.contrib.auth.models import User
from block.models import Block
from models import Article

def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")
    return render(request, "article_list.html", {"articles":articles,"b":block})

@login_required
def article_create(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render(request, "article_create.html", {"b":block})
    else:
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not request.POST["title"] or not request.POST["content"]:
            messages.add_message(request, messages.INFO, u'标题和内容不能空！')
            return render(request, "article_create.html", {"b":block,'title':title,'article_content':content})
        new_article = Article(block=block,owner=request.user,title=title,content=content)
        new_article.save()
        messages.add_message(request, messages.INFO, u'发表成功！')
        return redirect(reverse('article_list',args=[block.id]))

def article_detail(request,article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    return render(request, "article_detail.html", {"article":article})
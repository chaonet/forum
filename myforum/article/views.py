# coding: utf-8

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

# Create your views here.
from django.contrib.auth.models import User
from block.models import Block
from models import Article

def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")
    return render(request, "article_list.html", {"articles":articles,"b":block})

def article_create(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    context_instance = RequestContext(request)
    if request.method == "GET":
        return render(request, "article_create.html", {"b":block})
    else:
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not request.POST["title"] or not request.POST["content"]:
            return render(request, "article_create.html", {"b":block,'title':title,'article_content':content},context_instance = context_instance)
        owner = User.objects.all()[0] # TODO:
        request.POST["title"].strip()  # request 对象，字典
        request.POST["content"].strip()
        new_article = Article(block=block,owner=owner,title=title,content=content)
        new_article.save()
        return redirect(reverse('article_list',args=[block.id]))

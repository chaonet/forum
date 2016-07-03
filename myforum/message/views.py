# coding: utf-8

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from models import UserMessage
from comment.models import Comment
from article.models import Article

@login_required
def list_message(request):
    unread_message = UserMessage.objects.filter(owner=request.user, status=0).order_by("-id")
    readed_message = UserMessage.objects.filter(owner=request.user, status=1).order_by("-id")
    return render(request, 'list_message.html', {"unread_message":unread_message, 'readed_message':readed_message})

@login_required
def read_message(request,message_id):
    message = UserMessage.objects.get(id=int(message_id))
    message.status=1
    message.save()
    return redirect(message.link)

@login_required
def detail_message(request,article_id,comment_id):
    article_id = int(article_id)
    comment_id = int(comment_id)
    article = Article.objects.get(id=article_id)
    comment = Comment.objects.get(id=comment_id)
    return render(request, 'message_detail.html', {"article":article, "comment":comment})

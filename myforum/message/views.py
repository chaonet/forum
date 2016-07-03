# coding: utf-8

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from models import UserMessage

@login_required
def list_message(request):
    unread_message = UserMessage.objects.filter(owner=request.user, status=0).order_by("-id")
    readed_message = UserMessage.objects.filter(owner=request.user, status=1).order_by("-id")
    return render(request, 'list_message.html', {"unread_message":unread_message, 'readed_message':readed_message})

@login_required
def read_message(request):
    message = UserMessage.objects.get(id=int(message_id))
    message(status=1)
    message.save()
    return redirect(message.link)

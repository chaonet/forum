from django.shortcuts import render

from models import Block
from message.models import UserMessage

def block_list(request):
	if request.user.is_authenticated():
		msg_cnt = UserMessage.objects.filter(owner=request.user, status=0).count()
	else:
		msg_cnt = 0
	# print msg_cnt
	blocks = Block.objects.all().order_by("-id")
	return render(request, "block_list.html", {"blocks":blocks, "msg_cnt":msg_cnt})

from django.shortcuts import render

# Create your views here.
from models import Block

def block_list(request):
	blocks = Block.objects.all().order_by("-id")
	return render(request, "block_list.html", {"blocks":blocks})
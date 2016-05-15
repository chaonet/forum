from django.contrib.auth.decorators import login_required

from models import Comment
from article.models import Article
from utils.response import json_response

@login_required
def comment_create(request):
    article_id = int(request.POST["article_id"])
    content = request.POST["content"].strip()
    to_comment_id = int(request.POST["to_comment_id"])
    # print article_id, content, to_comment_id

    article = Article.objects.get(id=article_id)
    # print article
    comment = Comment(block=article.block, article=article, 
    				  owner=request.user, content=content, 
    				  to_comment_id=to_comment_id
    				 )
    comment.save()
    return json_response({})
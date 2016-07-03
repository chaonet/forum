# coding: utf-8

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from models import Comment
from article.models import Article
from message.models import UserMessage
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
    if to_comment_id == 0:
      owner=article.owner
      content=u"有人评论了您的文章 %s" % article.title
    else:
      owner=comment.to_comment.owner
      content=u"有人评论了您的评论 %s" % comment.to_comment.content[:30]
    
    new_message = UserMessage(owner=owner, 
                              content=content, 
                              link=reverse("detail_message", args=[int(article_id), int(comment.id)])
                              )
    new_message.save()
    return json_response({})
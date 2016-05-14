# coding: utf-8

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

from block.models import Block
from comment.models import Comment
from models import Article

def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")
    # return render(request, "article_list.html", {"articles":articles,"b":block})

    page_no = int(request.GET.get('page_no','1'))
    p = Paginator(articles, 1)
    if page_no < 0:
        page_no = 1
    if page_no > p.num_pages:
        page_no = p.num_pages
    page_list = [i for i in range(page_no - 5, page_no + 6) if i > 0 and i <= p.num_pages]
    page = p.page(page_no)
    previous_link = page_list[0] - 1
    next_link = page_list[-1] + 1
    first_link = page_list[0] - 2
    last_link = page_list[-1] + 2
    return render(request, 'article_list.html', 
                  {"articles":page.object_list,"b":block,
                   "has_previous":previous_link>0, "has_next":next_link<=p.num_pages,
                   "has_first":first_link>0, "has_last":last_link<=p.num_pages,
                   "previous_link":previous_link,
                   "next_link":next_link,
                   "current_no":page_no,
                   "pages_num":p.num_pages,
                   "page_list":page_list
                  }
                 )
    

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
    # return render(request, "article_detail.html", {"article":article})

    comments = Comment.objects.filter(article=article).order_by("-last_update_timestamp")
    comment_page_no = int(request.GET.get('comment_page_no','1'))
    p = Paginator(comments, 1)
    if comment_page_no < 0:
        comment_page_no = 1
    if comment_page_no > p.num_pages:
        comment_page_no = p.num_pages
    page_list = [i for i in range(comment_page_no - 5, comment_page_no + 6) if i > 0 and i <= p.num_pages]
    page = p.page(comment_page_no)
    previous_link = page_list[0] - 1
    next_link = page_list[-1] + 1
    first_link = page_list[0] - 2
    last_link = page_list[-1] + 2
    return render(request, 'article_detail.html',
                  {"article":article, "comments":page.object_list,
                   "has_previous":previous_link>0, "has_next":next_link<=p.num_pages,
                   "has_first":first_link>0, "has_last":last_link<=p.num_pages,
                   "previous_link":previous_link,
                   "next_link":next_link,
                   "current_no":comment_page_no,
                   "pages_num":p.num_pages,
                   "page_list":page_list
                  }
                 )

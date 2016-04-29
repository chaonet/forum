from django.conf.urls import url
from django.contrib import admin

from views import article_list,article_create

urlpatterns = [
    url(r'list/(?P<block_id>[0-9]+)/$', article_list, name = 'article_list'),
    url(r'create/(?P<block_id>[0-9]+)/$', article_create, name = 'article_create'),
]
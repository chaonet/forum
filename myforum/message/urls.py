from django.conf.urls import url
from django.contrib import admin

from views import list_message, read_message, detail_message

urlpatterns = [
    url(r'list/$', list_message, name='list_message'),
    url(r'read/(?P<message_id>[0-9]+)/', read_message, name='read_message'),
    url(r'detail/(?P<article_id>[0-9]+)/(?P<comment_id>[0-9]+)/$', detail_message, name='detail_message'),
]
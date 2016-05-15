from django.conf.urls import url, include
from django.contrib import admin

from views import comment_create

urlpatterns = [
    url(r'create/$', comment_create ,name='comment_create'),
]
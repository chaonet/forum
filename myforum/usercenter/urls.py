from django.conf.urls import url, include
from django.contrib import admin

from views import register, activate

urlpatterns = [
    url(r'register/$', register ,name='usercenter_register'),
    url(r'activate/(?P<article_id>[0-9a-f]{32})/$', activate ,name='usercenter_activate'),
    # url(r'^logout/', include('django.contrib.auth.urls'),name='logout'),
]
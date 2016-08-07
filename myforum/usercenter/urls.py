from django.conf.urls import url, include
from django.contrib import admin

from views import register, activate, upload_avatar

urlpatterns = [
    url(r'register/$', register ,name='usercenter_register'),
    url(r'activate/(?P<new_code>[0-9a-f]{32})/$', activate ,name='usercenter_activate'),
    url(r'avatar/$', upload_avatar, name='upload_avatar'),
]
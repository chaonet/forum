#!/usr/bin/env python
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myforum.settings")

import django
django.setup()

from usercenter.models import UserProfile
from django.contrib.auth.models import User
for u in User.objects.all():
	profile = UserProfile(user=u)
	profile.save()

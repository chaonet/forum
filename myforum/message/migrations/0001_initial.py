# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-03 03:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=10000, verbose_name='\u5185\u5bb9')),
                ('link', models.CharField(max_length=400, verbose_name='\u8fde\u63a5')),
                ('status', models.IntegerField(choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb')], default=0, verbose_name='\u72b6\u6001')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_update_timestamp', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u4f5c\u8005')),
            ],
        ),
    ]

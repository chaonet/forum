# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 08:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='block_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7ba1\u7406\u5458'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 01:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20160417_0836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='block_admin',
            new_name='admin',
        ),
        migrations.RenameField(
            model_name='block',
            old_name='block_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='block',
            old_name='block_name',
            new_name='name',
        ),
    ]

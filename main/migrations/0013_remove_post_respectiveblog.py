# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20160110_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='respectiveblog',
        ),
    ]

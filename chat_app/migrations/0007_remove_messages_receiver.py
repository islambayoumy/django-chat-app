# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 22:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0006_auto_20170611_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='receiver',
        ),
    ]
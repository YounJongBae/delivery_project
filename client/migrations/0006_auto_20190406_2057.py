# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-06 11:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20190405_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['created_at']},
        ),
    ]

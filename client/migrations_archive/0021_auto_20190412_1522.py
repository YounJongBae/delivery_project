# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-12 06:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0020_auto_20190412_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={},
        ),
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='created_at',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-03 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0004_partner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.TextField(verbose_name='메뉴 이름'),
        ),
    ]

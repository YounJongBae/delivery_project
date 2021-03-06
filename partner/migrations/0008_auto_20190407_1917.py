# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-07 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0007_partner_food_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='food_categories',
        ),
        migrations.AddField(
            model_name='partner',
            name='category',
            field=models.CharField(choices=[('KR', '한식'), ('WE', '양식'), ('JR', '일식'), ('DE', '디저트')], default=2, max_length=10, verbose_name='카테고리'),
            preserve_default=False,
        ),
    ]

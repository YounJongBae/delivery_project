# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-02 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_auto_20190331_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='가게 사진'),
            preserve_default=False,
        ),
    ]
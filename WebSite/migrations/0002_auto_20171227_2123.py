# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-28 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='basename',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='file',
            name='path',
            field=models.CharField(max_length=200),
        ),
    ]

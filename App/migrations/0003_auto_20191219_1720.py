# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-19 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20191219_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_age',
            field=models.IntegerField(verbose_name=3),
        ),
    ]
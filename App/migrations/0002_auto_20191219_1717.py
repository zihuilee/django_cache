# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-19 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_age',
            field=models.IntegerField(max_length=3),
        ),
    ]

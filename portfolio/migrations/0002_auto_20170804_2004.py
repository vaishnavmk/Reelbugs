# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-04 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

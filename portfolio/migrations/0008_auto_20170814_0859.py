# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-14 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20170810_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='summary',
            field=models.CharField(default='A story on blumury', max_length=800),
        ),
    ]

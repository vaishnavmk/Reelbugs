# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-19 06:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20170819_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]

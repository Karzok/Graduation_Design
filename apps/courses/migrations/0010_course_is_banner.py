# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-04-24 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20190331_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6e\u64ad'),
        ),
    ]
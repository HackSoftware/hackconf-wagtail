# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-11 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0063_auto_20190908_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='is_goodbye_drink',
            field=models.BooleanField(default=False),
        ),
    ]
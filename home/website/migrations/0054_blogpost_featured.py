# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0053_blogpost_grid_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]

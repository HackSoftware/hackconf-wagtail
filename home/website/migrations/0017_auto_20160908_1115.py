# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-08 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20160908_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='topic',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='topic',
            field=models.CharField(max_length=255),
        ),
    ]

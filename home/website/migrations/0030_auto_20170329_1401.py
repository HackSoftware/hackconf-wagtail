# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-29 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_auto_20170329_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='header_dates_bg',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='header_dates_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
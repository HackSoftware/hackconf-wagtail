# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-07 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_homepage_header_dates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='video_url',
        ),
        migrations.AddField(
            model_name='homepage',
            name='video_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

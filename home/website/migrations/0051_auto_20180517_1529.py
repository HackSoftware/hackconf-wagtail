# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-17 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0050_homepage_footer_cookie_statement_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='old_partners_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='old_partners_title_bg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='old_partners_title_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-07 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0059_auto_20190815_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheduledayone',
            old_name='lecture',
            new_name='lecture_hall_1',
        ),
        migrations.RenameField(
            model_name='scheduledaytwo',
            old_name='lecture',
            new_name='lecture_hall_1',
        ),
        migrations.AddField(
            model_name='scheduledayone',
            name='lecture_hall_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='website.Lecture'),
        ),
        migrations.AddField(
            model_name='scheduledaytwo',
            name='lecture_hall_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='website.Lecture'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-26 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20160913_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherPartners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_partners', to='website.HomePage')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='website.Partner')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
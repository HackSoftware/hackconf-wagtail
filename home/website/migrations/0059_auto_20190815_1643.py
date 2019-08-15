# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-15 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0058_auto_20190707_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccomodationPartners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StickerPartners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='homepage',
            name='accomodation_partners_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='accomodation_partners_title_bg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='accomodation_partners_title_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='show_accomodation_partners',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='show_sticker_partners',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sticker_partners_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sticker_partners_title_bg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sticker_partners_title_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stickerpartners',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='sticker_partners', to='website.HomePage'),
        ),
        migrations.AddField(
            model_name='stickerpartners',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='website.Partner'),
        ),
        migrations.AddField(
            model_name='accomodationpartners',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='accomodation_partners', to='website.HomePage'),
        ),
        migrations.AddField(
            model_name='accomodationpartners',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='website.Partner'),
        ),
    ]

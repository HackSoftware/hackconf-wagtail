# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-07 07:34
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_homepage_call_for_speakers_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='attendees_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='fb_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sponsors_partnership_description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sponsors_partnership_document_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sponsors_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='streaming_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
    ]

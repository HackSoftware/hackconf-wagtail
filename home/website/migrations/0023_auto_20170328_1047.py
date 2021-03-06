# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-28 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_homepage_live_stream'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about_text_bg',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_text_en',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='call_for_speakers_title_bg',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='call_for_speakers_title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='header_text_bg',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='header_text_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='live_bg',
            field=models.BooleanField(default=True, editable=False, verbose_name='live'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='live_en',
            field=models.BooleanField(default=True, editable=False, verbose_name='live'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='search_description_bg',
            field=models.TextField(blank=True, null=True, verbose_name='search description'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='search_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='search description'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='seo_title_bg',
            field=models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='seo_title_en',
            field=models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slug_bg',
            field=models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slug_en',
            field=models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_bg',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='url_path_bg',
            field=models.TextField(blank=True, editable=False, null=True, verbose_name='URL path'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='url_path_en',
            field=models.TextField(blank=True, editable=False, null=True, verbose_name='URL path'),
        ),
    ]

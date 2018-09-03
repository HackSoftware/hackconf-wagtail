# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-08 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('website', '0015_auto_20160907_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', wagtail.wagtailcore.fields.RichTextField()),
                ('lector', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleDayOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='website.Lecture')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScheduleDayTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='website.Lecture')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('video_url', models.URLField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
        migrations.CreateModel(
            name='SpeakersInfo',
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
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', wagtail.wagtailcore.fields.RichTextField()),
                ('lector', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkshopsDayOne',
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
            name='WorkshopsDayTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='speakers_title',
            new_name='call_for_speakers_title',
        ),
        migrations.AddField(
            model_name='homepage',
            name='show_call_for_speakers_section',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='show_schedule',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='homepage',
            name='show_speakers_section',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workshopsdaytwo',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshops_day_two', to='website.HomePage'),
        ),
        migrations.AddField(
            model_name='workshopsdaytwo',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='website.Workshop'),
        ),
        migrations.AddField(
            model_name='workshopsdayone',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshops_day_one', to='website.HomePage'),
        ),
        migrations.AddField(
            model_name='workshopsdayone',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='website.Workshop'),
        ),
        migrations.AddField(
            model_name='speakersinfo',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='speakers_info', to='website.HomePage'),
        ),
        migrations.AddField(
            model_name='speakersinfo',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='website.Workshop'),
        ),
        migrations.AddField(
            model_name='scheduledaytwo',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_day_two', to='website.HomePage'),
        ),
        migrations.AddField(
            model_name='scheduledayone',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_day_one', to='website.HomePage'),
        ),
    ]
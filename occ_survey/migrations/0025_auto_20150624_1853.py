# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0024_auto_20150624_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.TextField(blank=True)),
                ('update1', models.TextField(blank=True)),
                ('update2', models.TextField(blank=True)),
                ('update3', models.TextField(blank=True)),
                ('profile', models.TextField(blank=True)),
                ('comfort', models.TextField(blank=True)),
                ('control', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phase1_isDone',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phase2_isDone',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='comfort_isDone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='control_isDone',
            field=models.IntegerField(default=0),
        ),
    ]

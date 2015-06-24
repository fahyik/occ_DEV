# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'occ_survey', '0001_initial'), (b'occ_survey', '0002_question_order'), (b'occ_survey', '0003_userprofile'), (b'occ_survey', '0004_userprofile_username'), (b'occ_survey', '0005_loglux'), (b'occ_survey', '0006_loglighting'), (b'occ_survey', '0007_choice')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('answer', models.IntegerField()),
                ('in_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date submitted')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('question_text', models.CharField(max_length=255)),
                ('question_cat', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='occ_survey.Question'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room', models.CharField(max_length=10)),
                ('profile_isDone', models.IntegerField(default=0)),
                ('phase1_isDone', models.IntegerField(default=0)),
                ('phase2_isDone', models.IntegerField(default=0)),
                ('impromptu_count', models.IntegerField(default=0)),
                ('remote_use_count', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(max_length=20, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LogLux',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('g22', models.IntegerField(null=True, db_column=b'G22', blank=True)),
                ('g23', models.IntegerField(null=True, db_column=b'G23', blank=True)),
                ('rpi_0', models.IntegerField(null=True, db_column=b'RPi_0', blank=True)),
                ('g24', models.IntegerField(null=True, db_column=b'G24', blank=True)),
                ('g25_1', models.IntegerField(null=True, db_column=b'G25.1', blank=True)),
                ('g25_2', models.IntegerField(null=True, db_column=b'G25.2', blank=True)),
                ('g26_1', models.IntegerField(null=True, db_column=b'G26.1', blank=True)),
                ('g26_2', models.IntegerField(null=True, db_column=b'G26.2', blank=True)),
                ('g27', models.IntegerField(null=True, db_column=b'G27', blank=True)),
                ('g31_1', models.IntegerField(null=True, db_column=b'G31.1', blank=True)),
                ('g31_2', models.IntegerField(null=True, db_column=b'G31.2', blank=True)),
            ],
            options={
                'db_table': 'log_lux',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LogLighting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('g22', models.IntegerField(null=True, db_column=b'G22', blank=True)),
                ('g23', models.IntegerField(null=True, db_column=b'G23', blank=True)),
                ('rpi_0', models.IntegerField(null=True, db_column=b'RPi_0', blank=True)),
                ('g24', models.IntegerField(null=True, db_column=b'G24', blank=True)),
                ('g25_1', models.IntegerField(null=True, db_column=b'G25.1', blank=True)),
                ('g25_2', models.IntegerField(null=True, db_column=b'G25.2', blank=True)),
                ('g26_1', models.IntegerField(null=True, db_column=b'G26.1', blank=True)),
                ('g26_2', models.IntegerField(null=True, db_column=b'G26.2', blank=True)),
                ('g27w', models.IntegerField(null=True, db_column=b'G27W', blank=True)),
                ('g27f', models.IntegerField(null=True, db_column=b'G27F', blank=True)),
                ('g31_1', models.IntegerField(null=True, db_column=b'G31.1', blank=True)),
                ('g31_2', models.IntegerField(null=True, db_column=b'G31.2', blank=True)),
            ],
            options={
                'db_table': 'log_lighting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('type', models.CharField(max_length=10, choices=[(b'radio', b'radio'), (b'choice', b'choice'), (b'open', b'open-ended-text')])),
                ('choice1', models.CharField(max_length=30, null=True)),
                ('choice2', models.CharField(max_length=30, null=True)),
                ('choice3', models.CharField(max_length=30, null=True)),
                ('choice4', models.CharField(max_length=30, null=True)),
                ('choice5', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]

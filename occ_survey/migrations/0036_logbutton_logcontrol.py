# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0035_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogButton',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('room', models.TextField(null=True, blank=True)),
                ('state', models.IntegerField(null=True, blank=True)),
                ('lux', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'log_button',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LogControl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('name', models.TextField(null=True, blank=True)),
                ('ip', models.TextField(null=True, blank=True)),
                ('room', models.TextField(null=True, blank=True)),
                ('lux', models.IntegerField(null=True, blank=True)),
                ('td', models.IntegerField(null=True, db_column=b'TD', blank=True)),
                ('dt', models.IntegerField(null=True, blank=True)),
                ('action', models.TextField(null=True, blank=True)),
                ('occupied', models.IntegerField(null=True, blank=True)),
                ('dark', models.IntegerField(null=True, blank=True)),
                ('bright', models.IntegerField(null=True, blank=True)),
                ('lights', models.IntegerField(null=True, blank=True)),
                ('buttonontime', models.IntegerField(null=True, db_column=b'buttonOnTime', blank=True)),
                ('buttonofftime', models.IntegerField(null=True, db_column=b'buttonOffTime', blank=True)),
                ('trigger', models.TextField(null=True, blank=True)),
                ('mode', models.IntegerField(null=True, blank=True)),
                ('timetaken', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'log_control',
                'managed': False,
            },
        ),
    ]

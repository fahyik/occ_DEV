# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0033_remove_controladjustments_override'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogOccupancy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('room', models.TextField(null=True, blank=True)),
                ('state', models.IntegerField(null=True, blank=True)),
                ('dsid', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'log_occupancy',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='controlchanges',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

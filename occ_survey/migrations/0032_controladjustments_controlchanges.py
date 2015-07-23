# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0031_structure'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlAdjustments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('room', models.CharField(max_length=20)),
                ('lux_th', models.IntegerField(default=0)),
                ('upp_th', models.IntegerField(default=0)),
                ('td', models.IntegerField(default=0)),
                ('override', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'control_adjustments',
            },
        ),
        migrations.CreateModel(
            name='ControlChanges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('room', models.CharField(max_length=20)),
                ('lux_th_new', models.IntegerField(default=0)),
                ('upp_th_new', models.IntegerField(default=0)),
                ('td_new', models.IntegerField(default=0)),
                ('lux_th', models.IntegerField(default=0)),
                ('upp_th', models.IntegerField(default=0)),
                ('td', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'control_changes',
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0027_auto_20150630_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlLuxThreshold',
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
                ('g32_1', models.IntegerField(null=True, db_column=b'G32.1', blank=True)),
                ('g32_2', models.IntegerField(null=True, db_column=b'G32.2', blank=True)),
            ],
            options={
                'db_table': 'control_lux_threshold',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ControlLuxUpperThreshold',
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
                ('g32_1', models.IntegerField(null=True, db_column=b'G32.1', blank=True)),
                ('g32_2', models.IntegerField(null=True, db_column=b'G32.2', blank=True)),
            ],
            options={
                'db_table': 'control_lux_upper_threshold',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ControlLuxWLights',
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
                ('g32_1', models.IntegerField(null=True, db_column=b'G32.1', blank=True)),
                ('g32_2', models.IntegerField(null=True, db_column=b'G32.2', blank=True)),
            ],
            options={
                'db_table': 'control_lux_w_lights',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ControlTd1',
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
                ('g32_1', models.IntegerField(null=True, db_column=b'G32.1', blank=True)),
                ('g32_2', models.IntegerField(null=True, db_column=b'G32.2', blank=True)),
            ],
            options={
                'db_table': 'control_td1',
                'managed': False,
            },
        ),
    ]

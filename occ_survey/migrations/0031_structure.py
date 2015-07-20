# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0030_controlsetpoints'),
    ]

    operations = [
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('room', models.TextField(null=True, blank=True)),
                ('location', models.TextField(null=True, blank=True)),
                ('ip', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'structure',
                'managed': False,
            },
        ),
    ]

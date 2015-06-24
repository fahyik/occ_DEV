# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0006_loglighting'),
    ]

    operations = [
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

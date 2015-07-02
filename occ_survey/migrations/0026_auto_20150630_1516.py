# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0025_auto_20150624_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice1',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice2',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice3',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice4',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice5',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]

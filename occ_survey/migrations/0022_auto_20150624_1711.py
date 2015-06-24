# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0021_question_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choice_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='name',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0020_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choice',
            field=models.ForeignKey(blank=True, to='occ_survey.Choice', null=True),
        ),
    ]

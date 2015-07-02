# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0026_auto_20150630_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choice_name',
            field=models.CharField(max_length=30, null=True, editable=False, blank=True),
        ),
    ]

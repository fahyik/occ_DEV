# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0012_auto_20150624_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choice',
            field=models.ForeignKey(default=1, to='occ_survey.Choice'),
            preserve_default=False,
        ),
    ]

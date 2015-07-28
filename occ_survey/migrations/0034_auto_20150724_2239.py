# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0033_remove_controladjustments_override'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlchanges',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

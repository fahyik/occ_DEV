# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0048_logoverride'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_notification',
            field=models.IntegerField(default=1),
        ),
    ]

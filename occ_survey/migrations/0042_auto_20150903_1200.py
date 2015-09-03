# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0041_auto_20150903_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logoverride',
            name='control',
        ),
        migrations.RemoveField(
            model_name='logoverride',
            name='user',
        ),
        migrations.DeleteModel(
            name='LogOverride',
        ),
    ]

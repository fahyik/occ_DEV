# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0037_logoverride'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logoverride',
            options={'managed': False},
        ),
    ]

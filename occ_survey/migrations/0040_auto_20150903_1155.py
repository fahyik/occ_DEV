# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0039_auto_20150903_1155'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='logoverride',
            table='log_overrides',
        ),
    ]

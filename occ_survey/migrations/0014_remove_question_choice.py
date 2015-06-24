# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0013_auto_20150624_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choice',
        ),
    ]

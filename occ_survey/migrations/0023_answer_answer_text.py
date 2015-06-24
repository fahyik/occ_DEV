# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0022_auto_20150624_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_text',
            field=models.TextField(blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0008_question_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choice',
            field=models.ForeignKey(default=b'', to='occ_survey.Choice'),
        ),
    ]

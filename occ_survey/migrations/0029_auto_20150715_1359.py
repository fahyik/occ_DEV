# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0028_controlluxthreshold_controlluxupperthreshold_controlluxwlights_controltd1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='remote_use_count',
            new_name='remote_change_count',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='remote_switch_count',
            field=models.IntegerField(default=0),
        ),
    ]

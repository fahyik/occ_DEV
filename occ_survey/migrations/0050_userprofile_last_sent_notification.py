# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occ_survey', '0049_userprofile_is_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_sent_notification',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]

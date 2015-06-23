# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('occ_survey', '0002_question_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room', models.CharField(max_length=10)),
                ('profile_isDone', models.IntegerField(default=0)),
                ('phase1_isDone', models.IntegerField(default=0)),
                ('phase2_isDone', models.IntegerField(default=0)),
                ('impromptu_count', models.IntegerField(default=0)),
                ('remote_use_count', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

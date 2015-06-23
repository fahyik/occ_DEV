# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('answer', models.IntegerField()),
                ('in_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date submitted')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('question_text', models.CharField(max_length=255)),
                ('question_cat', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='occ_survey.Question'),
        ),
    ]
